from smsactivate.api import SMSActivateAPI
import time

API_KEY = "SMS_API_KEY"
sa = SMSActivateAPI(API_KEY)
country = 73

number = sa.getNumber(country=73, service='mb')
# number = {'activation_id': '0000000000', 'phone': '5500000000000'}
print(f"Seu número para verificação é: {number['phone']}")
# bot.send_message(callback.message.chat.id, f"Seu número para verificação é: {number['phone']}")
print('Após colocar o número, aguarde que te enviaremos o SMS com o código.')
# bot.send_message(callback.message.chat.id, 'Após colocar o número, aguarde que te enviaremos o SMS com o código.')
status = sa.getFullSms(id=number['activation_id'])
tester = sa.getStatus(id=number['activation_id'])
while status == "STATUS_WAIT_CODE":
    tester = sa.getStatus(id=number['activation_id'])
    status = sa.getFullSms(id=number['activation_id'])
    time.sleep(5)
print(status)

