from src.chain.stateful_chain import stateful_chain

stateful_chain = stateful_chain()

def chat_stateful(
        message: str, 
        session: str = "session_01"
    ) -> str:
    
    config = {
        "configurable": {
            "session_id": session
        }
    }

    response = stateful_chain.invoke({"input": message}, config=config)

    return response.content