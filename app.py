from src.searcher import search_collection
from src.extractor import extractor
from src.parser import parser
from config import TEMPERATURE
from config import GROQ_API_KEY
from config import MODEL_NAME
from flask import Flask, request, jsonify, render_template
from langchain_groq import ChatGroq
import random
import json

app = Flask(__name__, static_folder = 'static', template_folder = 'templates')

llm = ChatGroq(temperature  = TEMPERATURE , 
               groq_api_key = GROQ_API_KEY, 
               model_name   = MODEL_NAME)

@app.route('/')
def home():
    return render_template('index_home.html')

@app.route('/chatbot')
def chatbot():
    return render_template('index.html')
@app.route('/search', methods=['POST'])
def search():
    try:
        # Get the query from the request
        data = request.json
        conversation_history = data.get('query', '')

        # Extract and parse the query
        extracted_response = extractor(llm, conversation_history)
        parsed_data = parser(extracted_response)

        # Check if we have enough information to proceed
        if parsed_data["MOVE_ON"]:
            # Search the collection with extracted attributes
            results = search_collection(
                colour=parsed_data["colour"],
                individual_category=parsed_data["Individual_category"],
                category=parsed_data["Category"],
                category_by_gender=parsed_data["category_by_Gender"]
            )
            return jsonify({"results": results, "message": "Search results for your query"})
        else:
            
            return jsonify({"results": [], "message": parsed_data["FOLLOW_UP_MESSAGE"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
