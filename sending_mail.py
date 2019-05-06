import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'xxxxxxxxxx@gmail.com'
msg['To'] = 'xxxxxxxxxx@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('xxxxxxxx@gmail.com', 'Password')
mailserver.sendmail('xxxxxxxx@gmail.com', 'xxxxxxxxx@gmail.com', msg.as_string())
mailserver.quit()