from flask import Flask, request, render_template
from hl1voxsentenceformer import hl1sentenceformer as vox
from flask_simplelogin import SimpleLogin, login_required


app = Flask(__name__)

app.config['SECRET_KEY'] = 'something-secret'
app.config['SIMPLELOGIN_USERNAME'] = 'chuck'
app.config['SIMPLELOGIN_PASSWORD'] = 'norris'
SimpleLogin(app)

@app.route('/vox')
@login_required
def my_form():
    return render_template('index.html', phrases = vox.getcachedsentences())


@app.route('/vox', methods=['POST'])
@login_required
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

    sentence_data = vox.savetomp3(processed_text)
    print("received: " +  str(sentence_data))

    return render_template('play.html', mp3_link = sentence_data['path'],
                                        says = sentence_data['sentence'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
