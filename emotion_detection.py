import requests

def emotion_detector(text_to_analyze):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id/v1/analyze"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    params = {
        "version": "2021-08-01"
    }
    
    json_data = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }
    
    response = requests.post(url, headers=headers, params=params, json=json_data, auth=("apikey", "your-api-key"))
    
    if response.status_code == 200:
        data = response.json()
        emotions = data["emotion"]["document"]["emotion"]
        return emotions
    else:
        return None
