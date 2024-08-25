from dotenv import load_dotenv
import os

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import chains
from langchain_core.output_parsers import StrOutputParser

from linkedin_data import scrape_linkin_data
from linkedin_lookup_agents import lookup


def ice_break_with(name:str):
    linked_in_user_name = lookup(name = name)
    linked_in_data = scrape_linkin_data(profile_url=linked_in_user_name,test = True)

    summary_templete = """
            given the Linkedin information {information} about a person I want to create
            1. a short summary
            2. Major skills in the profile
                          
        """
    
    summary_prompy_templete = PromptTemplate(input_variables=['information'],template=summary_templete)

    llm = ChatOpenAI(temperature= 0.6,model= "gpt-3.5-turbo")

    chain = summary_prompy_templete | llm | StrOutputParser()

    information = scrape_linkin_data(profile_url = 'https://in.linkedin.com/in/larissa0702')

    res = chain.invoke(input={'information':information})

    print(res)

if __name__ == "__main__":
    load_dotenv()
    print('Ice Breaker')
    ice_break_with(name = 'Larissa Pereira Morgan Stanley Mumbai')
    
    
    
    


#llm = ChatOllama(model= "llama3")




