import asyncio
from agents import  Agent, Runner, OpenAIChatCompletionsModel
from typing import List
from openai import AsyncOpenAI 
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI 
from prompts import instructions


load_dotenv(override=True)

api_key = os.getenv('API_KEY1')
base_url = os.getenv('BASE_URL')

print(f"API_KEY: {api_key}")
print(f"BASE_URL: {base_url}")

client = AsyncOpenAI(base_url=base_url, api_key=api_key)

model= OpenAIChatCompletionsModel(
                    model="openai.o4-mini",
                    openai_client=client
                )  

summarizer_agent = Agent(
        name="summarizer_agent",
        instructions=instructions,
        model=model
)

def summarize_medical_record(medical_record: str) -> str:
    result = asyncio.run(Runner.run(summarizer_agent, medical_record))
    return result.final_output



