import smtplib, ssl

def read_acc():
	user = passw = ""
	with open("email_account.txt", "r") as f:
		file = f.readlines()
		user = file[0].strip()
		passw = file[1].strip()

	return user,  passw

port = 465

sender, password = read_acc()
recieve = "hsddung92.lpdat@gmail.com"

message = """\
Subject: python email

This is from Dat

Thank you! Sincerely!
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender, password)
	server.sendmail(sender, recieve, message)

print("Sent!!")
# error: Less security application access
# https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
