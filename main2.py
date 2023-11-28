from time import sleep
from flask import Flask, request, jsonify
import openai
from openai import OpenAI
import functions

app = Flask(__name__)

# Init client
import constants
OPENAI_API_KEY = constants.APIKEY
# Init client
client = OpenAI(
    api_key=OPENAI_API_KEY)  # should use env variable OPENAI_API_KEY in secrets (bottom left corner)
# Define the assistant ID
# assistant_id = 'asst_C0D0oLlyhovnQJtflH7msNvp'

# Create new assistant or load existing
assistant_id = functions.create_assistant(client)

# Define the question string
question = "What is the name of my chicken?"

# Start conversation thread
thread = client.beta.threads.create()

# Create a list of messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}
]

# Add the user's message to the thread
response = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="system",
    content="You are a helpful assistant."
)

response = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=question
)

# Generate response
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    thread_id = data.get('thread_id')
    user_input = data.get('message', '')

    if not thread_id:
        print("Error: Missing thread_id")  # Debugging line
        return jsonify({"error": "Missing thread_id"}), 400

    print(f"Received message: {user_input} for thread ID: {thread_id}")  # Debugging line

    # Add the user's message to the thread
    client.beta.threads.messages.create(thread_id=thread_id,
                                        role="user",
                                        content=user_input)

    # Run the Assistant
    run = client.beta.threads.runs.create(thread_id=thread_id,
                                          assistant_id=assistant_id)

    # Wait for the Run to complete
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        print(f"Run status: {run_status.status}")
        if run_status.status == 'completed':
            break
        sleep(1)  # Wait for a second before checking again

    # Retrieve and return the latest message from the assistant
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[-1].content[0].text.value  # Use the latest message

    print(f"Assistant response: {response}")  # Debugging line
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
