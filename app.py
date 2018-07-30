from flask import Flask, request, render_template
from hl1voxsentenceformer import hl1sentenceformer as vox


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html', phrases = vox.getcachedsentences())

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

    sentence_data = vox.savetomp3(processed_text)
    print("received: " +  str(sentence_data))

    return render_template('play.html', mp3_link = sentence_data['path'],
                                        says = sentence_data['sentence'])
