from langchain_core.tools import tool
'''
utilização do @tool para transformar funcoes em
ferramentas que o agente pode utilizar e chamar
'''

#exemple
@tool
def get_current_weather(location: str) -> str:
    """Get the current weather for a location.
    
    Use this when the user asks about weather conditions.
    
    Args:
        location: City name (e.g., "San Francisco", "New York")
    
    Returns:
        Weather description string
    """
    return f"The weather in {location} is sunny, 72°F"