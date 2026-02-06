
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "hello world"
if __name__ == '__main__':
    app.run(debug=True)

'''from ai import get_ai_response 

print("welcome to the AI chatbot!")
print("type exit to quit.\n")
    
while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
       
        
        response = get_ai_response(user_input)
        print(f"AI: {response}")'''