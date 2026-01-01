from src.chain.basic_chain import basic_chain

basic_chain = basic_chain()

def chat_stateless(message: str) -> str:
    response = basic_chain.invoke({"input": message})
    return response.content