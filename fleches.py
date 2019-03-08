#! /usr/bin/env python3
# coding: utf-8


init = (0, 0, 0, 1, 0, 1)
final = (1, 1, 1, 1, 1, 1)


def is_final(etat):
    return equals(etat, final)


def nb_paires_1(etat):
    paires_1 = 0
    i = 0
    prec = 2
    for l in etat:
        i += 1
        if i % 2 == 0:
            if prec == l == 1:
                paires_1 += 1
        else:
            prec = l
    return paires_1


def nb_1(etat): return sum(etat)


def nb_0(etat): return len(etat) - nb_1(etat)


def permute(fleche): return (fleche + 1) % 2


def action_i(pos, state):
    s = []
    n = 0
    for i in state:
        if n == pos or (n > 0 and n - 1 == pos):

            s.append(permute(i))
        else:
            s.append(i)
        n += 1
    return tuple(s), 1


def actions(etat):
    return [action_i(i, etat) for i in range(len(etat) - 1)]


def equals(s1, s2):
    for i in range(s1):
        if s1[i] != s2[i]: return False
    return True


def deja_vu(state, path):
    for node in path:
        if equals(state, node):
            return True
    return False


def get_chemin(noeud):
    return noeud[1]


def get_state(noeud):
    return noeud[0]


def action(): return [actions]


def afficher_sol(noeud):
    print("Soluce : ")
    path = get_chemin(noeud)
    for i in path:
        print(get_state(i))
    print(get_state(noeud))
    print(len(path) + 1)


def getCout(node):
    return node[2]


def heuristic(etat):
    return len(etat - nb_1(etat) / 2)


def ensSuivant(noeud):
    ls = []
    for act in action():
        liste_suivante = act(get_state(noeud))
        for e in liste_suivante:
            etat_suivant = get_state(e)
            cout_action = get_chemin(e)
            if not deja_vu(etat_suivant, get_chemin(noeud)):
                next_path = list(get_chemin(noeud))
                next_path.append(noeud)
                ls.append((etat_suivant, next_path, cout_action + getCout(noeud), heuristic(etat_suivant)))
    return ls


def a_star(liste_att):
    while liste_att:
        node = liste_att.pop()
        if is_final(get_state(node)):
            afficher_sol(node)
            return True
        liste_suivante = ensSuivant(node)
        liste_att.extend(liste_suivante)
        liste_att.sort(key=lambda elt: elt[2] + elt[3], reverse=True)


if __name__ == '__main__':
    print(actions(init))
    print(ensSuivant(init))
