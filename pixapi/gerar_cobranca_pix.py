from gerencianet import Gerencianet
import base64
import time

CREDENTIALS = {
    'client_id': 'GERENCIANET_CLIENT_ID',
    'client_secret': 'GERENCIANET_CLIENT_SECRET',
    'sandbox': False,
    'certificate': 'pixapi/certificado-bot_telegram_cert.pem'
}

gn = Gerencianet(CREDENTIALS)

def gerar_cobranca_pix(cpf, nome, valor):
    body = {
        'calendario': {
            'expiracao': 3600
        },
        'devedor': {
            'cpf': f'{cpf}',
            'nome': f'{nome}'
        },
        'valor': {
            'original': f'{valor}'
        },
        'chave': 'PIX_KEY',
        'solicitacaoPagador': 'Cobrança dos serviços prestados.'
    }
    cobranca_pix =  gn.pix_create_immediate_charge(body=body)
    params = {
        'id': cobranca_pix['loc']['id']
    }
    response =  gn.pix_generate_QRCode(params=params)
    #Generate QRCode Image
    if('imagemQrcode' in response):
        with open("qrCodeImage.png", "wb") as fh:
            fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))
    return response['qrcode']

gerar_cobranca_pix(cpf=00000000000, nome='Usuario Teste', valor=10.01)
