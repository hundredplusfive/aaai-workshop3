from typing import TypedDict, Optional


class State(TypedDict):
    """
    Overall state of the entire LangGraph system.
    """
    
    # TODO: Define state
    messages: list
    volley_msg_left: int
    next_speaker: Optional[str]
    exit_count: int