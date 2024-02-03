class Chatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day."

    def remember_context(self, key, value):
        self.context[key] = value

    def respond_to_question(self, question):
        responses = {
            "How are you?": "I'm just a chatbot, so I don't have feelings, but thanks for asking!",
            "What's the weather like today?": "I'm not sure about the current weather. You might want to check a weather website.",
            "Can you help me with something?": "Of course! Just let me know what you need assistance with.",
            "What time is it?": "I don't have access to real-time data, so I can't tell you the current time.",
            "Tell me a joke.": "Sure! Why don't scientists trust atoms? Because they make up everything!",
        }
        return responses.get(question, "I'm sorry, I don't understand that question.")

    def handle_user_interaction(self):
        questions = ["What's your name?", "Where are you from?", "What are your hobbies?"]
        for question in questions:
            user_input = input(question + " ")
            self.remember_context(question, user_input)
            print("Great! Thanks for sharing.")

    def start_conversation(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print(self.farewell())
                break
            elif user_input in self.context:
                print("You already told me about that! You said:", self.context[user_input])
            else:
                response = self.respond_to_question(user_input)
                print("Chatbot:", response)


if __name__ == "__main__":
    bot = Chatbot()
    bot.handle_user_interaction()
    bot.start_conversation()
