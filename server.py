from flask import Flask, Response, request, current_app, abort
import subprocess

app = Flask(__name__)

def transcode(channel):
    process = subprocess.Popen(['./twitch.sh', channel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        while True:
           chunk = process.stdout.read(1024)
           if not chunk:
               break
           yield chunk
    finally:
        process.terminate()
        process.wait()

@app.route('/')
def hello_world():
    print(request.headers)
    return Response(transcode('joehills'), mimetype='video/mpegts')

@app.route('/twitch/')
def stream_video():
    print(request.headers)
    channel = request.args.get('channel')
    return Response(transcode(channel), mimetype='video/mpegts')

if __name__ == '__main__':
    app.run(port=1234, threaded=True)
