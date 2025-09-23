import pandas as pd
import requests
from datetime import datetime
import os

# URL do arquivo TXT
url = "https://www.fenabrave.org.br/ftp/ASSODAF/Emplacamento_Diario.txt"
r = requests.get(url)
r.raise_for_status()

# Processa os dados
data = [line.split(";") for line in r.text.strip().split("\n")]

# Cria DataFrame
df = pd.DataFrame(data[1:], columns=data[0] if len(data) > 1 else None)

# Nome do arquivo por dia da semana
dias = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']
nome_arquivo = f'Emplacamento_{dias[datetime.now().weekday()]}.xlsx'

# Salva Excel na pasta output
os.makedirs('output', exist_ok=True)
df.to_excel(f'output/{nome_arquivo}', index=False)
