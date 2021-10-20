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

import csv
import socket
hostname = socket.gethostbyname(socket.gethostname())
port_number = 9999
s = socket.socket()
s_addr = (hostname,port_number)
s.bind(s_addr)
s.listen(10)


def codon_list(file):
    import csv
    global c_groups
    global amino
    c_groups = []
    amino = []
    with open(file) as file:
        read = csv.reader(file, delimiter=',')
        tally = 0
        for i in read:
            if tally == 0:
                tally += 1
            else:
                c_groups.append(i[0])
                amino.append(i[1])





clientcon,adr = s.accept()
print(adr[0])

while True:
    info = clientcon.recv(64).decode("utf-8")
    
    if info:
        info = int(info)
        info_con = clientcon.recv(info).decode("utf-8")
        if info_con == "DISCONNECT":
            break
        else:
            codon_list("codon-aminoacid.csv")
            old = info_con[0:3]
            new = info_con[0:3]
            check = ""
            for i in range(len(c_groups)):
                if (c_groups[i] == new):
                    check = amino[i]
            for j in range(len(amino)):
                if (amino[j] == check and c_groups[j] != new):
                    new = c_groups[j]
                    new = new[::-1]
                    break
            info_con = info_con.replace(old,new)
            if info_con == "DISCONNECT":
                clientcon.close()
            else:
                clientcon.send(f"Answer: {info_con}".encode("utf-8"))