def Cesar(alp, chaine, cle):
    chaineAchainer = chaine.replace(" ","").upper()
    chaineChainee = ""
    for i in range(0,len(chaineAchainer)):
        for j in range(0,len(alp)):
            if chaineAchainer[i] == alp[j]:
                chaineChainee += alp[(j+cle) % len(alp)]
    return chaineChainee




alp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chaine = str(input("Entrez votre message à coder : "))
cle = int(input("Entrez la clé : "))
print(Cesar(alp,chaine,1))
