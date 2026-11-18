from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """
    This is what flows through your agent.
    
    Messages is a list that keeps growing:
    - User questions
    - Agent responses
    - Tool results
    """

    messages: Annotated[Sequence[BaseMessage], add_messages]