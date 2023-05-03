from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    return render_template('submit.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.debug = True
    app.run()