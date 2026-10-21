from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools import get_current_weather
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, StateGraph
from state import AgentState
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
#creating tools
tools = [get_current_weather]

#stick togher the llm and the tools
llm_with_tools = llm.bind_tools(tools)

#creating a prompt template
system_prompt = """You are a helpful assistant that can provide weather information.
Your capabilities include:
- Answering questions about the current weather in various locations.

Guidelines:
- Be concise and clear in your responses.
- If you don't know the answer, admit it rather than making up information.
- Always use the `get_current_weather` tool when asked about weather information in an specific location.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages"),
])

async def call_agent(state: AgentState):
    """
    The agent node calls the LLM to decide the next action.
    
    The LLM can:
    1. Call one or more tools
    2. Generate a text response
    3. Both
    """
    messages = state["messages"]

    formatted = prompt.format_prompt(messages=messages)

    #call the llm with the tools
    response = await llm_with_tools.ainvoke(formatted)

    return {"messages": [response]}


tool_node = ToolNode(tools)

def should_continue(state: AgentState):
    """
    Router function that determines the next step.
    
    Returns:
        "tools" - if the LLM wants to use tools
        END - if the LLM is done (just text response)
    """
    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END

workflow = StateGraph(AgentState)

#add nodes
workflow.add_node("agent", call_agent)
workflow.add_node("tools", tool_node)

workflow.set_entry_point("agent")

#add conditional edge from agent
workflow.add_conditional_edges(
    "agent", 
    should_continue, 
    {
        "tools": "tools",
        END: END
    }
)


workflow.add_edge("tools", "agent")
agent = workflow.compile()