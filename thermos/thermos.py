from flask import Flask, render_template,url_for

app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname
    
    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)
    
    def initials(self):
        return "{}.{}.".format(self.firstname[0],self.lastname[0])
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="This is my title", text="This is my text.", user=User("Pixie", "Goodog"))

@app.route('/add')
def add():
    return render_template('add.html')

if __name__== '__main__':
    app.run(host='0.0.0.0')
