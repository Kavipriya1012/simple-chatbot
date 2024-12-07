import time

def greet_user():
    print("Hello! I'm your friendly chatbot.")
    print("How can I help you today?")

def tell_time():
    current_time = time.strftime("%I:%M %p")
    return f"The current time is {current_time}"

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I'm Chatbot, nice to meet you!"
    elif "time" in user_input:
        return tell_time()
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that. Can you ask something else?"


def main():
    greet_user()

    while True:
        user_input = input("\nYou: ")


        if "goodbye" in user_input.lower() or "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break


        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
