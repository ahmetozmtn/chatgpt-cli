import openai
import json

api_key = open("API_KEY.txt", "r").read()
openai.api_key = api_key

chat_log = []

while True:
    user_msg = input(">>>")
    if user_msg.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_msg})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )
        result = json.dumps(response, ensure_ascii=False, indent=2)
        result_dict = json.loads(result)
        assistant_response = result_dict['choices'][0]['message']['content']
        print("ChatGPT:", assistant_response.strip("\n").strip())
        chat_log.append({"role":"assistant","content":assistant_response.strip("\n").strip()})
