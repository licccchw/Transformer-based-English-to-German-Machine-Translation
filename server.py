from flask import Flask, render_template, request
from transformer_en_de.module import MTTransformer

app = Flask(__name__)
model = MTTransformer()

@app.route('/translate', methods=['POST'])
def translate():
    src_text=request.form.get('src_text')
    print(src_text)
    trg_text = model.predict([src_text])[0]
    return trg_text

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0')