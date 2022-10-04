#!/usr/bin/env python3
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# https://realpython.com/python-send-email/#sending-fancy-emails

# read user, password of nguoi gui from txt file
def read_acc():
	user = passwd = ""
	with open("email_account.txt", "r") as f:
		file = f.readlines()
		user = file[0].strip()
		passwd = file[1].strip()

	return user,  passwd

# nguoi gui
# user, password = read_acc()
sender_email = 'ledat.fake@gmail.com'
password = 'Googleaccc3'

# nguoi nhan
receiver_email = "hsddung92.lpdat@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Test send email!"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
	Subject: python email

	This is from Dat

	Thank you! Sincerely!
"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
# part2 = MIMEText(html, 'html')

message.attach(part1)
# message.attach(part2)

port = 465
context = ssl.create_default_context()
smtp_server = "smtp.gmail.com"

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message.as_string())

print("Sent!!")

# error: Less security application access
# https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NyfLPPStLLGVmMa0LZ3Rhupd7L14MRgQ4k1AhuiVazk5TXiy6nIrQ2xEV1_RtV4E7bWjHjlpoG3oNAIEp1W7f2pbhfhQ
