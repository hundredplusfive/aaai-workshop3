from tools import country_activities, country_cost, country_mthly_weather
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import debug
import re


# Persona configurations
PERSONAS = {
    "emily": {
        "name": "Emily Tan",
        "age": 32,
        "backstory": "A passionate travel blogger who’s explored 40+ countries, loves budget-friendly yet enriching trips",
        "personality": "Friendly, enthusiastic, detail-oriented, always excited to share travel tips",
        "speech_style": "Conversational, clear, uses some travel slang and emojis",
        "tools": ["cost_breakdown", "activities"]  # Emily specializes in budget and cost analysis
    },
    "mark": {
        "name": "Mark Lim",
        "age": 45,
        "backstory": "Former airline agent turned travel planner, specializes in flight deals and logistics",
        "personality": "Professional, precise, efficient, data-driven, calm under pressure",
        "speech_style": "Formal, concise, avoids slang, focuses on facts and numbers",
        "tools": ["weather", "activities"]  # Mark specializes in weather and climate info
    },
    "sara": {
        "name": "Sara Wong",
        "age": 28,
        "backstory": "Adventure seeker and budget traveler, active on social media sharing local hidden gems",
        "personality": "Energetic, adventurous, empathetic, loves personalization",
        "speech_style": "Casual, friendly, uses popular expressions and hashtags",
        "tools": ["activities", "cost_breakdown"]  # Sara specializes in activities and things to do
    }
}


def execute_tool(tool_name):
    """
    Execute a specific tool and return its output.
    Returns Tool output as string
    """
    tool_name = tool_name.lower().strip()

    if tool_name == "cost_breakdown":
        return country_cost()
    elif tool_name == "activities":
        return country_activities()
    elif tool_name == "weather":
        return country_mthly_weather()
    else:
        return f"Unknown tool: {tool_name}"


def participant(persona_id, state) -> dict:
    """
    Generate speech for a persona using ReAct workflow with real tool calling.

    Args:
        persona_id: One of "emily", "mark", "sara"
        state: Current conversation state

    Returns:
        Dict with message updates for state
    """
    if persona_id not in PERSONAS:
        return {"messages": [{"role": "assistant", "content": f"Unknown persona: {persona_id}"}]}

    persona = PERSONAS[persona_id]
    debug(f"\n=== {persona['name']} is thinking... ===")

    # Get recent conversation for context
    messages = state.get("messages", [])
    conversation_text = ""
    for msg in messages: 
        conversation_text += f"{msg.get('content', '')}\n"

    # System prompt for ReAct
    system_prompt = f"""You are {persona['name']}, {persona['age']} years old.
Background: {persona['backstory']}
Personality: {persona['personality']}
Speech style: {persona['speech_style']}

You are part of a Travel Planning Committee that organizes trips based on user preferences and budget.

You run in a loop of Thought, Action, Observation.
At the end of each loop, you output a Message to the user.

Use Thought to describe your current reasoning about the conversation and the user’s needs.
Use Action to invoke one of the tools/functions available to you.
Observation will be the result of that action.

Your goal is to recommend suitable travel destinations, budget breakdowns, and activities tailored to the user’s preferences and budget.

Available actions/tools:

cost_breakdown:
Returns detailed cost estimates for flights, hotels, food, and transport for multiple countries.

weather:
Returns typical weather conditions for each country by month.

activities:
Returns popular activities and attractions for each country.

------

Example session:

Thought: The user mentioned a budget but no trip duration. I should ask for how many days they plan to travel.
Message: Hi! To help plan your trip within your budget, may I know how many days you’re planning to travel?

---

You will be called again with:
User: I want to travel for 7 days.

Thought: Now I have the budget and trip duration. I should check which countries fit the budget.
Action: cost_breakdown

---

You will be called again with:
Observation: [Cost data for countries returned here]

Thought: With the cost data, I can recommend countries that fit the user’s budget for 7 days. I should also suggest popular activities.
Action: activities

---

You will be called again with:
Observation: [Activities data returned here]

Thought: I have enough info to respond with recommendations and activity ideas.
Message: Based on your budget and 7-day trip, you could visit Malaysia or Vietnam. Both offer great activities like exploring Langkawi beaches or cruising Ha Long Bay. Would you like me to help you with flights or accommodation details?

IMPORTANT:
- You can use multiple actions by continuing the loop
- You must not be providing Observation in your response. Observation is a result from tool, not for you to respond.
- DO NOT ask too many questions related to the activities that user would like to do (MAX:1-2 questions will do).
- Once you have narrow down to a country, provide the recommendation without asking further question.
- If you have multiple picks, you should list out and let the user decide instead of coming out with the best fit yourself.
- Don't over-question. if you have basic info (user's cost, weather and activities preference), you must list out the recommedation for users to decide (if there are more than 1) or just list out the recommendation if there is only 1 choice.
- ASK follow-up essential questions to better understand user needs.
- Keep your Message concise (1-2 sentences) and in character
"""

    # Internal loop for ReAct
    max_iterations = 5  # Prevent infinite loops
    internal_context = f"Recent conversation:\n{conversation_text}\n\nContinue the conversation as {persona['name']}.\n"

    for iteration in range(max_iterations):
        user_prompt = internal_context
        debug(f"Iteration {iteration + 1}/{max_iterations}")

        try:
            llm = ChatOpenAI(model="gpt-5-mini", temperature=1)
            response = llm.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ])
            content = response.content.strip()
            debug(f"LLM Response:\n{content}\n")

            # Check if the response contains Message:
            if "Message:" in content:
                # Extract the message
                message_match = re.search(r'Message:\s*(.*)', content, re.DOTALL)
                if message_match:
                    final_message = message_match.group(1).strip()
                    debug(f"Final Message: {final_message}")
                    debug(f"=== End of {persona['name']}'s thought process ===\n")

                    # Return the message to state
                    return {
                        "messages": [{
                            "role": "assistant",
                            "name": persona['name'],
                            "content": f"\n{persona['name']}: {final_message}\n\n"
                        }]
                    }

            # Check if the response contains Action:
            if "Action:" in content:
                # Extract the action
                action_match = re.search(r'Action:\s*(\w+)', content)
                if action_match:
                    tool_name = action_match.group(1)
                    debug(f"Executing tool: {tool_name}")

                    # Execute the tool
                    observation = execute_tool(tool_name)
                    debug(f"Observation: {observation}")
                    debug("")  # Empty line for readability

                    # Add observation to internal context
                    internal_context += f"\n{content}\n\nObservation: {observation}\n"
                    continue

            # If we get here without action or message, add to context and continue
            internal_context += f"\n{content}\n"

        except Exception as e:
            # Fallback response if LLM fails
            return {
                "messages": [{
                    "role": "assistant",
                    "name": persona['name'],
                    "content": f"{persona['name']}: Sorry ah, my mind a bit blur now..."
                }]
            }

    # If we exhausted iterations without getting a Message, provide default
    return {
        "messages": [{
            "role": "assistant",
            "name": persona['name'],
            "content": f"{persona['name']}: Well, that's interesting lah..."
        }]
    }
