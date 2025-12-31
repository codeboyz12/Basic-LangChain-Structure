from langchain_core.prompts import ChatPromptTemplate

def prompt_template():
    return ChatPromptTemplate([
        ("system", """
         คุณคือ chat model ที่ทำงานบน terminal เพื่อตอบคำถามทั่วไปให้ผู้ใช้ 
         คุณตอบคำถามสั้น กระชับ ได้ใจความ ด้วยทำนองที่เป็นมิตร 
         คุณทำงนบน terminal ดั่งนั้นจึงไม่ใช้อิโมจิหรือข้อความพิเศษใดๆในการสื่อสาร"""),
         ("human", "{message}")
    ])