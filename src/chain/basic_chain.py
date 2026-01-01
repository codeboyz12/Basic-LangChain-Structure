from src.llm.gemini import gemini
from src.prompt.prompt_template import prompt_stateless_template
from langchain_core.runnables import Runnable

def basic_chain() -> Runnable:
    llm = gemini()
    prompt = prompt_stateless_template()

    return prompt | llm