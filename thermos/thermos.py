from flask import Flask, renter_template,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    render_template('index.html')

if __name__= '__main__':
    app.run(host='0.0.0.0')
