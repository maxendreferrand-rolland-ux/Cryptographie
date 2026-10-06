def aplatirListe(listeImbrique):
    if len(listeImbrique) == 0:
        return []

    premier = listeImbrique[0]
    reste = listeImbrique[1:]

    if isinstance(premier, list):
        return aplatirListe(premier) + aplatirListe(reste)
    else:
        return [premier] + aplatirListe(reste)
#-----------------------------------------------
#-----------------OU----------------------------
#-----------------------------------------------
def aplatir(listeImbrique):
    if len(listeImbrique) == 0:
        return []

    premier = listeImbrique
    reste = listeImbrique[1:]

    try:
        len(premier)

        return aplatir_sans_isinstance(premier) + aplatir_sans_isinstance(reste)

    except TypeError:
        return [premier] + aplatir_sans_isinstance(reste)


test = [1,[2,[3,[4,5,[6]]]]]
print(aplatirListe(test))