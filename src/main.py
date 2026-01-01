import os
from src.chat.chat_stateful import chat_stateful

def main() -> None:
    print("Ready for conversation! (Type 'exit' to quit)")
    while True:
        message = input("User message: ")
        if message.lower() == 'exit':
            break
            
        reply = chat_stateful(message)
        print(f"Gemini: {reply}")

if __name__ == "__main__":
    if os.getenv("GOOGLE_API_KEY") is None:
        print("GOOGLE API KEY not found")
    else:
        print("GOOGLE API KEY INITIALIZE")
        main()