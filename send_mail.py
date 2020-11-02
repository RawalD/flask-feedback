import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '2d76f525fb5eae'
    password = 'badae383e8660d'
    message = f'<h3>New Feedback</h3><ul><li>Customer {customer}</li><li>Dealer{ dealer}</li><li>Rating {rating}</li><li>Comments {comments}</li></ul>'

    sender_email = 'email@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Toyota Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())