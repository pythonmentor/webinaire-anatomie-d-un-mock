def une_autre_fonction_de_mon_code():
    pass


def ma_fonction_a_tester():
    # ...
    element = (
        une_autre_fonction_de_mon_code()
    )  # je mocke les dépendances internes au projet
    print()  # pas de mock
    une_liste.append(1)  # pas de mock: objet et méthode standard
    elements_aleatoire = random.sample(
        une_liste, 3
    )  # je mocke pour rendre l'appel à random.sample() prédictif
    response = requests.get(
        url
    )  # je mocke parce que l'api peut être indisponible et que c'est lent
    cursor.execute(
        sql
    )  # je mocke parce que la db peut être indisponible et que c'est lent
    mon_query_set = MonModel.objects.filter(
        ...
    )  # je mocke les dépendances internes au projet
    # ...
