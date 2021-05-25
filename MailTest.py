import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def testmail(emisor, contra, receptor, Asunto, Des, filename):
    port = 465  #SSL
    smtp_server = "smtp.gmail.com"

    #Correo
    message = MIMEMultipart()
    message["Subject"] = Asunto
    message.attach(MIMEText(Des, "plain"))

    #filename = "Home.png"

    #Archivo Adjunto
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    #Contenido seguro SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(emisor, contra)
        server.sendmail(emisor, receptor, text)

    print()
