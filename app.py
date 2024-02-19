from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS  # Make sure you've installed flask-cors

app = Flask(__name__)
CORS(app)

# Assuming your OpenAI API key is set as an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


def fetch_course_details(query):
    # This is where you'd normally call the external courses API
    # For demonstration, let's assume a static response as before
    return {
        "courses": [
            {"name": "Introduction to AI", "university": "University A",
                "startDate": "2023-09-01"},
            {"name": "Data Science 101", "university": "University B",
                "startDate": "2023-10-15"},
        ]
    }


def generate_response_to_user_query(user_query):
    """
    Use OpenAI's GPT to generate a more context-aware response
    or query to fetch data using the mock `fetch_course_details` function.
    """
    gpt_response = openai.Completion.create(
        engine="text-davinci-003",  # You can select the appropriate model version
        prompt=f"Given a user query: '{user_query}', construct a professional response for a higher education AI consultant assistant.",
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return gpt_response.choices[0].text.strip()


@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    user_message = data.get('message')

    ai_response = generate_response_to_user_query(user_message)
    # For demonstration, we directly use this AI-generated response.
    # In a real scenario, this could be processed further or used to query the external API.

    return jsonify({"response": ai_response})


if __name__ == '__main__':
    app.run(debug=True)
