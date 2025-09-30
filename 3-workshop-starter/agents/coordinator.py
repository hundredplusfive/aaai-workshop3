from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import debug


def coordinator(state):
    """
    Select next speaker based on conversation context.
    Manages volley control and updates state accordingly.

    Updates state with:
    - next_speaker: Selected agent ID or "human"
    - volley_msg_left: Decremented counter

    Returns: Updated state
    """

    debug(state)
    volley_left = state.get("volley_msg_left", 0)
    exit_count = state.get("exit_count", 0)

    debug(f"Volley messages left: {volley_left}", "COORDINATOR")
    debug(f"exit_count: {exit_count}", "COORDINATOR")

    if volley_left <= 0:
        debug("No volleys left, returning to human", "COORDINATOR")
        return {
            "next_speaker": "human",
            "volley_msg_left": 0
        }

    messages = state.get("messages", [])

    conversation_text = ""
    for msg in messages:
        # Messages are now always dicts
        conversation_text += f"{msg.get('content', '')}\n"

    system_prompt = """
    You are managing a lively conversation within a Travel Planning Committee.

    Available agents:
    - emily: Emily Tan, 32yo travel blogger, enthusiastic and budget-savvy, knows detailed cost breakdowns and activities.
    - mark: Mark Lim, 45yo ex-airline agent, professional and precise, specializes in flights, budgets, and weather.
    - sara: Sara Wong, 28yo adventurous budget traveler, casual and energetic, expert on activities and weather.

    Based on the conversation flow, select who should speak next to keep the planning session smooth and engaging.
    Consider:
    - Who hasn't spoken recently
    - Who has expertise relevant to the user’s current question (budget, activities, weather)
    - Which expertise (budget, activities, weather) is missing from conversation
    - Which agent’s personality best fits the tone and user’s preference
    - Emily specializes in budget and cost analysis
    - Mark specializes in weather and climate info
    - Sara specializes in activities and things to do
    
    Respond with ONLY the agent ID (emily, mark, or sara).
    """

    user_prompt = f"""Recent conversation:
    {conversation_text}

    Who should speak next to keep this conversation lively?"""

    debug("Analyzing conversation context...", "COORDINATOR")

    # Call LLM
    try:
        llm = ChatOpenAI(model="gpt-5-nano", temperature=1)

        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])

        # Extract speaker from response
        if isinstance(response.content, list):
            selected_speaker = " ".join(str(item) for item in response.content).strip().lower()
        else:
            selected_speaker = str(response.content).strip().lower()
        debug(f"LLM selected: {selected_speaker}", "COORDINATOR")

        # Validate speaker
        valid_speakers = ["emily", "mark", "sara"]
        if selected_speaker not in valid_speakers:
            # Fallback to round-robin if invalid
            import random
            selected_speaker = random.choice(valid_speakers)
            debug(f"Invalid speaker, fallback to: {selected_speaker}", "COORDINATOR")

    except Exception as e:
        # Fallback selection if LLM fails
        import random
        valid_speakers = ["emily", "mark", "sara"]
        selected_speaker = random.choice(valid_speakers)
        debug(f"LLM error, random selection: {selected_speaker}", "COORDINATOR")

    debug(f"Final selection: {selected_speaker} (volley {volley_left} -> {volley_left - 1})", "COORDINATOR")

    # Return only the updates (LangGraph will merge with existing state)
    return {
        "next_speaker": selected_speaker,
        "volley_msg_left": volley_left - 1
    }
