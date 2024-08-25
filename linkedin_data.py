from dotenv import load_dotenv
import os
import requests

load_dotenv()


def scrape_linkin_data(profile_url, test = True):
    """Scrape Information from LinkedIn profile
    Manually Scrape information from LinkedIn profile"""

    if test:
        profile_url = "https://gist.githubusercontent.com/Larissavvy/eb2ac03178763fac7aef099db22b2b58/raw/9ca49111ca9c0bb191b397e98391a31e8f5b8250/larissa_pereira.json"
        response = requests.get(profile_url,timeout= 10 )


    else:
        print('No Data Found // API key cost a lot')
        print('update the GIST')


    data = response.json()

    data = {
        k : v
        for k,v in data.items()
        if v not in ([], "", "","None",None)
        and k not in ['people_also_viewed','certifications']
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop('profile_pic_url')

    return data