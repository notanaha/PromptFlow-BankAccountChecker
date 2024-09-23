from promptflow import tool
import json
import requests
from bs4 import BeautifulSoup


def browse_wesite(url):  
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    out_text = ''
    title_text = soup.find('title').get_text()
    out_text += title_text + '\n'

    # Show H1 to H3
    for level in range(1, 4):
        headers = soup.find_all(f'h{level}')
        for header in headers:
            header_text = header.get_text()
            out_text += f'H{level}: {header_text}\n'
    return out_text



def check_distance(zip1, zip2):
    # This is a dummy function to check the distance between two zip codes
    print('check_distance was called with zip codes', zip1, zip2)
    distance = "200(KM)"
    return distance


@tool
def run_function(response_message: dict) -> str:
    function_call = response_message.get("function_call", None)
    if function_call and "name" in function_call and "arguments" in function_call:
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        print(function_args)
        result = globals()[function_name](**function_args)
    else:
        print("No function call")
        '''if isinstance(response_message, dict):
            result = response_message.get("content", "")
        else:
            result = response_message'''
        result="Function was not called."
    return result
