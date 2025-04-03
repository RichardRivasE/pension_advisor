from flask import Flask, render_template, request, jsonify
from main import ChatbotAssistant, get_stocks

app = Flask(__name__)

# Initialize the chatbot assistant and load the pre-trained model
assistant = ChatbotAssistant('fin_intents.json', function_mappings={'stocks': get_stocks})
assistant.parse_intents()
assistant.load_model('chatbot_model.pth', 'model_dimensions.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    response = assistant.process_message(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
