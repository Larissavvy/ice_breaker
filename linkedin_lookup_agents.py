import os
from dotenv import load_dotenv
import requests

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
#from langchain_ollama import ChatOllama
from tools import get_profile_url_tavily

load_dotenv()

def lookup(name : str) -> str:
    
    llm = ChatOpenAI(temperature= 0,model= "gpt-3.5-turbo")
    #llm = ChatOllama(model= "llama3")

    prompt_statement = """Given the full name {name_of_person} of the person, I want to get a link to their LinkedIn profile page \
                        Your answer should contain only the URL"""
    
    prompt_temp = PromptTemplate(template= prompt_statement, input_variables= ['name_of_person'])

    tools_for_agent = [
        Tool(name= "crawl google 4 linkedin profile page",
             func= get_profile_url_tavily,
             description= "useful for when you need to get the LinkedIn Page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm= llm,tools=tools_for_agent,prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)

    result = agent_executor.invoke(
        input= {"input": prompt_temp.format_prompt(name_of_person = name)}
    )

    linkedin_url = result['output']
    return linkedin_url



# if __name__ == "__main__":
#     linked_in_url = lookup(name= "Larissa Pereira Morgan Stanley Mumbai")
#     print(linked_in_url)