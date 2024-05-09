import requests
from Crypto.Cipher import DES, AES

API_KEY = ""
#test()


def test():
    #print(API_KEY)
    #if test
    requests.get("https://www.google.com")



cipher = DES.new(API_KEY)
def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message)) # BAD: weak encryption