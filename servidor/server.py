from flask import Flask, jsonify, request
import ssl, json

app = Flask(__name__)

@app.route('/', methods=["POST"])
def imprimir():
    response = {"status": 200}
    return jsonify(response)

@app.route('/pix', methods=["POST"])
def imprimirPix():
    imprime = print(request.json)
    data = request.json
    with open('data.txt', 'a') as outfile:
        outfile.write("\n")
        json.dump(data, imprime)
    return jsonify(imprime)

if __name__ == "__main__":
  context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
  context.verify_mode = ssl.CERT_REQUIRED
  context.load_verify_locations('./chain-pix-prod.crt')
  context.load_cert_chain(
      './certchain.pem',
        './certprivkey.pem') #'/etc/letsencrypt/live/example.com/fullchain.pem' #'/etc/letsencrypt/live/example.com/privkey.pem'
  app.run(host='0.0.0.0', ssl_context=context) 
