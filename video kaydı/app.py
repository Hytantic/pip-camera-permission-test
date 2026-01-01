from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Videoların kaydedileceği klasör
SAVE_PATH = "captured_videos"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        video_file = request.files['video']
        filename = f"{SAVE_PATH}/video_{os.urandom(4).hex()}.webm"
        video_file.save(filename)
        return "Başarılı", 200
    return "Hata", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)