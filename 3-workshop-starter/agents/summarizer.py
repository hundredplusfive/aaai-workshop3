from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def summarizer(state) -> str:
    """
    Generate summary report using LLM when conversation ends.

    Args:
        state: Current conversation state with messages

    Returns:
        Formatted summary string
    """
    messages = state.get("messages", [])

    if not messages:
        return "No conversation to summarize."

    # Extract conversation text
    conversation_text = ""
    for msg in messages:
        # Messages are now always dicts
        conversation_text += f"{msg.get('content', '')}\n"

    if not conversation_text.strip():
        return "No conversation content to summarize."

    # System prompt for summarization
    system_prompt = """You are an attentive observer listening to a Travel Planning Committee discussion about organizing trips based on user preferences and budget.

    Generate a concise summary of the conversation that captures:
    1. Key travel destinations, budgets, and activities discussed
    2. The roles and contributions of each travel agent involved
    3. Any important recommendations or user preferences highlighted
    4. The overall tone and flow of the planning session

    Format your summary clearly and engagingly to reflect the collaborative and helpful nature of the committee.
    Keep it concise yet informative.
    """

    user_prompt = f"""Here's the conversation that took place:

{conversation_text}

Please provide a summary of this conversation."""

    try:
        # Call LLM
        llm = ChatOpenAI(model="gpt-5-nano", temperature=1)

        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])

        if isinstance(response.content, list):
            summary = " ".join(str(item) for item in response.content).strip()
        else:
            summary = str(response.content).strip()

        # Format with header
        return f"=== TRAVEL PLANNING CONVERSATION SUMMARY ===\n\n{summary}"

    except Exception as e:
        # Fallback to basic summary if LLM fails
        return f"""=== TRAVEL PLANNING CONVERSATION SUMMARY ===

Total messages: {len(messages)}

Unable to generate detailed summary at this time.
The conversation has been logged for review."""
