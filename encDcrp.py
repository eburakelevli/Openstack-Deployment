

from cryptography.fernet import Fernet

plainText = "hello geeks"
key = Fernet.generate_key()
fernet = Fernet(key) 

def setup():
    plainText = "hello geeks"
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print("i am in setup")

def encrypt(msg):
    if(msg == ""):
        msg = plainText
    encMessage = fernet.encrypt(msg.encode())
    print("original string: ", msg)
    print("encrypted string: ", encMessage)
    return encMessage

def decrypt(encMsg):
    dcrMessage = fernet.decrypt(encMsg).decode()
    print("decrypted string: ", dcrMessage)

print('Key = ' + str(key))
result1 = encrypt(" Hello, welcome to encryption ")
print(type(result1))

totext = result1.decode()
print(type(totext))
print("encrypted to string: ", totext)

tobyte = totext.encode()
print(type(tobyte))
print("encrypted to byte: ", tobyte)

decrypt(result1)

#print(type(result1))
#testing 
testmsg =  b'gAAAAABjp4izQOitfIQME9UTQV_9ArQgtAey0eV62INrcBCQw3wYbrEqH_MMAtxD8E0DLyic9UNVni-SyVHbcH5mj5jS_wceB8uZyEtoB1jRrMCNu5Rrih4='

if(tobyte == result1):
    print('same')


#decrypt(testmsg)

