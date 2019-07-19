import re
import os

text = False
results = []
#path = 'C:/Users/jerem/Desktop/MysticNights/@MYSTICNIGHTS.ISO/'
path = input("Enter search path : ")
target = input("Enter search target : ")
b_euckor = target.encode('euc-kr')
b_utf8 = target.encode('utf-8')

for root, dirs, files in os.walk(path):
     for file in files:
        with open(os.path.join(root, file), "rb") as data:
            buffer = data.read()  # read content
        #text = re.search(b'\x4d\x45\x4d\x4f\x52\x59\x20\x43\x41\x52\x44\x20\x73\x6c\x6f\x74\x20\x31', buffer, re.MULTILINE)
        text_kor = re.search(b_euckor, buffer, re.MULTILINE)
        text = re.search(b_utf8, buffer, re.MULTILINE)
        if text or text_kor:
            results.append(os.path.join(root,file))

if results.__len__()!=0:
    if results.__len__() ==1:
        print(f"{results.__len__()} MATCH FOUND.")
    else:
        print(f"{results.__len__()} MATCHES FOUND.")
    print(results)
else:
    print("NO MATCHES FOUND...")

