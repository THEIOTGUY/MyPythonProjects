import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "vaidandeayush.av@gmail.com"  # Enter your address
receiver_email = "vaidandeayush.av@gmail.com"  # Enter receiver address
password = "qzqujoudqvetxnwr" ## go to google security and then create an app password 
message = """\
Subject: this is the subject 

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)