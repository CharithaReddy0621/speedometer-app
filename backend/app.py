from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from database import db_session
from models import SpeedData
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/insert', methods=['POST'])
def insert_speed():
    data = request.json
    speed = SpeedData(timestamp=int(time.time()), speed=data['speed'])
    db_session.add(speed)
    db_session.commit()
    socketio.emit('update_speed', {'speed': data['speed']})
    return jsonify({'status': 'success'}), 200

@app.route('/latest', methods=['GET'])
def get_latest_speed():
    latest = db_session.query(SpeedData).order_by(SpeedData.timestamp.desc()).first()
    return jsonify({'speed': latest.speed if latest else 0}), 200

@socketio.on('connect')
def on_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
