# If you encounter an error related to roles ("only assistant and user allowed") replace "role":system with "role":assistant.

import json
import urllib2

Basisprompt = "Generate a basic JSON containing only the following information on the person mentioned: dateofbirth, placeofbirth, dateofdeath, placeofdeath. Do not provide further information."

url = "http://localhost:1234/v1/chat/completions"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "messages": [
        {
            "content": Basisprompt,
            "role": "system"
        },
        {
            "content": value,  
            "role": "user"
        }
    ],
    "model": "openchat-3.5-7b",
    "stream": False,
    "max_tokens": 2048,
    "stop": [
        "hello"
    ],
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}

data_string = json.dumps(data)  # Convert dictionary to JSON string
data_bytes = data_string.encode('utf-8')  # Encode to bytes

req = urllib2.Request(url, data=data_bytes, headers=headers)

response = urllib2.urlopen(req)
response_bytes = response.read()
response_json = json.loads(response_bytes.decode('utf-8'))
content = response_json["choices"][0]["message"]["content"]
content = content.replace("<|end_of_turn|>", "")
return content
