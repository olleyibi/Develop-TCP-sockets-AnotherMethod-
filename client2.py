def encrypt(message):
    encrypt = ""
    for i in message:
        position = alphabet.find(i)
        newposition = (position+key)%len(alphabet)
        encrypt += alphabet[newposition]
    message = encrypt
    return message



def decrypt(message):
    decrypt = ""
    for i in message:
        position = alphabet.find(i)
        newposition = (position-key)%len(alphabet)
        decrypt += alphabet[newposition]
    message = decrypt
    return message

def nucleotide_check(codon):
    if codon != "DISCONNECT":
        for i in codon:
            if i not in ("T","C","G","A"):
                codon = "DISCONNECT"
                break
        return codon
    else:
        return codon



import socket

file = input("File: ")
if file:
    with open (file,"r") as file_inp:
        content = file_inp.readline
else:
    while True:
        respond = input("Enter YES/NO: ")
        if respond.upper() ==  "YES":
            new_res = input("Enter 'START RNA': ")
            if new_res.upper() == "START RNA":
                codon_mes = input("Enter RNA String: ").upper()
                if len(codon_mes)%3 == 0:
                    codon_mes = nucleotide_check(codon_mes)
                    break
                else:
                    codon_mes = "DISCONNECT"
                
            else:
                print("Wrong entry")
        else:
            codon_mes = "DISCONNECT"
            break





hostname = socket.gethostbyname(socket.gethostname())
port_number = 9999
c = socket.socket()
c_addr = (hostname,port_number)
c.connect(c_addr)

codon_mes = codon_mes.encode("utf-8")
message_length = len(codon_mes)
message_length = str(message_length).encode("utf-8")
message_length += b" " * (64 - len(message_length))
c.send(message_length)
c.send(codon_mes)
print(c.recv(1024).decode("utf-8"))
input("Press <Enter> to exit")