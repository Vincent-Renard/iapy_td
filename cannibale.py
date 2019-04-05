#! /usr/local/bin/python
# -*- coding: utf_8 -*-

def initial():
    return [3, 3, 1]


def final(etat):
    if etat == [0, 0, 0]:
        return True
    return False


def actions():
    return [allez, retour]


def allez(etat):
    print("etat", etat)
    c, m, b = etat[0]

    if b == 0:
        return []

    listSuiv = []
    for i in range(0, c + 1):
        for j in range(0, m + 1):
            if (1 <= (i + j) <= 2 and ((m - j >= c - i) or (m - j == 0)) and (
                    (3 - c + i) <= (3 - m + j) or (3 - m + j) == 0)):
                listSuiv.append([c - i, m - j, 0])
        return listSuiv


def retour(etat):
    print(etat)
    [c, m, b] = etat[0]
    if b == 1:
        return []

    listSuiv = []
    for i in range(0, (3 - c) + 1):
        for j in range(0, (3 - m) + 1):
            if (1 <= (i + j) <= 2 and ((m + j >= c + i) or (m + j == 0)) and (
                    (3 - c - i) <= (3 - m - j) or (3 - m - j) == 0)):
                listSuiv.append([c + i, m + j, 1])
        return listSuiv


def afficher_sol(noeud):
    print("Solution :");
    chemin = getChemin(noeud);
    for i in chemin:
        print(getEtat(i));
    print(getEtat(noeud));
    print("Longueur : " + str(len(chemin) + 1));


def getChemin(noeud):
    return noeud[1]


def getEtat(noeud):
    return noeud[0]


def dejavu(etat, chemin):
    for noeud in chemin:
        state = getEtat(noeud)

        if etat[0] == state[0] and etat[1] == state[1] and etat[2] == state[2]:
            return True;
    return False;


def noeudsFils(noeud): #return [c for c in getChemin(noeud) if not dejavu(getEtat(c), getChemin(c))]

    ls = []
    for action in actions():
        listSuiv = action(getEtat(noeud))
        for etatSuiv in listSuiv:
            if not dejavu(etatSuiv, getChemin(noeud)):
                chemSuiv = list(getChemin(noeud))
                chemSuiv.append(noeud)
                print("not deja vu")
                ls.append((etatSuiv, chemSuiv))
    return ls



def rp_rec(noeud):
    if final(getEtat(noeud)):
        afficher_sol(noeud);
        return True;
    else:
        listSuiv = noeudsFils(noeud);

        if not listSuiv:
            print(1)
            return False;
        for suiv in listSuiv:
            if rp_rec(suiv):
                return True;

        print(2)
        return False


def rp_itt(noeud):
    if final(getEtat(noeud)):
        afficher_sol(noeud)
        return True
    else:
        listSuiv = noeudsFils(noeud)
        if not listSuiv:
            return False
        for suiv in listSuiv:
            if final(getEtat(suiv)):
                afficher_sol(suiv)
                return True


if __name__ == "__main__":
    noeudinitial = [initial(), []]

    print(rp_rec([noeudinitial]))
