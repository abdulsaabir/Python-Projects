import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Saabir Haaji'
email['to'] = 'abuukarhaaji9@gmail.com'
email['subject'] = 'Use python to send emails'

# email content 
email.set_content('i am sending this email using python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #  establishing a connection  to an SMTP to the server. 
    smtp.starttls()  # connecting securely with the server 
    # connect with the email
    smtp.login('saabirhaaji10@gmail.com', 'ihed bszv fgaa mvfv')
    smtp.send_message(email)
    print('we sent the email')

    
