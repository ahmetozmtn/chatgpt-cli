import os, json, openai
from dotenv import load_dotenv

def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model = "gpt-3.5-turbo"
    chat_log = []

    while True:
        user_msg = input(">>> ")
        if user_msg.lower() == "quit":
            logOut("Quit...")
        else:
            chat_log.append({"role": "user", "content": user_msg})
            response = openai.ChatCompletion.create(
                model=model, messages=chat_log
            )
            result = json.dumps(response, ensure_ascii=False, indent=2)
            result_dict = json.loads(result)
            assistant_response = result_dict["choices"][0]["message"]["content"]
            print("ChatGPT:", assistant_response.strip("\n").strip())
            chat_log.append(
                {
                    "role": "assistant", 
                    "content": assistant_response.strip("\n").strip()
                }
            )


def logOut(text):
    print(f"\n{text}\n")
    exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logOut("Quit...")
