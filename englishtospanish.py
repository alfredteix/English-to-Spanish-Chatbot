import requests

API_Key = "99bb21507ae4c2fe3ae8a8c4ab11aa572ca93e3fcdf62282793913286d0f864e"
TOGETHER_AI = "https://api.together.xyz/v1/chat/completions"


def translate_text(text, source_lang="English", target_lang="Spanish"):
    headers = {
        "Authorization": f"Bearer {API_Key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": f"Translate the following text from {source_lang} to {target_lang}: {text}"}],
        "temperature": 0.7
    }

    response = requests.post(TOGETHER_AI, json=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        return f"Error: {response.status_code}, {response.text}"


print("\nNeed to translate English to Spanish? Type 'exit' to quit.") #Prints welcome user message

while True:
    user = input("\nPlease type your message here: ") # Takes user input to translate English to Spanish

    if user.lower() == "exit": # exits while loop and breaks program
        print("Goodbye!")
        break

    response = translate_text(user, "English", "Spanish")
    print("\nAI Response:", response)
