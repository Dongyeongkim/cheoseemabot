from konlpy.tag import Kkma
from cheoseema import cheoseema as chs
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/translate')
def translate():
    if request.method == 'GET':
        return render_template('translation.html')
    return render_template('translation.html')


@app.route('/translate', methods=['POST'])
def trup():
    text = request.form['text']
    f = open("x.txt", 'w')
    f.write(text)
    f.close()
    kkma = Kkma()
    f = open('x.txt', 'r')
    sentences = f.read()
    sentence_list = kkma.sentences(sentences)
    chsr = chs(sentence_list)
    return chsr.처지(), chsr.심정(), chsr.어조()


@app.route('/evaluate')
def evaluate():
    return render_template('grading.html')


if __name__ == "__main__":
    app.run()
