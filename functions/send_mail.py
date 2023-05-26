import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 2525 
smtp_server = "smtp.mailtrap.io"
login = "42cdecf4678456" 
password = "83424a066fba49" 


def send_mail(engine, speak, listen):
    speak(engine, "What is your email?")
    sender_email = listen(engine)
    speak(engine, "Who do you want to send the email to?")
    receiver_email = listen(engine)
    speak(engine, "What is the subject of the email?")
    subject = listen(engine)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    speak(engine, "What should the email contain?")
    text = listen(engine)

   
    html = f"""\
    <html>
    <body>
        <h1 style="text-align:center; color:red; font-size:35px">Email sent with Intellify</h1>
        <h3 style="text-align:center; font-size: 20px; text-transform:uppercase">{text}</h3>
    </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # send your email
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    speak(engine, 'Email sent successfully.')