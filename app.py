from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def sendMessage():
    data = request.get_json()

    print(data)

    response = {
        'result' : 'success'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.debug = True
    app.run()