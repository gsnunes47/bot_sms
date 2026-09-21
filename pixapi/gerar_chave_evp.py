from gerencianet import Gerencianet
from credenciais import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

def gerar_evp():
    response =  gn.pix_create_evp()
    return response

print(gerar_evp())
