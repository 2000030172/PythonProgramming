import smtplib
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cmprashanth2002@gmail.com,'
app.config['MAIL_PASSWORD'] = 'Prashanth2002'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hello', sender='cmprashanth2002@gmail.com', recipients=['cmprashanth2002@gmail.com','2000030172@kluniversity.in'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)