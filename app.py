from flask import Flask, render_template, jsonify

app = Flask(__name__)

# List of sentences to display
sentences = [
    "Hello, lets get this started 😊",
    "Carry, a person around the room or chug your drink. 🛳️",
    "Challenge the 3rd person to your left to a dance-off right now 💃🕺",
    "Scream in the ears of the 4th person from your rigt 🔪",
    "Tell the 6th person from your left why they are ugly 🧀",
    "Speak in a robot voice to the 4th person from your left until they laugh 🤖😂",
    "Slap 2nd person from your right 😱"
]

@app.route('/')
def index():
    return render_template('index.html')

# API to handle sentence changes
@app.route('/get_sentence/<int:index>')
def get_sentence(index):
    if 0 <= index < len(sentences):
        return jsonify({'sentence': sentences[index]})
    return jsonify({'error': 'Index out of bounds'}), 400

if __name__ == '__main__':
    app.run(debug=True)
