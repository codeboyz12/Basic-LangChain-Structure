from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system_prompt = """
         คุณคือ chat model ที่ทำงานบน terminal เพื่อตอบคำถามทั่วไปให้ผู้ใช้ 
         คุณตอบคำถามสั้น กระชับ ได้ใจความ ด้วยทำนองที่เป็นมิตร 
         คุณทำงนบน terminal ดั่งนั้นจึงไม่ใช้อิโมจิหรือข้อความพิเศษใดๆในการสื่อสาร
         """

def prompt_stateful_template() -> ChatPromptTemplate:
    return ChatPromptTemplate([
        ("system", system_prompt),
         MessagesPlaceholder(variable_name="message_history"),
         ("human", "{input}")
    ])

def prompt_stateless_template() -> ChatPromptTemplate:
    return ChatPromptTemplate([
        ("system", system_prompt),
         ("human", "{input}")
    ])