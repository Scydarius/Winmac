from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    messages.append((username, message))
    return jsonify({'username': username, 'message': message})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})


@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)