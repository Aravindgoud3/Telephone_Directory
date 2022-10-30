from flask import Flask, render_template, url_for, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

database={}

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        name=request.form.get('name')
        number=request.form.get('number')
        database[name]=number
    return render_template('add.html')

@app.route('/display',methods=['GET','POST'])
def display():
    return render_template('display.html',database=database)

@app.route('/search',methods=['GET','POST'])
def search():
    name=request.form.get('name1')
    if request.method=='POST':
        if name in database.keys():
            return render_template('searchshow.html',name=name,phone=database[name])
        else:
            return render_template('fail.html')
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
