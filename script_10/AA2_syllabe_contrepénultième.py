"""
auteur : Daniel Escoval
license : license UNIL
"""
import re

#Importation des autres scripts
# from vocalisme import Vocalisme
# vocalisme = Vocalisme()

# from vocalisme_non_tonique import VocalismeNonTonique
# vocalisme_non_tonique = VocalismeNonTonique()

# from consonantisme_initial import ConsonantismeInitial
# consonantisme_initial = ConsonantismeInitial()

# from consonantisme_final import ConsonantismeFinal
# consonantisme_final = ConsonantismeFinal()

from syllabifier import Syllabifier
syllabifier = Syllabifier()


#Listes de toutes les lettres traitées dans le script
listes_lettres = {
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú"],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'voyelles_palatales': ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í'],

'voyelles_vélaires' : ['O', "Ǫ", "Ọ", 'U', "Ú"],

'consonnes' : ['B', 'C', 'D', 'F', 'G', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z'],

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

'consonnes_liquides' : ["R", "L"],

'consonnes_nasales' : ["M", "N"],

'yod_et_wau' : ["W", "Y"],

'consonantisme_explosif_complexe_2_lettres' : [
'CB', 'DC', 'FB', 'GB', 'HB', 'LB', 'MB', 'NB', 'PB', 'RB', 'SB', 'TB', 'VB', 'YB',
'BC', 'DC', 'FC', 'GC', 'HC', 'LC', 'MC', 'NC', 'PC', 'RC', 'SC', 'TC', 'VC', 'YC',
'BD', 'CD', 'FD', 'GD', 'HD', 'LD', 'MD', 'ND', 'PD', 'RD', 'SD', 'TD', 'VD', 'YD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'HJ', 'LJ', 'MJ', 'NJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ', 'YJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'LL', 'ML', 'NL', 'PL', 'RL', 'SL', 'TL', 'VL', 'YL',
'BM', 'CM', 'DM', 'FM', 'GM', 'HM', 'LM', 'MM', 'NM', 'PM', 'RM', 'SM', 'TM', 'VM', 'YM',
'BN', 'CN', 'DN', 'FN', 'GL', 'HL', 'LN', 'MN', 'NN', 'PN', 'RN', 'SN', 'TN', 'VN', 'YN',
'BP', 'CP', 'DP', 'FP', 'GP', 'HP', 'LP', 'MP', 'NP', 'RP', 'SP', 'TP', 'VP', 'YP',
'BR', 'CR', 'DR', 'FR', 'GR', 'HR', 'LR', 'MR', 'NR', 'PR', 'RR', 'SR', 'TR', 'VR', 'YR',
'BS', 'CS', 'DS', 'FS', 'GS', 'HS', 'LS', 'MS', 'NS', 'PS', 'RS', 'SS', 'TS', 'VS', 'YS',
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'YT'
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'YY',
],

'consonantisme_implosif_complexe_2_lettres' : [
'CB', 'DC', 'FB', 'GB', 'HB', 'LB', 'MB', 'NB', 'PB', 'RB', 'SB', 'TB', 'VB', 'YB',
'BC', 'DC', 'FC', 'GC', 'HC', 'LC', 'MC', 'NC', 'PC', 'RC', 'SC', 'TC', 'VC', 'YC',
'BD', 'CD', 'FD', 'GD', 'HD', 'LD', 'MD', 'ND', 'PD', 'RD', 'SD', 'TD', 'VD', 'YD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'HJ', 'LJ', 'MJ', 'NJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ', 'YJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'LL', 'ML', 'NL', 'PL', 'RL', 'SL', 'TL', 'VL', 'YL',
'BM', 'CM', 'DM', 'FM', 'GM', 'HM', 'LM', 'MM', 'NM', 'PM', 'RM', 'SM', 'TM', 'VM', 'YM',
'BN', 'CN', 'DN', 'FN', 'GL', 'HL', 'LN', 'MN', 'NN', 'PN', 'RN', 'SN', 'TN', 'VN', 'YN',
'BP', 'CP', 'DP', 'FP', 'GP', 'HP', 'LP', 'MP', 'NP', 'RP', 'SP', 'TP', 'VP', 'YP',
'BR', 'CR', 'DR', 'FR', 'GR', 'HR', 'LR', 'MR', 'NR', 'PR', 'RR', 'SR', 'TR', 'VR', 'YR',
'BS', 'CS', 'DS', 'FS', 'GS', 'HS', 'LS', 'MS', 'NS', 'PS', 'RS', 'SS', 'TS', 'VS', 'YS',
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'YT'
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'YY',
],


'consonantisme_explosif_complexe_3_lettres' : [
'SBR', 'SCR', 'SPR', 'STR',
],

'préfixes' : ['AD', 'IM',],

}

class SyllabeContrepenultieme:

    def __init__(self):
        return

    def syllabe_contrepenultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Consoantisme initial
        if syllabes[-5][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B (occlusive labiale sonore)
            if syllabes[-5][0] == 'B':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'C':
                        changements.append('g')
                    elif syllabes[-5][1] == 'L':
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #Exceptionnellement, une séquence -BR- peut perdre son statut intervocalique et aboutir en position implosive secondaire
                            if syllabes[-6][-1] == 'Ę' and syllabes[-4][0] == 'Y':
                                changements.append('r')
                            else:
                                changements.append('vr')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'T':
                            changements.append('d')
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            changements.append(syllabes[-5][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if syllabes[-5][2] == 'A':
                                changements.append('g')
                            #En milieu vélaire
                            else:
                                changements.append('i')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-5][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #Spirantisation en milieu palaral
                        if syllabes[-5][1] in ['A', 'Á', 'Ẹ', 'Ę', 'E', 'Í']:
                            if syllabes[-4][-1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    elif syllabes[-5][-2] + syllabes[-5][-1] == 'ER' and syllabes[-4][1] == 'Í':
                        changements.append('v')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de C (occlusive palatale sourde)
            elif syllabes[-5][0] == 'C':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'L':
                        #L mouillé
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #Pas besoin de I s'il est présent dans la voyelle antéposée
                            if syllabes[-6][-1] in ['Ẹ', 'Í']:
                                changements.append('l')
                            else:
                                changements.append('il')
                        #Après S, la séquence se simplifie en L
                        elif syllabes[-6][-1] == 'S':
                            changements.append('l')
                        elif syllabes[-6][-1] == 'C':
                            changements.append('gl')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] in ['Í']:
                                changements.append('r')
                            elif syllabes[-6][-1] == 'Á':
                                changements.append('gr')
                            else:
                                changements.append('ir')
                        elif syllabes[-6][-1] in ['R', 'S']:
                            changements.append('tr')
                        #Si un Y est antéposé inorganiquement
                        elif syllabes[-6][-1] == 'Y':
                            changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #Deuxième lettre = T
                    elif syllabes[-5][1] == 'T':
                        changements.append(syllabes[-5][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            if syllabes[-5][2] == 'A':
                                changements.append('qu')
                            else:
                                changements.append(syllabes[-5][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('s')
                        else:
                            #Ajout d'un signe diacritique devant A et O
                            if syllabes[-5][-1] in ['C', 'M', 'N']:
                                changements.append('c')
                            #Avancement du point d'articulation
                            elif syllabes[-4][-1] == 'D':
                                changements.append('g')
                            #Ajout d'un signe diacritique devant A et O
                            elif syllabes[-4][0] in ['A', 'O']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-5][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-5][1] in ['E', 'Ẹ', 'I']:
                            if syllabes[-6][-1] == 'Ẹ':
                                changements.append('s')
                            else:
                                changements.append('is')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-5][1] == 'A':
                            if syllabes[-6][-1] in ['A', 'E', 'I']:
                                changements.append('i')
                            #Après O et U
                            else:
                                changements.append('')
                        #Si les syllabes suivantes sont O ou U
                        elif syllabes[-5][1] in ['O', 'U']:
                            #Palatalisation de la vélaire sourde après Á et Í
                            if syllabes[-6][-1] in ['Á', 'A']:
                                changements.append('i')
                            elif syllabes[-6][-1] == 'Ǫ':
                                changements.append('u')
                            #Pour tout le reste
                            else:
                                changements.append('')
                        elif syllabes[-5][1] == 'Ọ':
                            changements.append('g')
                        else:
                            changements.append('')
                    else:
                        if syllabes[-6][-1] in ['L', 'M']:
                            changements.append('c')
                        #Palatalisation de C devant A
                        elif syllabes[-5][1] in ['A', 'Á']:
                            changements.append('ch')
                        elif syllabes[-6][-2] + syllabes[-6][-1] in ['ĘY', 'ǪY']:
                            changements.append('s')
                        elif syllabes[-6][-1] == 'Y' and syllabes[-5][1] == 'Ę':
                            changements.append('s')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de D (occlusive dentale sonore)
            elif syllabes[-5][0] == 'D':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        changements.append('')
                    elif syllabes[-5][1] == 'L':
                        #Assimilation
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('l')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-5][1] == 'R':
                        #Assimilation et simplification entre des voyelles
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('r')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            changements.append(syllabes[-5][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('i')
                        #Mouillure du N
                        elif syllabes[-6][-1] == 'N':
                            changements.append('gn')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-5]) > 2 and syllabes[-5][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-5][2] == 'S':
                            changements.append('t')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de F (fricative sourde)
            elif syllabes[-5][0] == 'F':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] in ['L', 'R']:
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal, la fricative se sonorise
                        if syllabes[-5][1] in ['A', 'E', 'I']:
                            changements.append('v')
                        elif syllabes[-5][1] == 'Ẹ':
                            changements.append('f')
                        #Sinon, elle s'amuït
                        else:
                            changements.append('')
                    elif syllabes[-5][-1] == ' ':
                        changements.append('v')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de G (occlusive palatale sonore)
            elif syllabes[-5][0] == 'G':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'L':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] in ['A', 'Á'] and syllabes[-5][2] in ['A', 'Á']:
                                changements.append('ill')
                            else:
                                changements.append('il')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'M':
                        changements.append(syllabes[-5][1])
                    #Mouillure du N
                    elif syllabes[-5][1] == 'N':
                        changements.append('gn')
                    elif syllabes[-5][1] == 'R':
                        #Les palatales combinées s'affaiblissent toutes en [ir]
                        if syllabes[-6][1] in listes_lettres['toutes_les_voyelles']:
                            #Si le yod est déjà présent, pas besoin de amrquer un i supplémentaire
                            if syllabes[-6][-1] in ['Ę', 'Í']:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        elif syllabes[-6][-1] in ['L', 'R']:
                            changements.append('dr')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        elif syllabes[-5][2] == 'A':
                            changements.append('gu')
                        else:
                            changements.append(syllabes[-5][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('i')
                        elif syllabes[-5][2] == 'U':
                            changements.append('g')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-5][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #La palatale sonore s'affaiblit en milieu intervocalique
                        if syllabes[-5][1] in ['E', 'I']:
                            changements.append('i')
                        #La palatale sonore s'affaiblit jusqu'à l'amuössement devant les voyelles toniques
                        elif syllabes[-5][1] in ['Ẹ', 'Ę', 'Í']:
                            #Petite méthode pour tricher lorsqu'il faut proposer une évolution scientifique
                            if syllabes[-6][-1] == 'Í':
                                changements.append('g')
                            else:
                                changements.append('')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-5][1] in ['A', 'Á']:
                            if syllabes[-6][-1] in ['E', 'I', 'A']:
                                changements.append('i')
                            elif syllabes[-6][-1] == 'O':
                                changements.append('v')
                            #Après 'U'
                            else:
                                changements.append('')
                        #généralement, la vélaire s'amuïse devant O et U, sauf s'il y a un i devant
                        elif syllabes[-5][1] in ['O', 'U']:
                            if syllabes[-6][-1] == 'I':
                                changements.append('i')
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    #Palatalisation de G devant A
                    elif syllabes[-5][1] in ['Á', 'O']:
                        changements.append('j')
                    elif syllabes[-6][-1] == 'N':
                        changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'H':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'J':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'K':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de L
            elif syllabes[-5][0] == 'L':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Mouillure du L
                    if syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] == 'H':
                            changements.append('ill')
                        else:
                            changements.append('ll')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-6][-1] == 'M':
                        changements.append('b' + syllabes[-5][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-6][-1] == 'N':
                        if syllabes[-6][-2] == 'Í':
                            changements.append('g' + syllabes[-5][0])
                        else:
                            changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-6][-1] == 'NY':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après L
                    elif syllabes[-6][-1] == 'L':
                        if syllabes[-6][-2] == 'Ę' and syllabes[-5][1] == 'A':
                            changements.append('ll')
                        else:
                            changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-6][-1] == 'LY':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-6][-1] == 'Z':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-6][-1] in ['S', 'X']:
                        if syllabes[-6][-2] in ['Ę', 'Í']:
                            changements.append('l')
                        else:
                            changements.append('t' + syllabes[-5][0])
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de M
            elif syllabes[-5][0] == 'M':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'R':
                        changements.append('br')
                    elif syllabes[-5][1] == 'Y':
                        changements.append('g')
                    else:
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                else:
                    if syllabes[-6][-1] == 'Ǫ' and syllabes[-5][1] == 'E':
                        changements.append('n')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de N
            elif syllabes[-5][0] == 'N':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] + syllabes[-5][2] == 'GR':
                        changements.append('ndre')
                    elif syllabes[-5][1] + syllabes[-5][2] == 'CR':
                        changements.append('ntr')
                    else:
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                else:
                    #Assimilation à la consonne précédente
                    if syllabes[-6][-1] == 'M':
                        changements.append('')
                    #Mouillure du N
                    elif syllabes[-6][-1] == 'G':
                        changements.append('ng')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de P (occlusive labiale sourde)
            elif syllabes[-5][0] == 'P':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'L':
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-5][0])
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('ch')
                        else:
                            changements.append('ch')
                    else:
                        changements.append(syllabes[-5][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #Affaiblissement jusqu'à se confondre avec la sonore en milieu palatal
                        if syllabes[-5][1] in ['A', 'Á', 'Ẹ']:
                            changements.append('v')
                        elif syllabes[-6][-1] == 'Ǫ' and syllabes[-5][1] == 'U':
                            changements.append('')
                        elif syllabes[-5][1] == 'Ę':
                            changements.append('p')
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de Q
            elif syllabes[-5][0] == 'Q':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('v')
                        elif syllabes[-5][2] == 'A':
                            changements.append('qu')
                        else:
                            changements.append(syllabes[-5][0])
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de R
            elif syllabes[-5][0] == 'R':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][-1] == 'R':
                        changements.append('R' + syllabes[-5][1])
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-6][-1] == 'M':
                        changements.append('b' + syllabes[-5][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-6][-1] == 'N':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-6][-1] == 'NY':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après L
                    elif syllabes[-6][-1] == 'L':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-5][-1] == 'LY':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-6][-1] == 'Z':
                        changements.append('d' + syllabes[-5][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-6][-1] in ['S', 'X']:
                        #Épenthèse d'un D après sifflante sonore
                        if syllabes[-6][-2] == 'Ǫ':
                            changements.append('d' + syllabes[-5][0])
                        else:
                            changements.append('t' + syllabes[-5][0])
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de S
            elif syllabes[-5][0] == 'S':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Groupe consonantique complexe de trois lettres
                    if syllabes[-5][2] in listes_lettres['consonnes_et_semi_consonnes']:
                        changements.append(syllabes[-5][0] + syllabes[-5][1] + syllabes[-5][2])
                    else:
                        if syllabes[-5][1] == 'R':
                            changements.append('str')
                        elif syllabes[-5][1] == 'T':
                            if syllabes[-5][2] == 'R':
                                changements.append(syllabes[-5][0] + syllabes[-5][1] + syllabes[-5][2])
                            else:
                                changements.append(syllabes[-5][0] + syllabes[-5][1])
                        #Les éléments en wau perdent généralement leur semi-voyelle
                        elif syllabes[-5][1] == 'W':
                            changements.append(syllabes[-5][0])
                        #La sifflante sourde se palatalise au contact du yod
                        elif syllabes[-5][1] == 'Y':
                            if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                                if syllabes[-5][-1] == 'C' and syllabes[-5][-2] == 'A' and syllabes[-4][2] == 'Á':
                                    changements.append('ssi')
                                else:
                                    changements.append('is')
                            else:
                                if syllabes[-6][-1] == 'C' and syllabes[-6][-2] == 'A' and syllabes[-5][2] == 'Á':
                                    changements.append('ssi')
                                else:
                                    changements.append('s')
                        else:
                            changements.append(syllabes[-5][0])
                else:
                    #Double ss
                    if (syllabes[-6][-1] in ['A', 'Á' ] and syllabes[-5][1] in ['A','Á']) or (syllabes[-6][-2] + syllabes[-6][-1] in ['AY', 'ÁY'] and syllabes[-5][1] in ['A', 'Á']):
                        changements.append('ss')
                    #Double SS
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-6][-1] in ['ES', 'ẸS'] and syllabes[-5][1] == 'A':
                        changements.append('ss')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de T
            elif syllabes[-5][0] == 'T':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        changements.append('c')
                    elif syllabes[-5][1] == 'L':
                        #La séquence TL devient CL puis l mouillé
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('il')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] in ['E', 'O'] and syllabes[-5][2] in ['Á', 'Í']:
                                changements.append('rr')
                            else:
                                changements.append('r')
                        else:
                            changements.append(syllabes[-5][0] + syllabes[-5][1])
                    elif syllabes[-5][1] == 'S':
                        #Si la syllabe est uniquement composée de TS
                        if len(syllabes[-5]) == 2:
                            changements.append('')
                        else:
                            changements.append('ts')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-5][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('is')
                        else:
                            if syllabes[-5][2] in ['A', 'O', 'Ọ', 'Ǫ']:
                                changements.append('ç')
                            elif syllabes[-4][0] in ['A', 'O', 'Ọ', 'Ǫ']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-5]) > 2 and syllabes[-5][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-5][2] == 'S':
                            changements.append('t')
                        elif len(syllabes[-6]) > 1 and syllabes[-6][0] + syllabes[-6][1] in listes_lettres['consonantisme_implosif_complexe_2_lettres']:
                            changements.append('t')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        if syllabes[-6][-2] + syllabes[-6][-1] == 'ǪY' and syllabes[-5][1] == 'Á':
                            changements.append('d')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de V
            elif syllabes[-5][0] == 'V':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Assimilation
                    if syllabes[-5][1] == 'R':
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('g')
                        elif syllabes[-6][-1] == 'N':
                            changements.append('vi')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu vélaire, la consonne subit un amuïssement
                        if syllabes[-5][1] in ['O', 'U']:
                            changements.append('')
                        else:
                            changements.append('v')
                    else:
                        if syllabes[-6][-1] == 'R':
                            changements.append('')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de W
            elif syllabes[-5][0] == 'W':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] == 'S':
                            changements.append('dr')
                        else:
                            changements.append(syllabes[-5][1])
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    if syllabes[-5][1] in ['Ẹ', 'Ú']:
                        changements.append('')
                    elif len(syllabes[-6]) > 1 and syllabes[-6][-2] + syllabes[-6][-1] == 'ĘY' and syllabes[-5][1] == 'A':
                        changements.append('v')
                    else:
                        changements.append('g')

            #Gestion de X
            elif syllabes[-5][0] == 'X':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles'] and syllabes[-5][1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-6][-1] == 'A' and syllabes[-5][1] == 'Ī':
                            changements.append('x')
                        else:
                            changements.append('ss')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de Y
            elif syllabes[-5][0] == 'Y':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        if syllabes[-5][2] in ['A', 'Á']:
                            changements.append('ch')
                        #Spirantisation
                        elif syllabes[-6][-2] + syllabes[-6][-1] == 'ĘD':
                            changements.append('r')
                        elif syllabes[-6][-2] + syllabes[-6][-1] in ['ẸN', 'ỌN']:
                            changements.append('')
                        else:
                            changements.append('c')
                    #Épenthèse d'un D après L
                    elif syllabes[-5][1] == 'R':
                        if syllabes[-6][-1] == 'L':
                            changements.append('DR')
                        else:
                            changements.append('r')

                    elif syllabes[-5][1] == 'T':
                        if syllabes[-5][2] in ['Á', 'Ẹ', 'Ọ']:
                            changements.append('d')
                        else:
                            changements.append(syllabes[-5][1])
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    #Le yod est déjà dprésent devant
                    if syllabes[-6][-1] == 'L':
                        if syllabes[-6] == 'TR':
                            changements.append('')
                        elif syllabes[-5][1] == 'Á':
                            changements.append('j')
                        else:
                            changements.append('')
                    #Spirantisation
                    elif syllabes[-6][-1] == 'D':
                        changements.append('r')
                    elif syllabes[-5][1] == 'Á':
                        if syllabes[-6][-1] in ['E', 'Ẹ']:
                            changements.append('i')
                        elif syllabes[-6][-1] == 'O':
                            changements.append('li')
                        elif syllabes[-6][-1] == 'G':
                            changements.append('')
                        elif syllabes[-6][-1] == 'C':
                            changements.append('g')
                        else:
                            changements.append('gi')
                    elif syllabes[-5][1] == 'E':
                            changements.append('g')
                    #Le reste
                    elif syllabes[-5][1] in ['C', 'Ę', 'G', 'Í', 'L', 'N', 'Ǫ', 'Ọ', 'R', 'S', 'Y']:
                        changements.append('')
                    else:
                        changements.append('i')

            #Gestion de Z
            elif syllabes[-5][0] == 'Z':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    changements.append(syllabes[-5][0])

        #Vocalisme atone
        #A
        if 'A' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-5][-1] == 'A':
                if len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] == 'TY':
                    changements.append('ie')
                else:
                    changements.append('e')
            #Si A se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'A':
                #Préfixe
                if syllabes[-6] == syllabes[0] == 'EM':
                    changements.append('a')
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                elif syllabes[-5][-2] == syllabes[-5][0] and syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('a')
                elif syllabes[-5][-1] in ['M', 'N']:
                    changements.append('a')
                elif syllabes[-5][-1] + syllabes[-4][0] == 'TY':
                    changements.append('ai')
                elif syllabes[-5][-1] == 'W':
                    changements.append('au')
                else:
                    changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')
        #E
        elif 'E' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-5][-1] == 'E':
                changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'E':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-5][-2] == syllabes[-5][0] and syllabes[-5][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('i')
                else:
                    changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-5][-1] == 'I':
                changements.append('')
            #Si I se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'I':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-5][-2] == syllabes[-5][0] and syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('i')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('ou')
                #Situation de hiatus avec un Ú tonique : affaiblissement
                elif syllabes[-4][0] == 'Ú':
                    changements.append('e')
                else:
                    changements.append('o')
            #Si O se trouve en position ouvert
            elif syllabes[-5][-1] == 'O':
                #Situation de hiatus avec un Ú tonique : affaiblissement
                if syllabes[-4][0] == 'Ú':
                    changements.append('e')
                else:
                    changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'O':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-5][-2] == syllabes[-5][0] and syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('o')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('u')
            #Si U se trouve en position ouvert
            elif syllabes[-5][-1] == 'U':
                changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'U':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-5][-2] == syllabes[-5][0] and syllabes[-6][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('u')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #Vocalisme tonique (cette éventualité peut se passer en cas de préfixation du mot)
        #Á
        if 'Á' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Absence de diphtongaison due à une nasale
                elif syllabes[-4][0] == 'N':
                    changements.append('ai')
                elif syllabes[-6][-1] == 'I':
                    changements.append('a')
                else:
                    changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-5][-1] == 'Á':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Absence de diphtongaison du à une nasale
                elif syllabes[-4][0] == 'N':
                    changements.append('ai')
                #Ouverture due à un yod
                elif syllabes[-4][0] + syllabes[-4][1] == 'CL':
                    changements.append('a')
                #Loi de Bartsch
                elif syllabes[-5][-2] in ['X', 'C']:
                    changements.append('ie')
                #Présence d'un yod antéposé
                elif syllabes[-5][-2] == 'Y':
                    changements.append('ie')
                #Présence d'un yod antéposé
                elif syllabes[-6][-1] == 'Y':
                    changements.append('ie')
                elif len(syllabes[-5]) > 2 and syllabes[-5][-3] == 'Y':
                    changements.append('ie')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'Á':
                #Absence de diphtongaison du à une nasale
                if syllabes[-5][-1] == 'N':
                    if syllabes[-4][0] == 'T':
                        changements.append('a')
                    else:
                        changements.append('ai')
                #Fermeture devant R
                elif syllabes[-5][-1] == 'R':
                    if syllabes[-5][-3] == 'Y':
                        changements.append('ie')
                    #Si ce n'est pas un verbe
                    elif syllabes[-4][0] not in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-5][0] == 'V':
                            changements.append('ai')
                        else:
                            changements.append('ie')
                    else:
                        changements.append('e')
                #Fermeture devant un wau
                elif syllabes[-5][-1] == 'W':
                    changements.append('o')
                #Diphtongaison
                elif syllabes[-5][-1] + syllabes[-4][0] == 'TY':
                    changements.append('ai')
                #Anticipation d'un Ī long final
                elif syllabes[-4] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-5]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-5][-1] == 'Ẹ':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-5][-2] == 'Ẹ':
                #Présence d'un yod
                if syllabes[-5][-1] == 'Y':
                    changements.append('i')
                elif syllabes[-4][0] == 'Y':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-5]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('i')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                else:
                    changements.append('ie')
            elif syllabes[-5][-1] == 'Ę':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('i')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                #Présence d'un n mouillé avant le E ouvert
                elif len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] == 'GN':
                    changements.append('e')
                else:
                    changements.append('ie')
            elif syllabes[-5][-2] == 'Ę':
                #Au contact d'un yod géminé
                if syllabes[-5][-1] == 'Y':
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif syllabes[-5][-1] + syllabes[-4][0] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                #Influence fermante d'un wau
                elif syllabes[-5][-1] + syllabes[-4][0] == 'QW':
                    changements.append('iu')
                #Le Ę ouvert échappe à l'action d'une nasale
                elif syllabes[-5][-1] == 'M':
                    changements.append('ie')
                else:
                    changements.append('e')
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                changements.append('i')
            elif syllabes[-5][-1] == 'Í':
                changements.append('i')
            elif syllabes[-5][-2] == 'Í':
                changements.append('i')
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('ui')
                #Au contact d'une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                else:
                    changements.append('ou')
            elif syllabes[-5][-1] == 'Ọ':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('ui')
                #Au contact d'une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                else:
                    changements.append('ou')
            elif syllabes[-5][-2] == 'Ọ':
                #Au contact d'un yod géminé
                if syllabes[-4][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    if syllabes[-5][-1] == 'N':
                        changements.append('oi')
                    else:
                        changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif syllabes[-5][-1] + syllabes[-4][0] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    if syllabes[-6][-1] == syllabes[0][-1] == 'A' or syllabes[-6][-2] == 'A':
                        changements.append('o')
                    else:
                        changements.append('ui')
                #Au contact d'un n mouillé
                elif syllabes[-5][-1] + syllabes[-4][0] in ['GN', 'NG']:
                    changements.append('oi')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Absence de diphtongaison du à une nasale
                elif syllabes[-4][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                else:
                    changements.append('ue')
            elif syllabes[-5][-1] == 'Ǫ':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Absence de diphtongaison du à une nasale
                elif syllabes[-4][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé
                elif syllabes[-4][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-4]) >= 2 and syllabes[-4][0] + syllabes[-4][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                else:
                    changements.append('ue')
            elif syllabes[-5][-2] == 'Ǫ':
                #Au contact d'un N mouillé
                if syllabes[-5][-1] + syllabes[-4][0] in ['GN', 'NG']:
                    changements.append('oi')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                else:
                    changements.append('u')
            elif syllabes[-5][-1] == 'Ú':
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-4][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                else:
                    changements.append('u')
            elif syllabes[-5][-2] == 'Ú':
                changements.append('u')
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-5][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-5][-1] == 'B':
                #Assimilation à la consonnne suivante
                changements.append('')

            #Gestion de C
            elif syllabes[-5][-1] == 'C':
                #Quelques trucs devront sûrement être changés
                #Amuïssmeent en î
                if syllabes[-5][-2] in ['A', 'Ẹ']:
                    #Cas d'assimilation à un groupe dégageant un yod
                    if syllabes[-4][0] + syllabes[-4][1] == 'TY':
                        changements.append('')
                    #Si le i est déjà dans la voyelle
                    else:
                        changements.append('i')
                elif syllabes[-5][-2] == 'Í':
                    if syllabes[-4][0] + syllabes[-4][1] == 'TY':
                        changements.append('s')
                    else:
                        changements.append('')
                #Assimilation
                else:
                    changements.append('')

            #Gestion de D
            elif syllabes[-5][-1] == 'D':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de F
            elif syllabes[-5][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[-5][-1] == 'G':
                if syllabes[-5] == 'RG':
                    changements.append('')
                #à voir
                if syllabes[-5][-2] in ['E', 'I']:
                    changements.append('i')
                elif syllabes[-5][-2] in ['A', 'Á', 'O', 'U']:
                    changements.append('u')
                else:
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-5][-1] == 'H':
                changements.apped('')

            #Gestion de L
            elif syllabes[-5][-1] == 'L':
                #Présence d'un yod
                if syllabes[-4][0] == 'Y':
                    if syllabes[-5][-2] == 'Á':
                        if syllabes[-4][1] == 'A':
                            changements.append('ill')
                        else:
                            changements.append('il')
                    else:
                        changements.append('ll')
                elif syllabes[-4][0] == 'L':
                    changements.append('')
                #Vocalisation en wau
                else:
                    changements.append('u')

            #Gestion de M
            elif syllabes[-5][-1] == 'M':
                if syllabes[-4][0] in ['B', 'T']:
                    changements.append('n')
                else:
                    changements.append(syllabes[-5][-1])

            #Gestion de N
            elif syllabes[-5][-1] == 'N':
                #Mouillure du N
                if syllabes[-4][0] == 'Y':
                    changements.append('gn')
                elif syllabes[-4][0] + syllabes[-4][1] == 'DY':
                    changements.append('')
                else:
                    changements.append(syllabes[-5][-1])

            #Gestion de P
            elif syllabes[-5][-1] == 'P':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de R
            elif syllabes[-5][-1] == 'R':
                if syllabes[-5] in ['BR', 'CR', 'FR', 'MR', 'SR', 'TR']:
                    changements.append('')
                #Présence d'un R dans la syllabe suivante
                elif syllabes[-4][0] == 'R':
                    changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[-5][-1])

            #Gestion de S
            elif syllabes[-5][-1] == 'S':
                #Présence d'un S en position explosive dans la syllabe suviante
                if syllabes[-4][0] == 'S':
                    if syllabes[-5][-2] == 'A' and syllabes[-4][1] == 'A':
                        changements.append('s')
                    else:
                        changements.append('')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-5][-1] == 'T':
                if syllabes[-5][-2] in ['A', 'Á'] and syllabes[-4][0] == 'Y':
                    changements.append('s')
                    """
                    Attention !! à manipuler avec précaution !!
                    """
                elif syllabes[-4][0] == 'Y':
                    changements.append('c')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de V
            elif syllabes[-5][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-5][-1] == 'W':
                if syllabes[-5][-2] == 'O':
                    changements.append('u')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de X
            elif syllabes[-5][-1] == 'X':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Y
            elif syllabes[-5][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[-5][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
