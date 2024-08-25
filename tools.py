from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_profile_url_tavily(name:str):
    "Searches Linkedin or Twitter Profile Page"

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]['url']