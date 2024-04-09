def n_høyeste(liste: list[int], n:int):
    høyeste_n = []
    for i in range(n):
        høyest = max(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n

