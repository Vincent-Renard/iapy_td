#! /usr/bin/env python3
# coding: utf-8


def base_regles():
    regles = [
        ([('panneau', 'ecole')], ('prox_etab', 'vrai')),
        ([('panneau_vit', 30)], ('limit_vit', 'vrai')),
        ([('meteo', 'pluie')], ('mauv_visib', 'vrai')),
        ([('meteo', 'neige')], ('chaussee_glissante', 'vrai')),
        ([('mauv_visib', 'vrai')], ('danger', 'vrai')),
        ([('chaussee_glissante', 'vrai')], ('danger', 'vrai')),
        ([('lieu', 'en_ville'), ('type_veh', 'leger'),
          ('limit_vit', 'faux'), ('prox_etab', 'faux'),
          ('danger', 'faux')], ('vitesse', 50)),
        ([('lieu', 'en_ville'), ('type_veh', 'leger'),
          ('limit_vit', 'faux'), ('prox_etab', 'faux'),
          ('danger', 'vrai'), ('vitesse', 40)]),
        ([("lieu", "en_ville"), ("type_veh", "leger"),
          ("limit_vit", 'vrai'), ("panneau_vit", 30),
          ("prox_etab", 'faux'), ("danger", 'faux')],
         ("vitesse", 30))]

    br = {}
    for regle in regles:
        if regle[1] in br:
            br[regle[1]].append(regle[0])
        else:
            br[regle[1]] = [regle[0]]
    print(br)
    return br
