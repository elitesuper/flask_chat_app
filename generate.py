import openai
import re


openai.api_key = "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"

def generate_message(prompt):

    message = "please answer of user's message but you have to don't message to users about IT or development tell to user about your apologize\n" + prompt

    response = openai.Completion.create( 
        engine="text-davinci-002", 
        prompt = message, 
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5,)
    
    output = response.choices[0].text
    output = re.sub('[^a-zA-Z0-9\n\.\?\!]+', ' ', output)

    return output.strip()