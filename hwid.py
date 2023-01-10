#simple hwid system
import os, requests, getpass, uuid, hashlib, getmac as gma


hwid = str(hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest())

if hwid not in requests.get('https://pastebin.com/z7QBLLD4').text:
        exit()

#requeriments
#pip install getmac
#pip install requests
#pip install uuid
