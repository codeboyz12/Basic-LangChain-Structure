from src.chain.basic_chain import basic_chain

def chat(message):
    chain = basic_chain()
    response = chain.invoke({"message": message})
    return response.content

def main():
    print("Ready for conversation!")
    for i in range(5):
        message = input("User message: ")
        reply = chat(message)
        print(f"Gemini: {reply}")

if __name__ == "__main__":
    main()