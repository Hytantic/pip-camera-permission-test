import eventlet
eventlet.monkey_patch()
from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/panel')
def panel():
    return render_template('panel.html')

# iOS İkonu için gerekli dosya gönderici
@app.route('/manifest.json')
def manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

@socketio.on('video_frame')
def handle_frame(data):
    # Görüntüyü panele gönder
    emit('stream_to_panel', data, broadcast=True)

if __name__ == '__main__':
    print("Sunucu Başlatıldı: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000)