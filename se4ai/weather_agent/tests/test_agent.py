import asyncio
from langchain_core.messages import HumanMessage
from agent import agent

async def main():
    result = await agent.ainvoke({
        "messages": [
            HumanMessage(content="Olá! Quem é você?")
        ]
    })

    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
