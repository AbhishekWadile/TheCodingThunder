from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import mapped_column


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/codingthander'
db=SQLAlchemy(app)

class Contacts(db.Model):

    '''
     sno name email phone_num msg date
    '''
    sno = db.column(INTEGER(unsigned=True), primary_key=True)
    name = db.column(String, nullable=False)
    email = db.column(String,nullable=False)
    phone_num = db.column(String,nullable=False)
    msg = db.column(String)
    date = db.column(String)

# @app.route("/")
# def hello():
#     return render_template('index.html')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        msg=request.form.get('msg')
        
        entry = Contacts(name=name,email=email,phone_num=phone,msg=msg)
        db.session.add(entry)
        db.session.commit()


    return render_template('contact.html')

app.run(debug=True)
