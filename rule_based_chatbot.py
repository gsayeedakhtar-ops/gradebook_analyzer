def ai_agent(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return"Hello ! I am your AI Agent. How can I help you today?"
    elif "weather" in user_input:
        return"I cant't check live weather. Let's assume it's sunny today!"
    elif "study" in user_input or "learn" in user_input:
        return"Great choice ! Consistency is the key to mastering coding"
    elif "joke" in user_input:
        return"Why do programmers dont like nature? Too many bugs"
    elif "motivation" in user_input:
        return"Keep pushing yourself forward ! Every line of code makes you stronger"
    elif "math" in user_input:
        equation = input("Enter a math equation(e.g., 2+4*8): ")
        try:
           result = eval(equation)
           return f"The result of {equation} is {result}"
        except Exception as e:
            return" Sorry ! I couldn't solve that, Error:{e}"
        
    elif "bye":
        return"Goodbye! Stay motivated"
    else:
       return"I'm not sure how to respond to that. Can you rephrase?"
def main():
    print("AI Agent (type 'bye' to exit)")
    with open("chat_history.txt", "a") as log:
        while True:
            
         user_input = input("You: ")
         response = ai_agent(user_input)
         print("Agent:", response)

         log.write(f"You: {user_input}\n")
         log.write(f"Agent: {user_input}\n\n")
         if "bye" in user_input.lower():
            break
if __name__ == "__main__":
     main()
