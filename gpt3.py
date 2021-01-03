import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


## thanks to https://www.twilio.com/blog/ultimate-guide-openai-gpt-3-language-model
## for the chatbot code, saved me some time!
## tweaked to add raw response and default values, and TODO: configs from file

def gpt3(prompt, engine='davinci', response_length=99,
         temperature=0.8, top_p=.5, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    #new_prompt = prompt
    return response, answer, new_prompt