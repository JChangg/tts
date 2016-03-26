from flask import Flask, jsonify
import tts

app = Flask(__name__)


@app.route('/speak/<text>', methods=['POST', 'GET'])
def speak(text):
	
	pos = tts.add_text(text)
	if pos >= 0:
		return jsonify({"content":text, "pos":pos})
	else:
		return jsonify({}), 503


if __name__ == '__main__':
	consumer = tts.Consumer()
	consumer.daemon = True
	consumer.start()
	app.run(debug=True, host='0.0.0.0')
