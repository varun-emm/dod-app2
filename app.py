from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of sentences to display
sentences = [
    "The 1st person from your right will pour water on your head 💧",
    "Tell the 6th person from your right why you think they’ll never be successful 😐",
    "The 4th person from your right will scream in your ears 🔪",
    "Let the 6th person from your right take something of yours and throw it in the trash 🧦",
    "Let the 5th person from your left write a funny word on your forehead with a marker 🖊️",
    "Do 5 terrible cartwheels in front of everyone, no matter how bad they are 🤸",
    "The 1st person from your left will blindfold you, and you must identify 3 items by smell 👃",
    "Sing an embarrassing song 🎤",
    "The 4th person from your right will throw a random object at you, and you have to catch it with your mouth 🦷",
    "Let the 3rd person from your right pick any object in the room, and you must balance it on your head for 2 minutes 🏺",
    "Let the 6th person from your left slap you with a shoe 🥿",
    "Tell the 3rd person from your left why they are the most annoying person here 😈",
    "Pretend to be a dog and bark at the 3rd person from your right for 2 minutes 🐕",
    "The 3rd person from your left will pour a random drink into your shoe, and you must drink from it 🥤👟",
    "The 1st person from your left will pour a random drink into your hand, and you must drink it 🍷",
    "The 1st person from your right will mess up your hair completely ✂️",
    "Have a staring contest with the 2nd person from your left, and whoever blinks first drinks 🤡",
    "Tell the 4th person from your left why you think they have bad hygiene 🦠",
    "Let the 6th person from your right put together an outfit for you from random items in the room, and you must wear it for 10 minutes 👗",
    "Let the 2nd person from your left make up an embarrassing name for you, and you must introduce yourself that way 🤪",
    "Become a slave to the 5th person from your right and call them 'Master' while they give you 2 ridiculous commands 👑",
    "The 3rd person from your left will text your parents something embarrassing from your phone 📲",
    "Do 10 jumping jacks while reciting the alphabet 🤸",
    "Let the 2nd person from your right spit water in your face, and you can't wipe it off 💦",
    "Let the 3rd person from your left choose a dare for you that you must do 🤐",
    "Just drink it because you're going to die alone 🍷",
    "Tell your first biased impression of the 2nd person from your right 🤡",
    "Introduce yourself as a robot and speak in a robotic voice for 2 minutes 🤖",
    "The 3rd person from your right will blindfold you and put something gross on your hand, and you have to guess what it is 👀",
    "The 7th person from your left will give you three ridiculous compliments, and you must respond as if they’re the greatest things you’ve ever heard 👏",
    "Let the 5th person from your right blindfold you and feed you something 🍴",
    "Let the 3rd person from your left throw an object at you, and you can’t dodge it 🏀",
    "Tell the 6th person from your left why they are ugly 🧀",
    "Let the 2nd person from your left draw something on your face 😈",
    "The 3rd person from your left will pick an embarrassing sentence, and you must shout it while everybody else films it 📢",
    "Do a silly dance in front of the 3rd person from your right 💃",
    "The first person on your left will burp in your face 😱",
    "2nd person from your left will slap you 5 times, and you should say “thank you” each time 😱",
    "Let the 3rd person from your left take a funny picture of you and send it to your family group 🤡",
    "Tell a joke to the group, and if no one laughs, drink twice 🤪",
    "I let you live, you can pass this round ✨",
    "Just drink it loser 🖕",
    "Let the 5th person from your right tell you a pose, and you must stay in that position for 2 minutes 🕴️",
    "Lick you feet, while making eye contact with the third person from your right🤪",
]

# Shuffle sentences once and store in-memory
shuffled_sentences = sentences[:]
random.shuffle(shuffled_sentences)
current_index = 0  # Starting index

@app.route('/')
def index():
    return render_template('index.html')

# API to handle sentence changes
@app.route('/get_sentence/<int:index>')
def get_sentence(index):
    global current_index
    if 0 <= index < len(shuffled_sentences):
        current_index = index  # Update the current index
        return jsonify({'sentence': shuffled_sentences[index]})
    return jsonify({'error': 'Index out of bounds'}), 400

if __name__ == '__main__':
    app.run(debug=True)
