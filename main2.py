#! /usr/bin/env python3
# coding: utf-8
# Viren
# 15/02/19


def initial():
    """Cree et retourne l'etat initial"""
    return [3, 3, 1]


def final(state):
    """Teste si un etat est valide"""
    return state[0] == 0 and state[1] == 0 and state[2] == 0
    # return state==[0,0,0]


def actions():
    return [aller, retour]


def aller(actual_state):
    [c, m, p] = actual_state
    psbl = []
    if p == 0:
        return psbl
    for hungry_men in range(0, c + 1):
        for christians in range(0, m + 1):
            # 1 condolier et pas plus de 2 personnes dans la pirogue if 0 <= hungry_men+christians < 3 and ((
            # m-christians >= c-hungry_men) or (m-christians==0)) and (3-m+christians)==0:

            if 0 <= hungry_men + christians < 3 and ((m - christians >= c - hungry_men) or (m - christians == 0)) and (
                    (3 - c + hungry_men) <= (3 - m + christians) or 3 - m + christians) == 0:
                psbl.append([c - hungry_men, m - christians, p - 1])

    return psbl


def retour(actual_state):
    [c, m, p] = actual_state
    psbl = []
    if p == 1:
        return psbl
    for hungry_men in range(0, c + 1):
        for christians in range(0, m + 1):
            # 1 condolier et pas plus de 2 personnes dans la pirogue
            #            if 0 <= hungry_men+christians < 3 and ((m-christians >= c-hungry_men) or (m-christians==0)) and (3-m+christians)==0:
            # 0 <= hungry_men + christians < 3 and ((m + christians >= c + hungry_men) or (m + christians == 0)) and ((3 - c + hungry_men) <= (3 - m - christians) or 3 - m - christians) == 0:

            if 3 > hungry_men + christians >= 0 == (
                    (3 - c + hungry_men) <= (3 - m - christians) or 3 - m - christians) and (
                    (m + christians >= c + hungry_men) or (m + christians == 0)):
                psbl.append([c + hungry_men, m + christians, p + 1])

    return psbl


def get_chemin(noeud):
    return noeud[1]


def get_state(noeud):
    return noeud[0]


def deja_vu(state, path):
    for node in path:
        if get_state(node) == state:
            return True
    return False


def afficher_sol(noeud):
    print("Solution : ")
    path = get_chemin(noeud)
    for node_i in path:
        print(get_state(node_i))
    print(get_state(noeud))
    print("Longeur : " + str(len(path) + 1))


def noeuds_fils(noeud):
    return [c for c in get_chemin(noeud) if not deja_vu(get_state(c), get_chemin(c))]


def noeuds_fils_II(noeud):
    """Correction"""
    ls = []
    for action in actions():
        liste_suivants = action(get_state(noeud))
        for etat_suivant in liste_suivants:
            if not deja_vu(etat_suivant, get_chemin()):
                next_path = list(get_chemin(noeud))
                next_path.append(noeud)
                ls.append((etat_suivant, next_path))
    return ls


def rp(noeud):
    if final(get_state(noeud)):
        afficher_sol(noeud)
        return True
    else:
        liste_suivante = noeuds_fils_II(noeud)
        if not liste_suivante:
            return False
        for suiv in liste_suivante:
            if rp(suiv):
                return True
        return False


def approf_succ(noeud):
    pass


if __name__ == '__main__':
    rp((initial(), []))
