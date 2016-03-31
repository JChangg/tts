from flask import Flask, jsonify

import Speech

app = Flask(__name__)

query_server = Speech.QueryHandler()


@app.route('/speak/<text>', methods=['POST', 'GET'])
def speak(text):
    pos = tts_server.add_text(text)
    if pos >= 0:
        return jsonify({"content": text, "pos": pos})
    else:
        return jsonify({}), 503


if __name__ == '__main__':
    query_server.start()
    app.run(debug=True, host='0.0.0.0', port=80)
