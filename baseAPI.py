from flask import Flask, redirect, url_for, request
from cryptography.fernet import Fernet
#import encDcrp

app = Flask(__name__)

#encDecryptHandler = encDcrp()
#encDecryptHandler.setup()
plainText = "hello geeks"
key = Fernet.generate_key()
fernet = Fernet(key) 

@app.route('/')
def defaultpath():
   return 'welcome to Home page' 

@app.route('/encryption/')
def encryption():
   return  'welcome to enc page' 

@app.route('/decryption/')
def decryption():
   return  "welcome to decrypyion"

@app.route('/encrypt')
def encrypt():
    msg = request.args.get('text')
    option = request.args.get('option')

    encMessage = fernet.encrypt(msg.encode())
    print("original string: ", msg)
    print("encrypted string: ", encMessage)

    return '''<h1>The text value is: {}</h1>
              <h1>The encrypted value is: {}</h1>
              <h1>The option value is: {}'''.format(msg, encMessage, option)

@app.route('/decrypt')
def decrypt():
    encMsg = request.args.get('text')
    option = request.args.get('option')
    txttoByte = encMsg.encode()

    dcrMessage = fernet.decrypt(txttoByte).decode()
    print("decrypted string: ", dcrMessage)

    return '''<h1>The text value is: {}</h1>
              <h1>The decrypted value is: {}</h1>
              <h1>The option value is: {}'''.format(encMsg, dcrMessage, option)

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/aes-encryption')
def aesencryption():
    text = request.args.get('text')
    key =  request.args.get('key')
    option = request.args.get('option')

    return '''<h1>The text value is: {}</h1>
              <h1>The key value is: {}</h1>
              <h1>The option value is: {}'''.format(text, key, option)

@app.route('/aes-decryption')
def aesdecryption():
    text = request.args.get('text')
    key =  request.args.get('key')
    option = request.args.get('option')

    return '''<h1>The text value is: {}</h1>
              <h1>The key value is: {}</h1>
              <h1>The option value is: {}'''.format(text, key, option)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host='0.0.0.0')