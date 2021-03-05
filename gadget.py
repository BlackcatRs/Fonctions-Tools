# sendMail
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(login_credentials, receiver_email, message):
    smtp_server = login_credentials[smtp_server]
    port = login_credentials[port]
    sender_email = login_credentials[sender_email]
    password = login_credentials[password]

    receiver_email = login_credentials[receiver_email]

    msg = MIMEMultipart() # create a message
    msg['Subject']= message[subject]

    # add in the message body
    msg.attach(MIMEText(message[body],"plain", "utf-8"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string().encode('ascii'))
