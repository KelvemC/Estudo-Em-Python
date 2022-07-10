from smtplib import SMTP
import ssl
import email.message

msg = email.message.Message()

body = """
Ola, mensagem de teste
"""

setor = 'B'

msg['Subject'] = f'Teste do script de mail: {setor}'
msg['From'] = 'blablabla@gmail.com' #este email não existe, é só um exemplo
msg['To'] = 'ademiro@gmail.com' #este email não existe, é só um exemplo

msg.add_header('Content-type', 'text/html')
msg.set_payload(body)

senha = '04196057208092'#essa senha não existe é só um exemplo 

context = ssl.create_default_context()
with SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()#verifica se a conexão está Ok
    conexao.starttls(context=context)#começa a criptgrafia
    conexao.login(msg['From'], senha)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    conexao.quit()


