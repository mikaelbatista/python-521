import os
import smtplib
import email.mime.text
import time

import dotenv


dotenv.load_dotenv()

CONTADOR = 0

def limpar_log(nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as f:
        pass

def encontrar_warning(linha):
    data, level, arquivo, mensagem = linha.split('|')
    if 'WARNING' in level and 'Falha na autenticação' in mensagem:
        return True
    return False
        
def enviar_email():

    smtp = smtplib.SMTP()

    server = 'smtp.gmail.com'
    port = 587

    destination = 'mikaelmika.mb@gmail.com'

    user = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    smtp.connect(server, port)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user, password)

    
    mensagem = "Tentativa de Acesso"

    mail = email.mime.text.MIMEText(mensagem, 'html')

    mail.set_charset('utf-8')
    
    mail['From'] = user
    mail['To'] = destination
    mail['Subject'] = 'Tentativa de acesso'


    smtp.sendmail(user, destination, mail.as_string())

enviar_email()  
exit()

done = False
while not done:
    with open('app.log', 'r') as f:
        for line in f.readlines():
            try:
                if encontrar_warning(line.strip()):
                    CONTADOR = CONTADOR + 1
            except Exception:
                pass
            if CONTADOR == 3:
                enviar_email()
                CONTADOR = 0
    limpar_log('app.log')
    time.sleep(1.0)
