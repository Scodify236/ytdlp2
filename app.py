from flask import Flask, request, jsonify
from yt_dlp_helper import get_audio_url

app = Flask(__name__)

@app.route('/get-audio-url', methods=['GET'])
def audio_url():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    try:
        audio_url = get_audio_url(video_url)
        return jsonify({"audio_url": audio_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)