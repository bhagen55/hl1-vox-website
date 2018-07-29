from flask import Flask, request, render_template
from hl1voxsentenceformer import hl1sentenceformer as vox


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

    sentence = vox.savetomp3(processed_text)

    return render_template('play.html', mp3_link = sentence,
                                        says = sentence)
