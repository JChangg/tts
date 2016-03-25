from flask import Flask, jsonify
import tts

app = Flask(__name__)


@app.route('/speak/<text>', methods=['POST', 'GET'])
def speak(text):
    tts.add_text(text)
    return jsonify({"content":text})


if __name__ == '__main__':
    consumer = tts.Consumer()
    consumer.daemon = True
    consumer.start()
    app.run(debug=True, host='0.0.0.0')
