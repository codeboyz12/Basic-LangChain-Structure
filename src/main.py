from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7
    )

    # 2. สร้างคำถาม
    message = HumanMessage(content="ช่วยอธิบายความเจ๋งของ LangChain ใน 3 ข้อสั้นๆ")

    # 3. เรียกใช้งานและแสดงผล
    print("--- กำลังถาม Gemini ---")
    response = llm.invoke([message])
    print(response.content)

if __name__ == "__main__":
    main()