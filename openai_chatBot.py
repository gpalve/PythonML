import os
import openai
# Load your API key from an environment variable or secret management service
openai.api_key = "Your api key here"
print("What's on your mind?Just ask bot...type exit to get out of loop\n")
while True:
    q=input("Question: ")
    if q == "exit":
        break
    response = openai.Completion.create(model="text-davinci-003", prompt=q, temperature=0, max_tokens=1000)
    bot_response = response["choices"][0]["text"]
    print("Bot: " +bot_response[2:],"\n")
    print("=========================================================================================================\n")