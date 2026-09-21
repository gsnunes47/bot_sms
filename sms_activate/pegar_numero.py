from smsactivate.api import SMSActivateAPI  
from botconfig.config import bot
import time

API_KEY = "SMS_API_KEY"
sa = SMSActivateAPI(API_KEY)
sa.debug_mode = True
country = 73

def pegar_numero(chat, servico):
    number = sa.getNumber(country=73, service=servico)
    bot.send_message(chat, f"Seu número para verificação é: {number['phone']}")
    bot.send_message(chat, 'Após colocar o número, aguarde que te enviaremos o SMS com o código.')
    status = sa.getFullSms(id=number['activation_id'])
    tester = sa.getStatus(id=number['activation_id'])
    while status == "STATUS_WAIT_CODE":
        tester = sa.getStatus(id=number['activation_id'])
        status = sa.getFullSms(id=number['activation_id'])
        time.sleep(5)
    bot.send_message(chat, f'{status}')
