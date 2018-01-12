from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SERECT_KEY'] = 'secret'
sio = SocketIO(app)

if __name__ == '__main__':
    sio.run(app)
