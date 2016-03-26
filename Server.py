from flask import Flask, jsonify

import Music as mp
import tts

app = Flask(__name__)

tts_server = tts.TextToSpeaker()
music_player = mp.MusicPlayer()


@app.route('/speak/<text>', methods=['POST', 'GET'])
def speak(text):
    pos = tts_server.add_text(text)
    if pos >= 0:
        return jsonify({"content": text, "pos": pos})
    else:
        return jsonify({}), 503


if __name__ == '__main__':
    tts_server.start()
    music_player.start()
    app.run(debug=True, host='0.0.0.0')
