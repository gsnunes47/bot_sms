import telebot
import requests
import time
from botconfig.config import bot
from pixapi.gerar_cobranca_pix import gerar_cobranca_pix
from sms_activate.pegar_numero import pegar_numero
from database import database, app
from database.models import Usuario

chave = "PIX_KEY"

def verificar(mensagem):
    if mensagem.text.isnumeric() and len(mensagem.text) == 11:
        with app.app_context():
            usuario = Usuario.query.filter_by(cpf=f'{mensagem.text}').first()
            if usuario:
                bot.send_message(mensagem.chat.id, text='CPF já cadastrado')
            else:
                usuario = Usuario(id_telegram=f'{mensagem.from_user.id}', nome=f'{mensagem.from_user.first_name} {mensagem.from_user.last_name}', cpf=f'{mensagem.text}')
                database.session.add(usuario)
                database.session.commit()
                bot.send_message(mensagem.chat.id, text='Cadastro realizado com sucesso!')
        return False
    return True

@bot.message_handler(commands=['cadastro'])
def cadastro(mensagem):
    bot.send_message(mensagem.chat.id, text='🚨ATENÇÃO🚨')
    bot.send_message(mensagem.chat.id, text='Para realizar o cadastro digite o seu CPF no seguinte modelo: 12345678901')
    bot.send_message(mensagem.chat.id, text='Sem pontos ou traços, APENAS os números.')

@bot.message_handler(commands=['servicos'])
def servicos(mensagem):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    agibank = telebot.types.InlineKeyboardButton('Agibank | R$10,00', callback_data='agibank')
    airbnb = telebot.types.InlineKeyboardButton('Airbnb | R$10,00', callback_data='airbnb')
    aliexpress = telebot.types.InlineKeyboardButton('Aliexpress | R$10,00', callback_data='aliexpress')
    amazon = telebot.types.InlineKeyboardButton('Amazon | R$10,00', callback_data='amazon')
    aposta_ganha = telebot.types.InlineKeyboardButton('Aposta ganha | R$10,00', callback_data='aposta_ganha')
    apple = telebot.types.InlineKeyboardButton('Apple | R$10,00', callback_data='apple')
    astropay = telebot.types.InlineKeyboardButton('Astropay | R$10,00', callback_data='astropay')
    badoo = telebot.types.InlineKeyboardButton('Badoo | R$10,00', callback_data='badoo')
    baidu = telebot.types.InlineKeyboardButton('Baidu | R$10,00', callback_data='baidu')
    banqi = telebot.types.InlineKeyboardButton('Banqi | R$10,00', callback_data='banqi')
    bet365 = telebot.types.InlineKeyboardButton('Bet365 | R$10,00', callback_data='bet365')
    bitso = telebot.types.InlineKeyboardButton('Bitso | R$10,00', callback_data='bitso')
    blablacar = telebot.types.InlineKeyboardButton('Blablacar | R$10,00', callback_data='blablacar')
    brahma = telebot.types.InlineKeyboardButton('Brahma | R$10,00', callback_data='brahma')
    budweiser = telebot.types.InlineKeyboardButton('Budweiser | R$10,00', callback_data='budweiser')
    yowin = telebot.types.InlineKeyboardButton('Yowin | R$10,00', callback_data='yowin')
    celcoin = telebot.types.InlineKeyboardButton('Celcoin | R$10,00', callback_data='celcoin')
    cloudbet = telebot.types.InlineKeyboardButton('Cloudbet | R$10,00', callback_data='cloudbet')
    corona = telebot.types.InlineKeyboardButton('Corona | R$10,00', callback_data='corona')
    cumbuca = telebot.types.InlineKeyboardButton('Cumbuca | R$10,00', callback_data='cumbuca')
    daki = telebot.types.InlineKeyboardButton('Daki | R$10,00', callback_data='daki')
    didi = telebot.types.InlineKeyboardButton('Didi | R$10,00', callback_data='didi')
    discord = telebot.types.InlineKeyboardButton('Discord | R$10,00', callback_data='discord')
    dotz = telebot.types.InlineKeyboardButton('Dotz | R$10,00', callback_data='dotz')
    ebay = telebot.types.InlineKeyboardButton('Ebay | R$10,00', callback_data='ebay')
    facily = telebot.types.InlineKeyboardButton('Facily | R$10,00', callback_data='facily')
    foodpanda = telebot.types.InlineKeyboardButton('Foodpanda | R$10,00', callback_data='foodpanda')
    get_response = telebot.types.InlineKeyboardButton('Get response | R$10,00', callback_data='get_response')
    gov = telebot.types.InlineKeyboardButton('Gov | R$10,00', callback_data='gov')
    gurubets = telebot.types.InlineKeyboardButton('Gurubets | R$10,00', callback_data='gurubets')
    icecasino = telebot.types.InlineKeyboardButton('Icecasino | R$10,00', callback_data='icecasino')
    icq = telebot.types.InlineKeyboardButton('Icq | R$10,00', callback_data='icq')
    ifood = telebot.types.InlineKeyboardButton('Ifood | R$10,00', callback_data='ifood')
    indriver = telebot.types.InlineKeyboardButton('Indriver | R$10,00', callback_data='indriver')
    instagram = telebot.types.InlineKeyboardButton('Instagram | R$10,00', callback_data='instagram')
    iti = telebot.types.InlineKeyboardButton('Iti | R$10,00', callback_data='iti')
    kwai = telebot.types.InlineKeyboardButton('Kwai | R$10,00', callback_data='kwai')
    linkedin = telebot.types.InlineKeyboardButton('Linkedin | R$10,00', callback_data='linkedin')
    meliuz = telebot.types.InlineKeyboardButton('Meliuz | R$10,00', callback_data='meliuz')
    mercado_livre = telebot.types.InlineKeyboardButton('Mercado livre | R$10,00', callback_data='mercado_livre')
    microsoft = telebot.types.InlineKeyboardButton('Microsoft | R$10,00', callback_data='microsoft')
    naver = telebot.types.InlineKeyboardButton('Naver | R$10,00', callback_data='naver')
    neon = telebot.types.InlineKeyboardButton('Neon | R$10,00', callback_data='neon')
    netflix = telebot.types.InlineKeyboardButton('Netflix | R$10,00', callback_data='netflix')
    nike = telebot.types.InlineKeyboardButton('Nike | R$10,00', callback_data='nike')
    nubank = telebot.types.InlineKeyboardButton('Nubank | R$10,00', callback_data='nubank')
    olx = telebot.types.InlineKeyboardButton('Olx | R$10,00', callback_data='olx')
    openai = telebot.types.InlineKeyboardButton('Openai | R$10,00', callback_data='openai')
    pagsmile = telebot.types.InlineKeyboardButton('Pagsmile | R$10,00', callback_data='pagsmile')
    paypal = telebot.types.InlineKeyboardButton('Paypal | R$10,00', callback_data='paypal')
    pofcom = telebot.types.InlineKeyboardButton('Pof.com | R$10,00', callback_data='pofcom')
    privalia = telebot.types.InlineKeyboardButton('Privalia | R$10,00', callback_data='privalia')
    protonmail = telebot.types.InlineKeyboardButton('Protonmail | R$10,00', callback_data='protonmail')
    recargapay = telebot.types.InlineKeyboardButton('Recargapay | R$10,00', callback_data='recargapay')
    shein = telebot.types.InlineKeyboardButton('Shein | R$10,00', callback_data='shein')
    shellbox = telebot.types.InlineKeyboardButton('Shellbox | R$10,00', callback_data='shellbox')
    shopee = telebot.types.InlineKeyboardButton('Shopee | R$10,00', callback_data='shopee')
    signal = telebot.types.InlineKeyboardButton('Signal | R$10,00', callback_data='signal')
    spaten = telebot.types.InlineKeyboardButton('Spaten | R$10,00', callback_data='spaten')
    steam = telebot.types.InlineKeyboardButton('Steam | R$10,00', callback_data='steam')
    tick = telebot.types.InlineKeyboardButton('Tick | R$10,00', callback_data='tick')
    tiktok = telebot.types.InlineKeyboardButton('Tiktok | R$10,00', callback_data='tiktok')
    tinder = telebot.types.InlineKeyboardButton('Tinder | R$10,00', callback_data='tinder')
    trembet = telebot.types.InlineKeyboardButton('Trembet | R$10,00', callback_data='trembet')
    twitter = telebot.types.InlineKeyboardButton('Twitter | R$10,00', callback_data='twitter')
    ultragaz = telebot.types.InlineKeyboardButton('Ultragaz | R$10,00', callback_data='ultragaz')
    viber = telebot.types.InlineKeyboardButton('Viber | R$10,00', callback_data='viber')
    vivo = telebot.types.InlineKeyboardButton('Vivo | R$10,00', callback_data='vivo')
    vkcom = telebot.types.InlineKeyboardButton('Vk.com | R$10,00', callback_data='vkcom')
    voltz = telebot.types.InlineKeyboardButton('Voltz | R$10,00', callback_data='voltz')
    xadrezfeliz = telebot.types.InlineKeyboardButton('Xadrezfeliz | R$10,00', callback_data='xadrezfeliz')
    yahoo = telebot.types.InlineKeyboardButton('Yahoo | R$10,00', callback_data='yahoo')
    ze_delivery = telebot.types.InlineKeyboardButton('Ze delivery | R$10,00', callback_data='ze_delivery')
    cassino_bet = telebot.types.InlineKeyboardButton('Cassino bet | R$10,00', callback_data='cassino_bet')
    next_app = telebot.types.InlineKeyboardButton('Next | R$10,00', callback_data='next')
    app_99 = telebot.types.InlineKeyboardButton('App 99 | R$10,00', callback_data='app_99')
    google = telebot.types.InlineKeyboardButton('Google | R$10,00', callback_data='google')
    facebook = telebot.types.InlineKeyboardButton('Facebook | R$10,00', callback_data='facebook')
    uber = telebot.types.InlineKeyboardButton('Uber | R$10,00', callback_data='uber')
    telegram = telebot.types.InlineKeyboardButton('Telegram | R$10,00', callback_data='telegram')
    picpay = telebot.types.InlineKeyboardButton('Picpay | R$10,00', callback_data='picpay')
    whatsapp = telebot.types.InlineKeyboardButton('Whatsapp | R$10,00', callback_data='whatsapp')
    outro = telebot.types.InlineKeyboardButton('Outros | R$10,00', callback_data='outro')
    markup.add(agibank, airbnb, aliexpress, amazon, aposta_ganha, apple, astropay, badoo, baidu, banqi, bet365, bitso, blablacar, brahma, budweiser, yowin, celcoin, cloudbet, corona, cumbuca, daki, didi, discord, dotz, ebay, facily, foodpanda, get_response, gov, gurubets, icecasino, icq, ifood, indriver, instagram, iti, kwai, linkedin, meliuz, mercado_livre, microsoft, naver, neon, netflix, nike, nubank, olx, openai, pagsmile, paypal, pofcom, privalia, protonmail, recargapay, shein, shellbox, shopee, signal, spaten, steam, tick, tiktok, tinder, trembet, twitter, ultragaz, viber, vivo, vkcom, voltz, xadrezfeliz, yahoo, ze_delivery, cassino_bet, next_app, app_99, google, facebook, uber, telegram, picpay, whatsapp, outro)
    bot.send_message(mensagem.chat.id, text='Escolha um dos serviços abaixo:', reply_markup=markup)

@bot.message_handler(func=verificar)
def answer(mensagem):
    texto = f"""
        Olá {mensagem.from_user.first_name + ' ' +  mensagem.from_user.last_name}, seja bem-vindo ao sms-bot!

Para fazer sua verificação primeiro faça o cadastro e depois escolha um serviço.

/cadastro
/servicos
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    with app.app_context():
        usuario = Usuario.query.filter_by(id_telegram=f'{callback.from_user.id}').first()
    if not usuario:
        bot.send_message(callback.message.chat.id, 'Antes de solicitar um serviço, por favor, faça o /cadastro.')
    else:
        bot.send_message(callback.message.chat.id, 'O número sera liberado após o pagamento.')
        bot.send_message(callback.message.chat.id, "Chave Pix:")
        bot.send_message(callback.message.chat.id, gerar_cobranca_pix(nome=usuario.nome, cpf=usuario.cpf, valor=9.99))
        bot.send_photo(callback.message.chat.id, photo=open('qrCodeImage.png', 'rb'))
        #while verificacao == false:
            # verificacao = atualizar
            #time.sleep(5);
        if callback.message:
            if callback.data == 'agibank':
                            # pegar_numero(chat=callback.message.chat.id, servico='sa')
                            pass
            elif callback.data == 'airbnb':
                            # pegar_numero(chat=callback.message.chat.id, servico='uk')
                            pass
            elif callback.data == 'aliexpress':
                            # pegar_numero(chat=callback.message.chat.id, servico='hx')
                            pass
            elif callback.data == 'amazon':
                            # pegar_numero(chat=callback.message.chat.id, servico='am')
                            pass
            elif callback.data == 'aposta_ganha':
                            # pegar_numero(chat=callback.message.chat.id, servico='ml')
                            pass
            elif callback.data == 'apple':
                            # pegar_numero(chat=callback.message.chat.id, servico='wx')
                            pass
            elif callback.data == 'astropay':
                            # pegar_numero(chat=callback.message.chat.id, servico='gr')
                            pass
            elif callback.data == 'badoo':
                            # pegar_numero(chat=callback.message.chat.id, servico='qv')
                            pass
            elif callback.data == 'baidu':
                            # pegar_numero(chat=callback.message.chat.id, servico='li')
                            pass
            elif callback.data == 'banqi':
                            # pegar_numero(chat=callback.message.chat.id, servico='vc')
                            pass
            elif callback.data == 'bet365':
                            # pegar_numero(chat=callback.message.chat.id, servico='ie')
                            pass
            elif callback.data == 'bitso':
                            # pegar_numero(chat=callback.message.chat.id, servico='ht')
                            pass
            elif callback.data == 'blablacar':
                            # pegar_numero(chat=callback.message.chat.id, servico='ua')
                            pass
            elif callback.data == 'brahma':
                            # pegar_numero(chat=callback.message.chat.id, servico='sy')
                            pass
            elif callback.data == 'budweiser':
                            # pegar_numero(chat=callback.message.chat.id, servico='zt')
                            pass
            elif callback.data == 'yowin':
                            # pegar_numero(chat=callback.message.chat.id, servico='sm')
                            pass
            elif callback.data == 'celcoin':
                            # pegar_numero(chat=callback.message.chat.id, servico='ix')
                            pass
            elif callback.data == 'cloudbet':
                            # pegar_numero(chat=callback.message.chat.id, servico='jn')
                            pass
            elif callback.data == 'corona':
                            # pegar_numero(chat=callback.message.chat.id, servico='om')
                            pass
            elif callback.data == 'cumbuca':
                            # pegar_numero(chat=callback.message.chat.id, servico='ahh')
                            pass
            elif callback.data == 'daki':
                            # pegar_numero(chat=callback.message.chat.id, servico='ahi')
                            pass
            elif callback.data == 'didi':
                            # pegar_numero(chat=callback.message.chat.id, servico='xk')
                            pass
            elif callback.data == 'discord':
                            # pegar_numero(chat=callback.message.chat.id, servico='ds')
                            pass
            elif callback.data == 'dotz':
                            # pegar_numero(chat=callback.message.chat.id, servico='cj')
                            pass
            elif callback.data == 'ebay':
                            # pegar_numero(chat=callback.message.chat.id, servico='dh')
                            pass
            elif callback.data == 'facily':
                            # pegar_numero(chat=callback.message.chat.id, servico='alc')
                            pass
            elif callback.data == 'foodpanda':
                            # pegar_numero(chat=callback.message.chat.id, servico='nz')
                            pass
            elif callback.data == 'get_response':
                            # pegar_numero(chat=callback.message.chat.id, servico='ala')
                            pass
            elif callback.data == 'gov':
                            # pegar_numero(chat=callback.message.chat.id, servico='afe')
                            pass
            elif callback.data == 'gurubets':
                            # pegar_numero(chat=callback.message.chat.id, servico='ik')
                            pass
            elif callback.data == 'icecasino':
                            # pegar_numero(chat=callback.message.chat.id, servico='dq')
                            pass
            elif callback.data == 'icq':
                            # pegar_numero(chat=callback.message.chat.id, servico='iq')
                            pass
            elif callback.data == 'ifood':
                            # pegar_numero(chat=callback.message.chat.id, servico='pd')
                            pass
            elif callback.data == 'indriver':
                            # pegar_numero(chat=callback.message.chat.id, servico='rl')
                            pass
            elif callback.data == 'instagram':
                            # pegar_numero(chat=callback.message.chat.id, servico='ig')
                            pass
            elif callback.data == 'iti':
                            # pegar_numero(chat=callback.message.chat.id, servico='ad')
                            pass
            elif callback.data == 'kwai':
                            # pegar_numero(chat=callback.message.chat.id, servico='vp')
                            pass
            elif callback.data == 'linkedin':
                            # pegar_numero(chat=callback.message.chat.id, servico='tn')
                            pass
            elif callback.data == 'meliuz':
                            # pegar_numero(chat=callback.message.chat.id, servico='uy')
                            pass
            elif callback.data == 'mercado_livre':
                            # pegar_numero(chat=callback.message.chat.id, servico='cq')
                            pass
            elif callback.data == 'microsoft':
                            # pegar_numero(chat=callback.message.chat.id, servico='mm')
                            pass
            elif callback.data == 'naver':
                            # pegar_numero(chat=callback.message.chat.id, servico='nv')
                            pass
            elif callback.data == 'neon':
                            # pegar_numero(chat=callback.message.chat.id, servico='aex')
                            pass
            elif callback.data == 'netflix':
                            # pegar_numero(chat=callback.message.chat.id, servico='nf')
                            pass
            elif callback.data == 'nike':
                            # pegar_numero(chat=callback.message.chat.id, servico='ew')
                            pass
            elif callback.data == 'nubank':
                            # pegar_numero(chat=callback.message.chat.id, servico='aaa')
                            pass
            elif callback.data == 'olx':
                            # pegar_numero(chat=callback.message.chat.id, servico='sn')
                            pass
            elif callback.data == 'openai':
                            # pegar_numero(chat=callback.message.chat.id, servico='dr')
                            pass
            elif callback.data == 'pagsmile':
                            # pegar_numero(chat=callback.message.chat.id, servico='gg')
                            pass
            elif callback.data == 'paypal':
                            # pegar_numero(chat=callback.message.chat.id, servico='ts')
                            pass
            elif callback.data == 'pof.com':
                            # pegar_numero(chat=callback.message.chat.id, servico='pf')
                            pass
            elif callback.data == 'privalia':
                            # pegar_numero(chat=callback.message.chat.id, servico='afs')
                            pass
            elif callback.data == 'protonmail':
                            # pegar_numero(chat=callback.message.chat.id, servico='dp')
                            pass
            elif callback.data == 'recargapay':
                            # pegar_numero(chat=callback.message.chat.id, servico='xu')
                            pass
            elif callback.data == 'shein':
                            # pegar_numero(chat=callback.message.chat.id, servico='aez')
                            pass
            elif callback.data == 'shellbox':
                            # pegar_numero(chat=callback.message.chat.id, servico='vg')
                            pass
            elif callback.data == 'shopee':
                            # pegar_numero(chat=callback.message.chat.id, servico='ka')
                            pass
            elif callback.data == 'signal':
                            # pegar_numero(chat=callback.message.chat.id, servico='bw')
                            pass
            elif callback.data == 'spaten':
                            # pegar_numero(chat=callback.message.chat.id, servico='ky')
                            pass
            elif callback.data == 'steam':
                            # pegar_numero(chat=callback.message.chat.id, servico='mt')
                            pass
            elif callback.data == 'tick':
                            # pegar_numero(chat=callback.message.chat.id, servico='rb')
                            pass
            elif callback.data == 'tiktok':
                            # pegar_numero(chat=callback.message.chat.id, servico='lf')
                            pass
            elif callback.data == 'tinder':
                            # pegar_numero(chat=callback.message.chat.id, servico='oi')
                            pass
            elif callback.data == 'trembet':
                            # pegar_numero(chat=callback.message.chat.id, servico='abj')
                            pass
            elif callback.data == 'twitter':
                            # pegar_numero(chat=callback.message.chat.id, servico='tw')
                            pass
            elif callback.data == 'ultragaz':
                            # pegar_numero(chat=callback.message.chat.id, servico='afr')
                            pass
            elif callback.data == 'viber':
                            # pegar_numero(chat=callback.message.chat.id, servico='vi')
                            pass
            elif callback.data == 'vivo':
                            # pegar_numero(chat=callback.message.chat.id, servico='kx')
                            pass
            elif callback.data == 'vkcom':
                            # pegar_numero(chat=callback.message.chat.id, servico='vk')
                            pass
            elif callback.data == 'voltz':
                            # pegar_numero(chat=callback.message.chat.id, servico='eb')
                            pass
            elif callback.data == 'xadrezfeliz':
                            # pegar_numero(chat=callback.message.chat.id, servico='fa')
                            pass
            elif callback.data == 'yahoo':
                            # pegar_numero(chat=callback.message.chat.id, servico='mb')
                            pass
            elif callback.data == 'ze_delivery':
                            # pegar_numero(chat=callback.message.chat.id, servico='em')
                            pass
            elif callback.data == 'cassino_bet':
                            # pegar_numero(chat=callback.message.chat.id, servico='pc')
                            pass
            elif callback.data == 'next_app':
                            # pegar_numero(chat=callback.message.chat.id, servico='aey')
                            pass
            elif callback.data == 'app99':
                            # pegar_numero(chat=callback.message.chat.id, servico='ki')
                            pass
            elif callback.data == 'google':
                            # pegar_numero(chat=callback.message.chat.id, servico='go')
                            pass
            elif callback.data == 'facebook':
                            # pegar_numero(chat=callback.message.chat.id, servico='fb')
                            pass
            elif callback.data == 'uber':
                            # pegar_numero(chat=callback.message.chat.id, servico='ub')
                            pass
            elif callback.data == 'telegram':
                            # pegar_numero(chat=callback.message.chat.id, servico='tg')
                            pass
            elif callback.data == 'picpay':
                            # pegar_numero(chat=callback.message.chat.id, servico='ev')
                            pass
            elif callback.data == 'whatsapp':
                            # pegar_numero(chat=callback.message.chat.id, servico='wa')
                            pass
            elif callback.data == 'outro':
                            # pegar_numero(chat=callback.message.chat.id, servico='ot')
                            pass

bot.polling()