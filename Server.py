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


@app.route('/song/add/<file_name>', methods=['POST', 'GET'])
def song_add(file_name):
    music_player.add_song(file_name)
    return jsonify({'queued': file_name})


@app.route('/song/skip', methods=['POST', 'GET'])
def skip():
    skipped = music_player.current
    music_player.skip_song()
    return jsonify({'skipped': skipped})


@app.route('/song/pause', methods=['POST', 'GET'])
def pause():
    paused = music_player.current
    music_player.pause_song()
    return jsonify({'paused': paused})


@app.route('/song/resume', methods=['POST', 'GET'])
def resume():
    un_paused = music_player.current
    music_player.un_pause_song()
    return jsonify({'resumed': un_paused})


if __name__ == '__main__':
    tts_server.start()
    music_player.start()
    app.run(debug=True, host='0.0.0.0', port=80)
