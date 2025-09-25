
import json
import re
from collections import Counter
import random

class VirtualAssistant:
    def __init__(self, intents_file):
        with open(intents_file, 'r') as f:
            self.intents_data = json.load(f)
        self.intents = self.intents_data['intents']
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.split()
    
    def find_intent(self, user_input):
        user_words = set(self.clean_text(user_input))
        best_match = None
        best_score = 0
        
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_words = set(self.clean_text(pattern))
                
                common_words = user_words.intersection(pattern_words)
                if len(pattern_words) > 0:
                    score = len(common_words) / len(pattern_words)
                    
                    if score > best_score and score > 0.3:
                        best_score = score
                        best_match = intent
        
        return best_match
    
    def get_response_from_json(self, intent_tag):
        """Helper function to get response from JSON by intent tag"""
        for intent in self.intents:
            if intent['tag'] == intent_tag and intent['responses']:
                return random.choice(intent['responses'])
        return None
    
    def get_response(self, user_input):
        intent = self.find_intent(user_input)
        
        if intent:
            # Check if we have custom functions for specific intents that need special handling
            if intent['tag'] in custom_responses:
                return custom_responses[intent['tag']](self)
            # Use responses from JSON file
            elif intent['responses']:
                return random.choice(intent['responses'])
        
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Custom functions that read from JSON and add special behavior
def goodbye(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('goodbye')
    if response:
        print("Assistant:", response)
    else:
        print("Assistant: Goodbye! Safe travels!")
    exit()

def book_flight(assistant_instance):
    # Get response from JSON
    json_response = assistant_instance.get_response_from_json('book_flight')
    if not json_response:
        json_response = "I can help you book a flight."
    
    # Add interactive elements
    flights = ['Delta', 'Cathay Pacific', 'Dutch Airlines', 'Emirates', 'Qatar Airways']
    destinations = ['New York', 'London', 'Tokyo', 'Dubai', 'Sydney']
    
    return f"{json_response} Available airlines: {', '.join(flights)}. Available destinations: {', '.join(destinations)}."

def weather(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('weather')
    return response if response else "Please tell me your location so I can check the weather."

def joke(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('joke')
    return response if response else "Why don't airplanes ever get tired? Because they always have a good altitude! ✈️"

def conversation_advanced(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('conversation_advanced')
    return response if response else "That's an interesting topic! I'm specialized in flight bookings, but I'd be happy to help you with any travel-related questions."

def greeting(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('greeting')
    return response if response else "Hello! How can I help you today?"

def thanks(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('thanks')
    return response if response else "You're welcome!"

def name_query(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('name_query')
    return response if response else "I'm your AI virtual assistant."

def available_flights(assistant_instance):
    # Get response from JSON
    response = assistant_instance.get_response_from_json('available_flights')
    return response if response else "Available airlines: Delta, Cathay Pacific, Dutch Airlines, Emirates, Qatar Airways"

# Map all intents to functions that read from JSON
custom_responses = {
    'greeting': greeting,
    'goodbye': goodbye,
    'thanks': thanks,
    'name_query': name_query,
    'book_flight': book_flight,
    'available_flights': available_flights,
    'weather': weather,
    'joke': joke,
    'conversation_advanced': conversation_advanced
}

# Create assistant
assistant = VirtualAssistant('intents.json')

print("Virtual Assistant is ready!")
print("Type 'quit' to exit")
print("-" * 40)

# Main conversation loop
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['quit', 'exit']:
        print("Assistant: Goodbye! Have a great day!")
        break
    
    response = assistant.get_response(user_input)
    print("Assistant:", response)
