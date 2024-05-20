import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from os import path

class EmailService:
    @staticmethod
    def send_email_with_attachment(sender_email, receiver_email, subject, body, file_path):
        msg = MIMEMultipart()

        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        msg.attach(MIMEText(body, 'plain'))

        if path.isfile(file_path):
            file = MIMEBase('application', 'octet-stream')
            file.set_payload(open(file_path, 'rb').read())
            encoders.encode_base64(file)
            file.add_header('Content-Disposition', "attachment; filename= %s" % path.basename(file_path))
            msg.attach(file)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender_email, "dowp okge akui ckkw")
                smtp.send_message(msg)
            return True, 'Correo enviado con éxito'
        except Exception as e:
            return False, str(e)