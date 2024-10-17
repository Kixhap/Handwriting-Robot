from openai import OpenAI
import os
from dotenv import load_dotenv
import re

# Define the regex pattern to allow only specified characters
# The regex will match any character in the set defined within the square brackets
reg = r"[9Df;'6FNeT?hYoE-LnP8j7)Hp v4kCUsyuGVcK!Jir2dlxzbb1.Aa#IWw5gM3mq:RBS]"

# Load environment variables from .env file
load_dotenv()

def get_openai_response(question):
    # Initialize the OpenAI client with the given base URL and API key
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.environ.get("KEY")
    )

    # Create the completion request
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role": "user", "content": question}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    # Collect the response
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            # Print the chunk content as it arrives (optional)
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content

    # Use regex to filter the response, keeping only characters defined in 'reg'
    response = ''.join(re.findall(reg, response))

    return response
