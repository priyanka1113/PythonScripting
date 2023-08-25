from smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage
html=Template(Path('emailindex.html').read_text())
msg=EmailMessage()
msg["from"]='priyanka Deo'
msg["To"]='dummy user'
msg['Subject']="you have won 100000000 dollares!"

#msg.set_content('I am master.I am the Prize!')
#for dynamic content
msg.set_content(html.substitute(name='priyanka'),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummy gmail id','credentials needed to be entered!')
	smtp.send_message(msg)


