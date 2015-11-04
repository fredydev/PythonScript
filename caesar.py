import os
cle=int(input("choisir cle : "))
os.system("sleep 2")
#fichier = open("texte.txt", "r")
#texte_clair=fichier.read()
texte_clair=input("Entrer texte")
os.system("sleep 1")
texte_chiffre=""
for i in range(0,len(texte_clair)):
    if 97<=ord(texte_clair[i])<=122:
       coder=chr((((ord(texte_clair[i])-97)+cle)%26)+97)
       texte_chiffre=texte_chiffre+coder
    elif 65<=ord(texte_clair[i])<=90:
       coder=chr((((ord(texte_clair[i])-65)+cle)%26)+65)
       texte_chiffre=texte_chiffre+coder
    elif 30<=ord(texte_clair[i])<=64:
       coder=chr(ord(texte_clair[i]))
       texte_chiffre=texte_chiffre+coder
    else:
        texte_chiffre=texte_chiffre+"(FX)"
print(texte_chiffre)
