import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "deepseek/DeepSeek-V3-0324"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage("You are a helpful assistant. Respond in Kanglish (Kannada + English)."),
]

print("Chatbot initialized! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    if not user_input:
        continue
    
    messages.append(UserMessage(user_input))
    
    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=100,
        model="gpt-4o-mini"
    )
    
    assistant_message = response.choices[0].message.content
    print(f"Assistant: {assistant_message}\n")
    
    messages.append(AssistantMessage(assistant_message))

