from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
from langchain.messages import HumanMessage , AIMessage , SystemMessage

llm = ChatOpenAI(
    model = "gpt-4.1-mini"
)
messages = []
while True:
    user_prompt = input("You : ")
    if user_prompt == "0":
        break
    messages.append(HumanMessage(content=user_prompt))
    response = llm.invoke(messages)
    
    messages.append(response)
    result = response.content
    
    print("AI : " , result)
