import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Saabir Haaji'
email['to'] = 'abuukarhaaji9@gmail.com'
email['subject'] = 'Use python to send emails'

# email content 
email.set_content(html.substitute(name= 'Saalax'), 'html  ')

# email.set_content(html.substitute({'name': 'Saalax', 'age': 13})) # if the html had mulitple templates 

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #  establishing a connection  to an SMTP to the server. 
    smtp.starttls()  # connecting securely with the server 
    # connect with the email
    # PROF-ABDI-PYTHON
    smtp.login('saabirhaaji10@gmail.com', 'ihed bszv fgaa mvfv')
    smtp.send_message(email)
    print('we sent the email')

    
