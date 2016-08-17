import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'momodota2@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'swag@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with the server
server.connect()
try:
    server.sendmail('author@example.com', ['momodota2@gmail.com'], msg.as_string())
finally:
    server.quit()