from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

myModel = ChatOpenAI(
    model="gpt-4o",
    # api_key="your-api-key",
    # max_tokens=150

)


myResult = myModel.invoke("Hello, how are you?  who i am ?")
print(myResult.content)