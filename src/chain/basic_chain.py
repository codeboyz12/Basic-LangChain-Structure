from src.llm.gemini import gemini
from src.prompt.prompt_template import prompt_stateless_template

def basic_chain():
    llm = gemini()
    prompt = prompt_stateless_template()

    return prompt | llm