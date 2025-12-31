from src.chat.chat_stateful import chat_stateful

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