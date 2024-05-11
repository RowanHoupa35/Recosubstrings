def RechercheForceBrute(chaine, sousChaine):
    longueurChaine = len(chaine)
    longueurSousChaine = len(sousChaine)

    for i in range(longueurChaine - longueurSousChaine + 1):
        sousChaineTrouvee = True

        for j in range(longueurSousChaine):
            if chaine[i + j] != sousChaine[j]:
                sousChaineTrouvee = False
                break

        if sousChaineTrouvee:
            print("Correspondance trouvée à l'indice:", i)
            return True

    print("Aucune correspondance trouvée.")
    return False


# Exemple d'utilisation
chaine = "nobodynoticed"
sousChaine = "not"
RechercheForceBrute(chaine, sousChaine)
