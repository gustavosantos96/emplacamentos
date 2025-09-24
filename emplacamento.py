import pandas as pd
import requests
import smtplib
from datetime import datetime
from email.message import EmailMessage
import os

# Baixar o arquivo
url = "https://www.fenabrave.org.br/ftp/ASSODAF/Emplacamento_Diario.txt"
r = requests.get(url)
r.raise_for_status()

data = [line.split(";") for line in r.text.strip().split("\n")]
df = pd.DataFrame(data[1:], columns=data[0] if len(data) > 1 else None)

dias = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']
nome_arquivo = f'Emplacamento_{dias[datetime.now().weekday()]}.xlsx'
df.to_excel(nome_arquivo, index=False)

# Configurações do email
smtp_server = "smtp.office365.com"
smtp_port = 587
email_user = "gustavo.santos@daftrucks.com"
email_pass = "Pontagrossa@2025v3"
email_to = "gustavo.santos@daftrucks.com"  # Ou use outro destinatário, conforme o fluxo do Power Automate

# Montar email
msg = EmailMessage()
msg['Subject'] = f"Emplacamento Diário - {dias[datetime.now().weekday()]}"
msg['From'] = email_user
msg['To'] = email_to
msg.set_content("Planilha de emplacamento em anexo. Envio automático.")

# Anexar planilha
with open(nome_arquivo, "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=nome_arquivo)

# Enviar email
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_user, email_pass)
    smtp.send_message(msg)

# Remover arquivo local (opcional)
os.remove(nome_arquivo)
