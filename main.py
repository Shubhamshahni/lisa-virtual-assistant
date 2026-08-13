# from google import genai 
# client = genai.Client()

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



conversation = "The following is a conversation between a helpful assistant and a user.\n\n\n"

model_to_use=["gemini-3.5-flash","gemini-3.6-flash","gemini-3.5-flash-lite","gemini-2.5-pro"]


print(f"1:{model_to_use[0]}\n2:{model_to_use[1]}\n3:{model_to_use[2]}\n4:{model_to_use[3]}")


mo_no=int(input("\nSelect Gemini Model: "))
mo_no-=1
conversation+=f"{model_to_use[mo_no]}"

print(f"*************************************************************\nModel in Use:{model_to_use[mo_no]} to End Chat: exit,stop or quit\n")
print("Gemini: Hello! How can I help you today?\n")

while True:
    
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit","stop"}:
        print("Gemini: Goodbye!")
        break

    conversation += f"User: {user_input}\nAssistant:"

    response = client.models.generate_content(
        # model="gemini-3.5-flash",
        model=model_to_use[mo_no],
        contents=conversation,
    )

    assistant_text = response.text.strip()

    print(f"Gemini: {assistant_text}3\n")

    conversation += f" {assistant_text}\n"
