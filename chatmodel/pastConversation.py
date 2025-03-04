from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

myModel = ChatOpenAI(
    model="gpt-4o",
    # api_key="your-api-key",
)



messages = [

  SystemMessage("You are expert in python programming  since 2019"),
  HumanMessage("Hello, how are you? tell me about myself"), 
]



result = myModel.invoke(messages) 

print(result.content)