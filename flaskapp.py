import flask
import os
import threading

app = flask.Flask(__name__)
@app.route('/')
def index():
    
    threading.Thread(target=lambda:os.system('python multiplechoice.py')).start()
    return "Python task started"
if __name__ == "__main__":
    app.run()