# Define a function to respond to user inputs
def chatbot(user):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user.lower()

    # Define some predefined rules and responses
    greetings = ["hello", "hi", "hey"]
    farewell = ["goodbye", "bye", "see you later"]
    questions = ["how are you?", "what's your name?", "what can you do?"]

    # Check if the user input matches any predefined rules
    if user in greetings:
        return "Hello! How can I assist you today?"
    
    elif user in farewell:
        return "Goodbye! Have a great day!"

    elif user in questions:
        return "Hi,I'm doing fine.My name is AI and I'm here to help you slove real-world problems"

    else:
        return "I'm sorry, I don't understand that. Please ask me something else."

# Main loop for chattinghi
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)