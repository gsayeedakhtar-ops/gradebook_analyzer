def chatbot():
    print("AI Agent (type 'bye' to exit)")
    history_file = "chat_history.txt"

    # --- Load history at startup ---
    try:
        with open(history_file, "r") as f:
            history = f.readlines()
            if history:
                print("📖 I remember our last chat:")
                for line in history[-4:]:   # show last 4 lines only
                    print(line.strip())
    except FileNotFoundError:
        print("🆕 Starting fresh. No history yet.")

    # --- Chat Loop ---
    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Agent: Goodbye! I'll remember our chat next time.")
            break

        # Generate response
        if "hello" in user_input.lower():
            response = "Hello again! I’m your AI Agent."
        elif "learn" in user_input.lower():
            response = "Great choice! Consistency is the key to mastering coding."
        else:
            response = "I'm not sure about that, but I’ll remember it."

        print("Agent:", response)

        # Save new conversation
        with open(history_file, "a") as f:
            f.write(f"You: {user_input}\n")
            f.write(f"Agent: {response}\n")
