# 📊 Emplacamento Diário FENABRAVE


![GitHub last commit](https://img.shields.io/github/last-commit/gustavosantos96/emplacamentos)
![GitHub repo size](https://img.shields.io/github/repo-size/gustavosantos96/emplacamentos)
![GitHub issues](https://img.shields.io/github/issues/gustavosantos96/emplacamentos)
![GitHub stars](https://img.shields.io/github/stars/gustavosantos96/emplacamentos?style=social)

Este repositório contém um script em Python e um workflow do GitHub Actions que automatizam o processo de:

1. Baixar o arquivo de emplacamento diário da **FENABRAVE**.
2. Converter os dados em uma planilha Excel.
3. Enviar a planilha por e-mail automaticamente.
4. Executar o processo diariamente via agendamento no GitHub Actions.

---

## 🚀 Funcionalidades

- Download automático do arquivo `Emplacamento_Diario.txt` da FENABRAVE.
- Conversão para planilha Excel (`.xlsx`) com data no nome do arquivo.
- Envio da planilha por e-mail usando servidor SMTP do Gmail.
- Execução diária às **07h BRT (10h UTC)** via GitHub Actions.
- Remoção do arquivo local após envio (opcional).

---

## 📂 Estrutura do Repositório

- `emplacamento_email.py` → Script principal em Python.
- `.github/workflows/emplacamento_diario.yml` → Workflow do GitHub Actions para execução automática.

---

## ⚙️ Configuração

### 1. Variáveis de ambiente
No GitHub, configure os **Secrets** para autenticação do e-mail:

- `EMAIL_USER` → Endereço de e-mail remetente.
- `EMAIL_PASS` → Senha ou App Password do Gmail.

### 2. Dependências
O script utiliza as seguintes bibliotecas Python:

- `pandas`
- `openpyxl`
- `requests`

Instaladas automaticamente pelo workflow.

### 3. Workflow
O workflow está configurado para rodar diariamente às 07h BRT:

```yaml
on:
  schedule:
    - cron: '0 10 * * *'  # 07h BRT (10h UTC)
  workflow_dispatch: 
```
---

## 📧 Envio de E-mail

- Servidor SMTP: `smtp.gmail.com`  
- Porta: `587`  
- Autenticação via variáveis de ambiente.  
- Destinatário padrão: `gustavo.santos@daftrucks.com` (pode ser alterado no script).

---

## 🛡️ Observações

- É necessário habilitar **App Passwords** ou permitir acesso de apps menos seguros no Gmail para autenticação.  
- O workflow só funcionará se os **Secrets** estiverem corretamente configurados.  
- O arquivo Excel é removido após o envio para evitar acúmulo de arquivos no runner.  

---

## 📅 Agendamento

O processo é executado automaticamente todos os dias às **07h BRT (10h UTC)**.  
Também pode ser disparado manualmente pelo GitHub Actions (`workflow_dispatch`).  

---

## 🔧 Uso Local (opcional)

Para rodar o script manualmente:

```bash
pip install pandas openpyxl requests
python emplacamento_email.py
```
![License](https://img.shields.io/github/license/gustavosantos96/emplacamentos)
![Python Version](https://img.shields.io/badge/python-3.10-blue)
