import requests 
import os 
import json 

def content_moderation_request(input):
    moderation_url = "https://api.openai.com/v1/moderations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }
    data = json.dumps({"input": input})
    r = requests.post(moderation_url, headers=headers, data=data)
    return r.json() 


if __name__ == "__main__":
    out = content_moderation_request("I like broccoli.")
    print(out)
