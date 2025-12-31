from src.chain.basic_chain import basic_chain
from src.chain.stateful_chain import stateful_chain

basic_chain = basic_chain()
stateful_chain = stateful_chain()

def chat_stateless(message: str):
    response = basic_chain.invoke({"input": message})
    return response.content

def chat_stateful(message: str, session: str = "session_01"):
    config = {
        "configurable": {
            "session_id": session
        }
    }
    response = stateful_chain.invoke({"input": message}, config=config)
    return response.content

def main():
    print("Ready for conversation! (Type 'exit' to quit)")
    while True:
        message = input("User message: ")
        if message.lower() == 'exit':
            break
            
        reply = chat_stateful(message)
        print(f"Gemini: {reply}")

if __name__ == "__main__":
    main()