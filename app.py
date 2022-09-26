
from flask import Flask,session,render_template,request,redirect,url_for

app =Flask(__name__)
app.secret_key = '5bfef38cecca6314b07863d3cbd93a790291f6161468bf6364d9bfd680eb301c'

##### Connecting to Company Database
db = client.User

@app.route('/', methods=['POST','GET'])
def index():
    if 'name' in session:
        return 'You are logged in as ' + session['name']
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)