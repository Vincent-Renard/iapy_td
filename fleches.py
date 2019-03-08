#! /usr/bin/env python3
# coding: utf-8


init = (0, 0, 0, 1, 0, 1)
final = (1, 1, 1, 1, 1, 1)


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


def permute(fleche): return fleche + 1 % 2


def action_i(pos, state):
    s = []
    n = 0
    for i in state:
        if n == pos or n - 1 == pos:
            s[n] = permute(i)
        n += 1
    return tuple(s)


def actions(state):
    l = []
    for i in range(len(state)):
        l.append(action_i(i, state))
    return l


if __name__ == '__main__':
    pass
