from datetime import datetime
from flask import Flask, render_template,url_for,request
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname
    
    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)
    
    def initials(self):
        return "{}.{}.".format(self.firstname[0],self.lastname[0])
 
 bookmarks = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="This is my title", text="This is my text.", user=User("Pixie", "Goodog"))

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url' + url)
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500

if __name__== '__main__':
    app.run(host='0.0.0.0')
