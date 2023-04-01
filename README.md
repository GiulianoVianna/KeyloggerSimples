# Keylooger Simples
Keylooger Simples desenvolvido em python para estudo.

## Definição da Aplicação
Esta é uma aplicação de keylogger simples em Python que registra as teclas pressionadas pelo usuário e envia o registro por e-mail periodicamente. 

## Bibliotecas

<b>pynput:</b> A biblioteca pynput permite monitorar e controlar dispositivos de entrada, como mouse e teclado. Neste caso, ela é usada para capturar eventos do teclado.

<b>smtplib:</b> A biblioteca smtplib do Python permite o envio de e-mails usando o protocolo Simple Mail Transfer Protocol (SMTP). Neste caso, é usada para enviar o arquivo de registro de teclas por e-mail.

<b>email.mime.multipart:</b> Este módulo define classes para gerenciar mensagens MIME de várias partes. É usado para criar mensagens de e-mail com anexos.

<b>email.mime.base:</b> Este módulo define a classe base para todos os outros objetos MIME do módulo email.mime.

<b>email.mime.text:</b> Este módulo define a classe MIMEText, que é usada para criar objetos MIME do tipo text/plain.

<b>email.encoders:</b> Este módulo contém funções para codificar e decodificar arquivos anexados a mensagens MIME.

<b>time:</b> A biblioteca time do Python fornece funções relacionadas ao tempo. Neste caso, ela é usada para criar um intervalo de tempo entre o envio de e-mails.

### Bliblioteca que precisa ser instalada:

```bash
pip install pynput
```
</pre>

## Vídeo
https://user-images.githubusercontent.com/101942554/229258035-f514d686-1e89-46b3-98cb-04f235aa61ab.mp4



