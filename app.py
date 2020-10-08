from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Nimish bhaiya OP'

if __name__ == '__main__':
    app.run()
