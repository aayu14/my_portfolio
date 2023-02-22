from flask import Flask,render_template,request,redirect,url_for,send_file
from flask_mail import Mail,Message



app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=""
app.config['MAIL_PASSWORD']=""
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message',methods=['POST','GET'])
def send_message():
    if request.method=="POST":
        email=request.form['email']
        name=request.form['name']
        phone=request.form['phone_number']
        msg=request.form['message']

        message=Message(subject=f" Mail from:{name}",body=f"Name:{name}\nE-mail:{email}\nPhone:{phone}\n\n\n{msg}",sender=f"{email}",recipients=['am94947651@gmail.com'])     
        mail.send(message)
        success="message sent"
        print(success)
        return redirect('/')


@app.route('/download_file')
def download_file():
    path='static/cv/Ayush_mishra_cv.pdf'
    return  send_file(path,as_attachment=True)










if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')

