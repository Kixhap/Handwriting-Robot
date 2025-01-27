from openai import OpenAI
import os
from dotenv import load_dotenv

reg = r"9Gn()T'p,ymRB0MLY#18si?-Du:b2AqeJ5g9!PatHoFcO.h6NIkd3 V 74rjlKWzESCU;xwvf"

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
        messages=[{"role": "user", "content": question+" opisz to krotko prosze"}],
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

    replacement_map = {
        "Z": "z", "Ż": "z", "Ź": "z", "ź": "z", "ż": "z",
        "Ś": "s", "ś": "s",
        "ł": "l", "Ł": "l",
        "ć": "c", "Ć": "c",
        "ą": "a", "Ą": "a",
        "ę": "e", "Ę": "e",
        "ń": "n", "Ń": "n",
        "ó": "o", "Ó": "o"
    }
    result = "".join(replacement_map.get(char, char) for char in response)
    response = "".join(char for char in result if char in reg)

    return response




