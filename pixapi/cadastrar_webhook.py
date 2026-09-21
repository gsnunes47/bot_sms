from gerencianet import Gerencianet

CREDENTIALS = {
    'client_id': 'GERENCIANET_CLIENT_ID',
    'client_secret': 'GERENCIANET_CLIENT_SECRET',
    'sandbox': False,
    'certificate': 'pixapi/certificado-bot_telegram_cert.pem'
}

gn = Gerencianet(CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'true'
}

params = {
    'chave': 'PIX_KEY'
}

body = {
    'webhookUrl': 'https://example.com:5000'
}

response =  gn.pix_config_webhook(params=params, body=body, headers=headers)
print(response)
