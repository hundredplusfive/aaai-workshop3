from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

from state import State
from agents import coordinator
from nodes import (
    human_node,
    check_exit_condition,
    coordinator_routing,
    participant_node,
    summarizer_node
)


load_dotenv(override=True)  # Override, so it would use your local .env file




def build_graph():
    """
    Build the LangGraph workflow.
    """

    builder = StateGraph(State)

    # TODO: Connect the graph
    builder.add_node("human", human_node)
    builder.add_node("coordinator", coordinator)
    builder.add_node("participant", participant_node)
    builder.add_node("summarizer", summarizer_node)

    builder.add_edge(START, "human")
    builder.add_conditional_edges("human", check_exit_condition, {"summarizer": "summarizer", "coordinator": "coordinator"})
    builder.add_conditional_edges("coordinator", coordinator_routing, {"participant": "participant", "human": "human"})

    builder.add_edge("participant", "coordinator")
    builder.add_edge("summarizer", END)

    return builder.compile()


def main():
    print("=== TRAVEL PLANNING COMMITTEE CHAT ===")
    print("Plan your next trip with our expert travel agents! Type 'exit' to end.\n")
    print("Setting: A lively travel planning session with a team of passionate travel advisors...")
    print("Meet Emily, the budget-savvy travel blogger,")
    print("Mark, the detail-focused ex-airline agent,")
    print("and Sara, the adventurous explorer sharing hidden gems.\n")

    graph = build_graph()

    print(graph.get_graph().draw_ascii())

    initial_state = State(
        messages=[],
        volley_msg_left=0,
        next_speaker=None
    )

    try:
        graph.invoke(initial_state)
    except KeyboardInterrupt:
        print("\n\nConversation interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Ending conversation...")


if __name__ == "__main__":
    main()
