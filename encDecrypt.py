

from cryptography.fernet import Fernet

def setup():
    plainText = "hello geeks"
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print("i am up")

def encrypt(msg):
    if(msg == ""):
        msg = message
    encMessage = fernet.encrypt(message.encode())
    print("original string: ", message)
    print("encrypted string: ", encMessage)
    return encMessage



mmsg = encrypt()

decMessage = fernet.decrypt(mmsg).decode()

print("decrypted string: ", decMessage)

from Crypto.Cipher import AES
#from Crypto import Random

key = ''.join(chr(Random.randint(0, 0xFF)) for i in range(16))
print('key', [x for x in key])
# prints
key ['+', 'Y', '\xd1', '\x9d', '\xa0', '\xb5', '\x02', '\xbf', ';', '\x15', '\xef', '\xd5', '}', '\t', ']', '9']

aes = AES.new(key, AES.MODE_CBC, iv)
data = 'hello world 1234' # <- 16 bytes
encd = aes.encrypt(data)

aes = AES.new(key, AES.MODE_CBC, iv)
decd = adec.decrypt(encd)
print(decd)



decMessage = Fernet.decrypt(mmsg.decode())

print("decrypted string: ", decMessage)
