import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

password = 'wjmkywzqcfyuuolb'
username = 'pythonsample4@gmail.com'


def send_email_to(subject, name, message, user_mail):
    my_context = ssl.create_default_context()
    subject = f"Subject: {subject}\n"
    message = subject + f"Hey {name},\n" + message
    try:
        with smtplib.SMTP_SSL(host, port, context=my_context) as server:
            server.login(username, password)
            server.sendmail(username, user_mail, message)
    except Exception as _:
        pass
