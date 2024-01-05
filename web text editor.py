from flask import Flask, render_template, request

app = Flask(__name__)

## Global variable to store the text content
text_content = ""


@app.route('/')
def index():
    return render_template('index.html', text_content=text_content)


@app.route('/save', methods=['POST'])
def save():
    global text_content
    text_content = request.form['text']
    return ''


if __name__ == '__main__':
    app.run(debug=True)
