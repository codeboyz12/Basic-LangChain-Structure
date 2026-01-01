from src.llm.gemini import gemini
from src.prompt.prompt_template import prompt_stateful_template
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

def get_message_history(sessionId: str) -> BaseChatMessageHistory:
    if sessionId not in store:
        store[sessionId] = InMemoryChatMessageHistory()
    return store[sessionId]

def stateful_chain() -> RunnableWithMessageHistory:
    llm = gemini()
    prompt = prompt_stateful_template()

    chain =  prompt | llm

    return RunnableWithMessageHistory(
        chain,
        get_message_history,
        input_messages_key="input",
        history_messages_key="message_history"
    )