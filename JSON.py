import json
from difflib import get_close_matches

# Function to load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Function to find the best match for a user question
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Function to get an answer for a question from the knowledge base
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

# Main function to run the chatbot
def chatbot():
    # Load the knowledge base
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Exit condition
        if user_input.lower() == 'quit':
            print("Chatbot session ended.")
            break
        
        # Find the best match from the knowledge base
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            # Get the answer for the matched question
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input("You: (Type the answer or 'skip' to skip) ").strip()
            
            if new_answer.lower() != 'skip':
                # Add the new question and answer to the knowledge base
                knowledge_base["questions"].append({
                    "question": user_input,
                    "answer": new_answer
                })
                # Save the updated knowledge base
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I learned a new response.")

# Run the chatbot if this script is executed directly
if __name__ == '__main__':
    chatbot()
