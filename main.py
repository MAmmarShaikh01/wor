import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
    name="Smart Student",
    instructions="yau are a smart student who will Answer academic questions , Provide study tips and Summarize small text passages",
    model=model
)

result = Runner.run_sync(agent,"hello who are you and what is my name (my name is ammar)")
print(result.final_output)