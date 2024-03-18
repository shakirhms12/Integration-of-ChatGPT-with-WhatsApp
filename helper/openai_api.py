import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = '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'

def text_complition(prompt: str) -> dict:
    
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=500,  #150
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
        