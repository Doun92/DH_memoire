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

class SyllabePenultieme:

    def __init__(self):
        return

    def syllabe_penultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Si la première syllabe est un préfixe
        if syllabes[-2][0] == ' ':
            if syllabes[-2][1] == 'Á':
                changements.append('a')
            else:
                changements.append(syllabes[-2][1])

        #Consoantisme initial
        if syllabes[-2][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-2][0] == 'B':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        changements.append('g')
                    elif syllabes[-2][1] == 'L':
                        if syllabes[-3][-1] == 'M':
                            if syllabes[-3][-2] == 'A':
                                changements.append('bl')
                            else:
                                changements.append('br')
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Exceptionnellement, une séquence -BR- peut perdre son statut intervocalique et aboutir en position implosive secondaire
                            if syllabes[-3][-1] == 'Ę' and syllabes[-1][0] == 'Y':
                                changements.append('r')
                            else:
                                changements.append('vr')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'T':
                            changements.append('d')
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            changements.append(syllabes[-2][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if len(syllabes[-2]) > 2 and syllabes[-2][2] == 'A':
                                changements.append('g')
                            elif syllabes[-3][-1] == 'A' and syllabes[-2][2] == 'Ǫ':
                                changements.append('j')
                            #En milieu vélaire
                            else:
                                changements.append('i')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-2][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal, la spirante se stabilise en [v]
                        if syllabes[-3][-1] in ['Á', 'Ẹ', 'Ę', 'E', 'Í', 'I'] or syllabes[-2][1] in ['A', 'Á', 'Ẹ', 'Ę', 'E', 'Í', 'I']:
                            #En finale ou devant S et T, elle s'assourdit
                            if syllabes[-2][1] not in ['A', 'Á'] and syllabes[-1][0] in ['S', 'T']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        #Si une voyelle vélaire précède ou suit B, le relachement peut se prolonger en [w] et aller jusqu'à l'amuïssement
                        elif syllabes[-3][-1] in ['O', 'Ǫ', 'Ọ', 'U', 'Ú'] or syllabes[-2][1] in ['O', 'Ǫ', 'Ọ', 'U', 'Ú']:
                            changements.append('')
                        else:
                            changements.append('b')
                    #Consonantisme explosif
                    elif syllabes[-3][-2] + syllabes[-3][-1] == 'ER' and syllabes[-2][1] in ['Ẹ', 'Í']:
                        changements.append('v')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de C
            elif syllabes[-2][0] == 'C':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'L':
                        #L mouillé
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Pas besoin de I s'il est présent dans la voyelle antéposée
                            if syllabes[-3][-1] in ['Ẹ', 'Í']:
                                changements.append('l')
                            else:
                                changements.append('il')
                        #Après S, la séquence se simplifie en L
                        elif syllabes[-3][-1] == 'S':
                            changements.append('l')
                        elif syllabes[-3][-1] == 'C':
                            changements.append('gl')
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'P':
                        if syllabes[-2][2] == 'U':
                            changements.append('qu')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] in ['Í']:
                                changements.append('r')
                            elif syllabes[-3][-1] == 'Á':
                                changements.append('gr')
                            else:
                                changements.append('ir')
                        elif syllabes[-3][-1] in ['N', 'R', 'S']:
                            if syllabes[-1][0] == 'B':
                                changements.append('cr')
                            else:
                                changements.append('tr')
                        #Si un Y est antéposé inorganiquement
                        elif syllabes[-3][-1] == 'Y':
                            changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    #Deuxième lettre = T
                    elif syllabes[-2][1] == 'T':
                        changements.append(syllabes[-2][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            if syllabes[-2][2] == 'A':
                                changements.append('qu')
                            else:
                                changements.append(syllabes[-2][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('s')
                        else:
                            if syllabes[-3][-1] in ['C', 'M', 'N']:
                                changements.append('c')
                            #Avancement du point d'articulation
                            elif syllabes[-3][-1] == 'D':
                                changements.append('g')
                            #Ajout d'un signe diacritique devant A et O
                            elif syllabes[-1][0] in ['A', 'O']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-2][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in ['E', 'Ẹ', 'I', 'Í']:
                            if syllabes[-3][-1] in ['Á', 'E', 'Ẹ']:
                                changements.append('s')
                            else:
                                changements.append('is')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-2][1] == 'A':
                            if syllabes[-3][-1] in ['A', 'E', 'I']:
                                changements.append('i')
                            #Après O et U
                            else:
                                changements.append('')
                        #Si les syllabes suivantes sont O ou U
                        elif syllabes[-2][1] in ['O', 'U']:
                            #Palatalisation de la vélaire sourde après Á et Í
                            if syllabes[-3][-1] in ['Á', 'A']:
                                changements.append('i')
                            elif syllabes[-3][-1] == 'Ǫ':
                                changements.append('u')
                            #Pour tout le reste
                            else:
                                changements.append('')
                        elif syllabes[-2][1] == 'Ọ':
                            changements.append('g')
                        elif syllabes[-3][-1] in ['E', 'Í'] and syllabes[-2][1] in ['Ę', 'Ǫ', 'Ú']:
                            changements.append('c')
                        else:
                            changements.append('')
                    else:
                        #Palatalisation de C devant A
                        if syllabes[-2][1] in ['A', 'Á']:
                            if syllabes[-3][-1] == 'M':
                                changements.append('g')
                            else:
                                changements.append('ch')
                        elif syllabes[-3][-1] in ['L', 'M']:
                            changements.append('c')
                        elif syllabes[-3][-2] + syllabes[-3][-1] in ['ĘY', 'ǪY']:
                            changements.append('s')
                        elif syllabes[-3][-1] == 'Y' and syllabes[-2][1] == 'Ę':
                            changements.append('s')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de D
            elif syllabes[-2][0] == 'D':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        #Palatalisation
                        if syllabes[-2][2] == 'Á':
                            changements.append('g')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'L':
                        #Assimilation
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('l')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'R':
                        #Assimilation et simplification entre des voyelles
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] in ['A', 'Á'] and syllabes[-2][2] in ['A', 'Á']:
                                changements.append('rr')
                            else:
                                changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        else:
                            changements.append(syllabes[-2][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] == 'Ǫ' and syllabes[-2][2] == 'Á':
                                changements.append('')
                            else:
                                changements.append('i')
                        #Mouillure du N
                        elif syllabes[-3][-1] == 'N':
                            changements.append('gn')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-2]) > 2 and syllabes[-2][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2][2] == 'S':
                            changements.append('t')
                        #Présence d'un préfixe
                        elif syllabes[-3][-1] == 'Ọ' and syllabes[-2][1] == 'Ọ':
                            changements.append('d')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de F
            elif syllabes[-2][0] == 'F':
                #Cas où un préfixe est présent
                if syllabes[-3][-1] == ' ':
                    if syllabes[-2][1] == 'Ẹ':
                        changements.append('v')
                    else:
                        changements.append('f')
                elif syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-2][1] in ['L', 'R']:
                        changements.append(syllabes[-2][0] + syllabes[-2][1])
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal, la fricative se sonorise
                        if syllabes[-2][1] in ['A', 'Á', 'E', 'I']:
                            changements.append('v')
                        elif syllabes[-2][1] == 'Ẹ':
                            changements.append('f')
                        #Sinon, elle s'amuït
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de G
            elif syllabes[-2][0] == 'G':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-2][1] == 'L':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] in ['A', 'Á'] and syllabes[-2][2] in ['A', 'Á']:
                                changements.append('ill')
                            elif syllabes[-3][-1] == 'Ẹ':
                                if syllabes[-2][2] in ['A', 'Á']:
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                changements.append('il')
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'M':
                        changements.append(syllabes[-2][1])
                    #Mouillure du N
                    elif syllabes[-2][1] == 'N':
                        if syllabes[-3][-1] == 'Ǫ':
                            changements.append('n')
                        else:
                            changements.append('gn')
                    elif syllabes[-2][1] == 'R':
                        #Les palatales combinées s'affaiblissent toutes en [ir]
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Si le yod est déjà présent, pas besoin de amrquer un i supplémentaire
                            if syllabes[-3][-1] in ['Ę', 'Í']:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        elif syllabes[-3][-1] in ['L', 'R']:
                            changements.append('dr')
                        elif syllabes[-3][-1] == 'G':
                            changements.append('r')
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'T':
                        changements.append('t')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        elif len(syllabes[-2]) > 2 and syllabes[-2][2] == 'A':
                            changements.append('gu')
                        else:
                            changements.append(syllabes[-2][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('i')
                        elif syllabes[-2][2] == 'U':
                            changements.append('g')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-2][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #La palatale sonore s'affaiblit en milieu intervocalique
                        if syllabes[-2][1] in ['E', 'I']:
                            changements.append('i')
                        #La palatale sonore s'affaiblit jusqu'à l'amuössement devant les voyelles toniques
                        elif syllabes[-2][1] in ['Ẹ', 'Ę', 'Í']:
                            #Petite méthode pour tricher lorsqu'il faut proposer une évolution scientifique
                            if syllabes[-3][-1] == 'Í':
                                changements.append('g')
                            else:
                                changements.append('')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-2][1] in ['A', 'Á']:
                            if syllabes[-3][-1] in ['E', 'I', 'A']:
                                changements.append('i')
                            elif syllabes[-3][-1] == 'O':
                                changements.append('v')
                            #Après 'U'
                            else:
                                changements.append('')
                        #généralement, la vélaire s'amuïse devant O et U, sauf s'il y a un i devant
                        elif syllabes[-2][1] in ['O', 'U']:
                            if syllabes[-3][-1] == 'I':
                                changements.append('i')
                            # elif syllabes[-3][-1] == 'Ọ':
                                # changements.append('g')
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    #Palatalisation de G devant A
                    elif syllabes[-2][1] in ['Á', 'O']:
                        changements.append('j')
                    elif syllabes[-3][-1] == 'N':
                        if syllabes[-2][1] in ['Ę', 'Ẹ', 'Ọ']:
                            changements.append('g')
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'H':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'J':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'K':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de L
            elif syllabes[-2][0] == 'L':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'M':
                        changements.append(syllabes[-2][0] + syllabes[-2][1])
                    #Mouillure du L
                    elif syllabes[-2][1] == 'W':
                        changements.append('l')
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] == 'H':
                            changements.append('ill')
                        elif syllabes[-3][-1] == 'Ę' and syllabes[-1][0] == 'R':
                            changements.append('u')
                        else:
                            changements.append('ll')
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-3][-1] == 'M':
                        changements.append('b' + syllabes[-2][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-3][-1] == 'N':
                        if syllabes[-3][-2] == 'Í':
                            changements.append('g' + syllabes[-2][0])
                        else:
                            changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] == 'NY':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après L
                    # elif syllabes[-3][-1] == 'L':
                    #     changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] == 'LY':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-3][-1] == 'Z':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-3][-1] in ['S', 'X']:
                        if syllabes[-3][-2] in ['Ę', 'Í']:
                            changements.append('l')
                        else:
                            changements.append('t' + syllabes[-2][0])
                    #Mouillure de L
                    elif syllabes[-3][-1] == 'Y':
                        if syllabes[-3][-2] == 'A' and syllabes[-2][1] == 'Í':
                            changements.append('ll')
                        else:
                            changements.append('l')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de M
            elif syllabes[-2][0] == 'M':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'R':
                        changements.append('br')
                    elif syllabes[-2][1] == 'Y':
                        changements.append('g')
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    if syllabes[-3][-1] == 'Ǫ' and syllabes[-2][1] == 'E':
                        changements.append('n')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de N
            elif syllabes[-2][0] == 'N':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if len(syllabes[-2]) > 2 and syllabes[-2][1] + syllabes[-2][2] == 'GR':
                        changements.append('ndre')
                    elif len(syllabes[-2]) > 2 and syllabes[-2][1] + syllabes[-2][2] == 'CR':
                        changements.append('ntr')
                    elif syllabes[-2][1] == 'T':
                        changements.append('nt')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Assimilation à la consonne précédente
                    if syllabes[-3][-1] == 'M':
                        changements.append('')
                    #Mouillure du N
                    elif syllabes[-3][-1] == 'G':
                        changements.append('gn')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de P
            elif syllabes[-2][0] == 'P':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        if syllabes[-2][2] in ['A', 'Á']:
                            changements.append('ch')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'L':
                        changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'T':
                        changements.append('t')
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-3][0])
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('ch')
                    else:
                        changements.append(syllabes[-2][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #Affaiblissement jusqu'à se confondre avec la sonore en milieu palatal
                        if syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ọ', 'Ǫ']:
                            changements.append('v')
                        elif syllabes[-3][-1] == 'Ǫ' and syllabes[-2][1] == 'U':
                            changements.append('')
                        elif syllabes[-2][1] == 'Ę':
                            changements.append('p')
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de Q
            elif syllabes[-2][0] == 'Q':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('v')
                        elif len(syllabes[-2]) > 2 and syllabes[-2][2] == 'A':
                            changements.append('qu')
                        elif 'A' not in syllabes[-1] or 'E' not in syllabes[-1] or 'I' not in syllabes[-1] or 'O' not in syllabes[-1] or 'U' not in syllabes[-1]:
                            changements.append('que')
                        else:
                            changements.append(syllabes[-2][0])
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de R
            elif syllabes[-2][0] == 'R':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-3][-1] == 'R':
                        if syllabes[-2][1] == 'C':
                            if syllabes[-2][2] == 'Á':
                                changements.append('g')
                            else:
                                changements.append('c')
                        else:
                            changements.append('R' + syllabes[-2][1])
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] == 'E' and syllabes[-2][2] == 'Ǫ':
                            changements.append('r')
                        else:
                            changements.append('rj')
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-3][-1] == 'M':
                        changements.append('b' + syllabes[-2][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-3][-1] == 'N':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] == 'NY':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après L
                    elif syllabes[-3][-1] == 'L':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] == 'LY':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-3][-1] == 'Z' or syllabes[-3] == 'SW':
                        changements.append('d' + syllabes[-2][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-3][-1] in ['S', 'X']:
                        #Épenthèse d'un D après sifflante sonore
                        if syllabes[-3][-2] == 'Ǫ':
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append('t' + syllabes[-2][0])
                    elif syllabes[-3][-1] == 'R':
                        if syllabes[-3][-2] in ['A', 'Ǫ'] and syllabes[-2][1] in ['A', 'Ú']:
                            changements.append('r')
                        else:
                            changements.append('rr')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de S
            elif syllabes[-2][0] == 'S':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Groupe consonantique complexe de trois lettres
                    if len(syllabes[-2]) > 2 and syllabes[-2][2] in listes_lettres['consonnes_et_semi_consonnes']:
                        changements.append(syllabes[-2][0] + syllabes[-2][1] + syllabes[-2][2])
                    else:
                        if syllabes[-2][1] == 'R':
                            changements.append('str')
                        elif syllabes[-2][1] == 'T':
                            if syllabes[-2][2] == 'R':
                                changements.append(syllabes[-2][0] + syllabes[-2][1] + syllabes[-2][2])
                            else:
                                changements.append(syllabes[-2][0] + syllabes[-2][1])
                        #Les éléments en wau perdent généralement leur semi-voyelle
                        elif syllabes[-2][1] == 'W':
                            changements.append(syllabes[-2][0])
                        #La sifflante sourde se palatalise au contact du yod
                        elif syllabes[-2][1] == 'Y':
                            if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                                if syllabes[-2][-1] == 'C' and syllabes[-2][-2] == 'A' and syllabes[-1][2] == 'Á':
                                    changements.append('ssi')
                                else:
                                    changements.append('is')
                            elif syllabes[-3][-1] == 'S':
                                if syllabes[-2][-1] == 'Á':
                                    changements.append('s')
                                else:
                                    changements.append('ss')
                            else:
                                if syllabes[-3][-1] == 'C' and syllabes[-3][-2] == 'A' and syllabes[-2][2] == 'Á':
                                    changements.append('ssi')
                                else:
                                    changements.append('s')
                        else:
                            changements.append(syllabes[-2][1])
                else:
                    #Double ss
                    if (syllabes[-3][-1] in ['A', 'Á' ] and syllabes[-2][1] in ['A','Á']) or (len(syllabes[-3]) > 2 and syllabes[-3][-2] + syllabes[-3][-1] in ['AY', 'ÁY'] and syllabes[-2][1] in ['A', 'Á']):
                        changements.append('ss')
                    #Double SS
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] in ['ES', 'ẸS'] and syllabes[-2][1] == 'A':
                        changements.append('ss')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de T
            elif syllabes[-2][0] == 'T':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        #Palatalisation
                        if syllabes[-2][2] == 'Á':
                            changements.append('ch')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'L':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('il')
                        elif syllabes[-3][-1] == 'B':
                            changements.append('l')
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'M':
                        changements.append('m')
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] in ['E', 'O'] and syllabes[-2][2] in ['Á', 'Í']:
                                changements.append('rr')
                            #Éléments triples (consonne + liquide + semi-voyelle)
                            elif syllabes[-1][0] == 'Y':
                                changements.append('tr')
                            else:
                                changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'S':
                        #Si la syllabe est uniquement composée de TS
                        if len(syllabes[-2]) == 2:
                            changements.append('')
                        else:
                            changements.append('ts')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-2][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] in ['Á', 'Ẹ', 'Í']:
                                changements.append('s')
                            else:
                                changements.append('is')
                        else:
                            if syllabes[-3][-1] == 'C':
                                if syllabes[-3][-2] == 'Í':
                                    changements.append('t')
                                else:
                                    changements.append('c')
                            elif syllabes[-3][-1] in ['N', 'S']:
                                changements.append('t')
                            # if len(syllabes[-2]) > 2 and syllabes[-2][2] in ['O', 'Ọ', 'Ǫ']:
                            #     changements.append('ç')
                            # elif len(syllabes[-2]) > 2 and syllabes[-2][2] == 'Á':
                            #     if syllabes[-3][-1] in ['C', 'N', 'R', 'S']:
                            #         if syllabes[-3][-2] in ['Ẹ', 'O', 'U']:
                            #             if syllabes[-2][2] == 'Á':
                            #                 changements.append('c')
                            #             else:
                            #                 changements.append('ci')
                            #         else:
                            #             changements.append('t')
                            #     else:
                                    # changements.append('ci')
                            # elif syllabes[-1][0] in ['A', 'O', 'Ọ', 'Ǫ']:
                            #     changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-2]) > 2 and syllabes[-2][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2][2] == 'S':
                            changements.append('t')
                        elif len(syllabes[-3]) > 1 and syllabes[-3][0] + syllabes[-3][1] in listes_lettres['consonantisme_implosif_complexe_2_lettres']:
                            if syllabes[-3][-1] == 'I' and syllabes[-2][1] == 'Á':
                                changements.append('')
                            else:
                                changements.append('t')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        if syllabes[-3][-2] + syllabes[-3][-1] in ['ỌY', 'ǪY'] and syllabes[-2][1] == 'Á':
                            changements.append('d')
                        elif len(syllabes) > 3 and syllabes[-4][-1] + syllabes[-3][-2] + syllabes[-3][-1] == 'ỌGY':
                            changements.append('d')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de V
            elif syllabes[-2][0] == 'V':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'D':
                        changements.append('v')
                    elif syllabes[-2][1] == 'R':
                        changements.append(syllabes[-2][0] + syllabes[-2][1])
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('g')
                        #Consonantisme explosif
                        elif syllabes[-3][-1] == 'N':
                            changements.append('v')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu vélaire, la consonne subit un amuïssement
                        if syllabes[-2][1] in ['Ę', 'Ẹ', 'Í', 'O', 'Ọ', 'U']:
                            if len(syllabes[-2]) > 2 and syllabes[-2][2] == 'N':
                                changements.append('v')
                            elif syllabes[-3][-1] == 'O' and syllabes[-2][1] == 'Ę':
                                changements.append('v')
                            else:
                                changements.append('')
                        else:
                            changements.append('v')
                    else:
                        if syllabes[-3][-1] == 'R':
                            if syllabes[-2][1] in ['Ẹ', 'Í']:
                                changements.append('v')
                            else:
                                changements.append('')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de W
            elif syllabes[-2][0] == 'W':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] == 'S':
                            changements.append('dr')
                        else:
                            changements.append(syllabes[-2][1])
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    if syllabes[-2][1] in ['Ẹ', 'Ú', 'Á']:
                        changements.append('')
                    elif len(syllabes[-3]) > 1 and syllabes[-3][-2] + syllabes[-3][-1] == 'ĘY' and syllabes[-2][1] == 'A':
                        changements.append('v')
                    else:
                        changements.append('g')

            #Gestion de X
            elif syllabes[-2][0] == 'X':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles'] and syllabes[-2][1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][-1] == 'A' and syllabes[-2][1] == 'Ī':
                            changements.append('x')
                        else:
                            changements.append('ss')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de Y
            elif syllabes[-2][0] == 'Y':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        if len(syllabes[-2]) > 2 and syllabes[-2][2] in ['A', 'Á']:
                            changements.append('ch')
                        #Spirantisation
                        elif syllabes[-3][-2] + syllabes[-3][-1] == 'ĘD':
                            changements.append('r')
                        elif syllabes[-3][-2] + syllabes[-3][-1] in ['ẸN', 'ỌN']:
                            changements.append('')
                        else:
                            changements.append('c')
                    #Épenthèse d'un D après L
                    #Mouillure du L
                    elif syllabes[-2][1] == 'L':
                        if syllabes[-3][-1] == 'Y':
                            changements.append('ll')
                        else:
                            changements.append('l')
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-3][-1] == 'L':
                            changements.append('DR')
                        else:
                            changements.append('r')
                    elif syllabes[-2][1] == 'T':
                        if syllabes[-2][2] in ['Á', 'Ẹ', 'Ọ']:
                            if syllabes[-3][-1] in ['D', 'Y']:
                                changements.append('t')
                            else:
                                changements.append('d')
                        else:
                            changements.append(syllabes[-2][1])
                    else:
                        changements.append(syllabes[-2][1])
                else:
                    #La labiale sonore + yod agit différemment selon son enoturage vocalique
                    if syllabes[-3][-1] in ['B', 'V']:
                        #En milieu palatal
                        if syllabes[-3][-2] in ['A', 'E']:
                            #Norme orthographique différente selon la voyelle qui suit
                            if len(syllabes[-2]) == 2 and syllabes[-2][1] == 'Ǫ':
                                changements.append('j')
                            else:
                                changements.append('g')
                        #En milieu vélaire
                        else:
                            changements.append('')
                    #Le yod est déjà présent devant
                    elif syllabes[-3][-1] in ['L', 'R']:
                        if syllabes[-3] == 'TR':
                            changements.append('')
                        elif syllabes[-3] == 'CL':
                            changements.append('')
                        elif syllabes[-2][1] == 'Á':
                            changements.append('j')
                        else:
                            changements.append('')
                    #Spirantisation
                    elif syllabes[-3][-1] in ['D', 'Q', 'T']:
                        """
                        Faut voir ça
                        # changements.append('r')
                        """
                        changements.append('')
                    #La labiale sourde + yod se redouble et voit la semi-consonne se durcir en chuintante
                    elif syllabes[-3][-1] == 'P':
                        changements.append('ch')
                    elif syllabes[-3][-1] == 'S':
                        changements.append('')
                    elif syllabes[-3][-1] == 'Ẹ':
                        changements.append('')
                    #Histoires de voyelles, c'est un peu compliqué, voir si je peux débrouiller le tout
                    elif syllabes[-2][1] == 'Á':
                        if syllabes[-3][-1] in ['E', 'Ẹ']:
                            changements.append('i')
                        elif syllabes[-3][-1] == 'O':
                            changements.append('li')
                        elif syllabes[-3][-1] == 'G':
                            changements.append('')
                        elif syllabes[-3][-1] == 'C':
                            changements.append('g')
                        else:
                            changements.append('gi')
                    elif syllabes[-2][1] == 'E':
                        changements.append('g')
                    #Le reste
                    elif syllabes[-2][1] in ['C', 'Ę', 'G', 'Í', 'L', 'N', 'Ǫ', 'Ọ', 'R', 'S', 'Y']:
                        changements.append('')
                    else:
                        changements.append('i')

            #Gestion de Z
            elif syllabes[-2][0] == 'Z':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    changements.append(syllabes[-2][0])


        #Vocalisme atone
        #A
        if 'A' in syllabes[-2]:
            #Cas où il y  un préfixe
            if syllabes[-3][-1] == ' ':
                changements.append('a')
            elif syllabes[-2][0] == ' ':
                changements.append('a')
            #Cas où la longueur syllabique est d'une lettre
            elif len(syllabes[-2]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('e')
                else:
                    changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-2][-1] == 'A':
                #Si la première syllabe est un préfixe
                if syllabes[-2][0] == ' ':
                    changements.append('a')
                elif syllabes[-2][0] == 'X':
                    changements.append('a')
                # if syllabes[-2][-1] == 'N':
                    # changements.append('a')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] == 'TY':
                    changements.append('ie')
                elif len(syllabes[-1]) > 2 and syllabes[-1][-3] + syllabes[-1][-2] + syllabes[-1][-1] in ['UNT', 'WIT']:
                    changements.append('oi')
                else:
                    changements.append('e')
            #Si A se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'A':
                #Préfixe
                if syllabes[-3] == syllabes[0] in ['EM', 'EX']:
                    changements.append('a')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] == 'X':
                    changements.append('a')
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                elif syllabes[-2][-2] == syllabes[-2][0] and syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('a')
                elif syllabes[-2][-1] + syllabes[-1][0] == 'TY':
                    changements.append('ai')
                #Nasale
                elif syllabes[-2][-1] in ['M', 'N']:
                    changements.append('a')
                elif syllabes[-2][-1] == 'W':
                    changements.append('au')
                elif syllabes[-2][-1] == 'U':
                    changements.append('o')
                else:
                    changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')

        #E
        elif 'E' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('ei')
                else:
                    changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-2][-1] == 'E':
                if syllabes[-3] == syllabes[0] in ['RE', 'SE']:
                    changements.append('e')
                else:
                    changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'E':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-2][-2] == syllabes[-2][0] and syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('e')
                #S'il y a la présence d'un préfixe
                elif syllabes[-3][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('i')
                else:
                    changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-2][-1] == 'I':
                changements.append('')
            #Si I se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'I':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-2][-2] == syllabes[-2][0] and syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('i')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-2]:
            #Présence d'un préfixe
            if syllabes[-3][-1] == ' ':
                if syllabes[-2][-1] == 'Y':
                    changements.append('oi')
                else:
                    changements.append('o')
            #Cas où la longueur syllabique est d'une lettre
            elif len(syllabes[-2]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    if syllabes[-3][-1] == 'Í':
                        changements.append('o')
                    else:
                        changements.append('ou')
                #Situation de hiatus avec un Ú tonique : affaiblissement
                elif syllabes[-1][0] == 'Ú':
                    changements.append('e')
                else:
                    changements.append('o')
            #Si O se trouve en position ouvert
            elif syllabes[-2][-1] == 'O':
                #Situation de hiatus avec un Ú tonique : affaiblissement
                if syllabes[-1][0] == 'Ú':
                    changements.append('e')
                else:
                    changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'O':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-2][-2] == syllabes[-2][0] and syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('o')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('u')
                else:
                    changements.append('u')
            #Si U se trouve en position ouvert
            elif syllabes[-2][-1] == 'U':
                if syllabes[-2][-2] == ' ':
                    changements.append('u')
                else:
                    changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'U':
                #En cas de hiatus avec la tonique précédente, la voyelle devient tonique
                if syllabes[-2][-2] == syllabes[-2][0] and syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                    changements.append('u')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #Vocalisme tonique (paroxyton)
        #Á tonique
        if 'Á' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #L'absence d'un élément consonantique explosif au début de la syllabe suivante fait perdre la valeur tonique à la voyelle
                if syllabes[-1][0] in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                #Absence de diphtongaison due à une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('ai')
                elif syllabes[-3][-1] == 'I':
                    changements.append('a')
                else:
                    changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-2][-1] == 'Á':
                if syllabes[-1] == 'VIT':
                    changements.append('a')
                #Absence de diphtongaison due à une nasale
                elif syllabes[-2][0] + syllabes[-2][1] in ['GL', 'GR']:
                    changements.append('ie')
                elif syllabes[-1][0] == 'N':
                    changements.append('ai')
                elif syllabes[-1][0] + syllabes[-1][1] == 'TY':
                    if len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] == 'TY':
                        changements.append('ia')
                    else:
                        changements.append('ai')
                #Présence d'un yod
                elif syllabes[-1][1] == 'Y':
                    if syllabes[-2][-2] == 'V':
                        changements.append('iai')
                    elif syllabes[-1][0] == 'R':
                        changements.append('ie')
                    else:
                        changements.append('ai')
                #Ouverture due à un yod
                elif syllabes[-1][0] + syllabes[-1][1] in ['CL']:
                    changements.append('a')
                #Loi de Bartsch
                elif syllabes[-2][-2] in ['C', 'X']:
                    if syllabes[-3][-1] == 'O':
                        changements.append('e')
                    else:
                        changements.append('ie')
                #Présence d'un yod antéposé
                elif syllabes[-2][-2] == 'Y':
                    """
                    À vérifier
                    """
                    if syllabes[-3][-1] == 'O':
                        changements.append('e')
                    else:
                    # if len(syllabes[-2]) > 2 and syllabes[-2][-3] == 'T':
                        # changements.append('e')
                    # else:
                        changements.append('ie')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] == 'Y':
                    changements.append('ie')
                #Présence d'un yod antéposé
                elif syllabes[-3][-1] == 'Y':
                    changements.append('ie')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'Á':
                #Préfixe
                if syllabes[-2][-3] == ' ':
                    changements.append('')
                #Absence de diphtongaison du à une nasale
                elif syllabes[-2][-1] == 'N':
                    if syllabes[-1][0] == 'T':
                        changements.append('a')
                    else:
                        changements.append('ai')
                #Fermeture devant R
                elif syllabes[-2][-1] == 'R':
                    if syllabes[-2][-3] == 'Y':
                        changements.append('ie')
                    #Si ce n'est pas un verbe
                    # elif syllabes[-1][0] not in listes_lettres['toutes_les_voyelles']:
                    #     if syllabes[-2][0] == 'V':
                    #         changements.append('ai')
                    #     else:
                    #         changements.append('ie')
                    else:
                        changements.append('a')
                #Fermeture devant un wau
                elif syllabes[-2][-1] == 'W':
                    changements.append('o')
                #Diphtongaison
                elif syllabes[-2][-1] + syllabes[-1][0] == 'TY':
                    if syllabes[-2][-3] in ['N', 'M', 'Y']:
                        changements.append('a')
                    else:
                        changements.append('ai')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-2]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                if syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                #Rencontre en hiatus d'un Ī long final
                elif syllabes[-1] == 'Ī':
                    changements.append('i')
                #Rencontre en hiatus d'un U ou d'un O
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ieu')
                #Rencontre en hiatus d'un A
                elif syllabes[-1] == 'A':
                    changements.append('ei')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-2][-1] == 'Ẹ':
                #Sous l'influence d'un Ī long final (métaphonie)
                if syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                #Rencontre en hiatus d'un Ī long final
                elif syllabes[-1] == 'Ī':
                    changements.append('i')
                elif syllabes[-1][0] == 'Y':
                    changements.append('i')
                #Rencontre en hiatus d'un U ou d'un O
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ieu')
                #Rencontre en hiatus d'un A
                elif syllabes[-1] == 'A':
                    changements.append('ei')
                #Monophtongaison face à une terminaison verbale fermante
                elif syllabes[-1] in ['NÍT', 'TIS']:
                    changements.append('e')
                elif syllabes[-1] == 'NIT':
                    changements.append('i')
                #Fermeture face à une séquence dentale
                # elif len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1]:
                    # changements.append('e')
                #Pour se coller aux paradigmes verbaux
                elif syllabes[-1] == 'ANT':
                    changements.append('oi')
                elif syllabes[-1][0] + syllabes[-1][1] == 'CY':
                    changements.append('i')
                elif syllabes[-1] == 'BAT':
                    changements.append('oi')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-2][-2] == 'Ẹ':
                #Sous l'influence d'un Ī long final (métaphonie)
                if syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    #Fermeture à cause d' wau
                    if syllabes[-1][-2] == 'W':
                        changements.append('ui')
                    elif syllabes[-2][-1] + syllabes[-1][0] == 'LL':
                        changements.append('e')
                    else:
                        changements.append('i')
                #Présence d'un yod
                elif syllabes[-2][-1] == 'Y':
                    changements.append('i')
                #Normalement la séquences SCR est en position explosive de la syllabe suivante
                elif syllabes[-2][-1] == 'S':
                    if syllabes[-1][0] + syllabes[-1][1] == 'CR':
                        changements.append('ei')
                    else:
                        changements.append('e')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-1] == 'N' and syllabes[-2][-3] == 'M':
                    if syllabes[-3][-1] == 'G':
                        changements.append('e')
                    elif syllabes[-1][0] == 'T':
                        changements.append('e')
                    else:
                        changements.append('ei')
                elif syllabes[-1][0] == 'Y':
                    if syllabes[-2][-1] == 'C':
                        changements.append('i')
                    else:
                        changements.append('ei')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-2]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #Rencontre en hiatus d'un Ī long final
                if syllabes[-1] == 'Ī':
                    changements.append('i')
                #Rencontre en hiatus d'un U ou d'un O
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ieu')
                #Au contact d'un yod géminé
                elif syllabes[-1][0] == 'Y':
                    changements.append('i')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                else:
                    changements.append('ie')
            elif syllabes[-2][-1] == 'Ę':
                #Rencontre en hiatus d'un Ī long final
                if syllabes[-1] == 'Ī':
                    changements.append('i')
                #Rencontre en hiatus d'un U ou d'un O
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ieu')
                #Influence d'un Ī long final
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ui')
                #Présence d'un n mouillé avant le E ouvert
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] == 'GN':
                    changements.append('e')
                #Présence d'une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('i')
                elif syllabes[-1][0] == 'W':
                    changements.append('e')
                else:
                    changements.append('ie')
            elif syllabes[-2][-2] == 'Ę':
                #Au contact d'un yod géminé
                if syllabes[-2][-1] == 'Y':
                    changements.append('i')
                #Influence d'un Ī long final
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif syllabes[-2][-1] + syllabes[-1][0] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    if syllabes[-1][1] in ['A', 'C']:
                        changements.append('e')
                    else:
                        changements.append('i')
                elif syllabes[-2][0] + syllabes[-2][1] == 'CR' and syllabes[-2][-1] == 'S':
                    changements.append('ei')
                #Influence fermante d'un wau
                elif syllabes[-2][-1] + syllabes[-2][0] == 'QW':
                    changements.append('iu')
                #Le Ę ouvert échappe à l'action d'une nasale
                elif syllabes[-2][-1] == 'M':
                    changements.append('ie')
                else:
                    changements.append('e')
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                if syllabes[-1] == 'E':
                    changements.append('i')
                else:
                    changements.append('i')
            elif syllabes[-2][-1] == 'Í':
                if syllabes[-1] == 'E':
                    changements.append('i')
                else:
                    changements.append('i')
            elif syllabes[-2][-2] == 'Í':
                changements.append('i')
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                if syllabes[-1] == 'A':
                    changements.append('ou')
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ou')
                #Au contact d'un yod géminé
                elif syllabes[-1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                else:
                    changements.append('ou')
            elif syllabes[-2][-1] == 'Ọ':
                if syllabes[-1] == 'A':
                    changements.append('ou')
                elif syllabes[-1] in ['O', 'U']:
                    changements.append('ou')
                #Au contact d'un yod géminé
                elif syllabes[-1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('o')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                elif syllabes[-1] == 'ANT':
                    changements.append('oi')
                elif syllabes[-1][0] + syllabes[-1][1] == 'RY':
                    changements.append('oi')
                else:
                    changements.append('ou')
            elif syllabes[-2][-2] == 'Ọ':
                #Au contact d'un yod géminé
                if syllabes[-1][0] == 'Y':
                    if syllabes[-2][-1] == 'V':
                        changements.append('o')
                    elif syllabes[-2][-1] == 'N':
                        changements.append('oi')
                    else:
                        changements.append('ui')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    if syllabes[-2][-1] == 'N':
                        changements.append('oi')
                    else:
                        changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif syllabes[-2][-1] + syllabes[-1][0] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    if syllabes[-3][-1] == syllabes[0][-1] == 'A' or syllabes[-3][-2] == 'A':
                        changements.append('o')
                    else:
                        changements.append('ui')
                #Au contact d'un n mouillé
                elif syllabes[-2][-1] + syllabes[-1][0] in ['GN', 'ND', 'NG', 'YT']:
                    changements.append('oi')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                if syllabes[-1] in ['O', 'U']:
                    changements.append('ue')
                #Absence de diphtongaison du à une nasale
                elif syllabes[-1][0] == 'N':
                    changements.append('o')
                #Influence d'un Ī long final
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Au contact d'un yod géminé
                elif syllabes[-1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                else:
                    changements.append('ue')
            elif syllabes[-2][-1] == 'Ǫ':
                if syllabes[-1] in ['O', 'U']:
                    changements.append('ue')
                #Absence de diphtongaison du à une nasale
                if syllabes[-1][0] == 'N':
                    changements.append('o')
                #Influence d'un Ī long final
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Au contact d'un yod géminé
                elif syllabes[-1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[-1]) >= 2 and syllabes[-1][0] + syllabes[-1][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                elif syllabes[-2][0] == 'Y' == syllabes[-2][-2] and syllabes[-3][-1] == 'T':
                    changements.append('io')
                else:
                    changements.append('ue')
            elif syllabes[-2][-2] == 'Ǫ':
                #Au contact d'un N mouillé
                if syllabes[-2][-1] + syllabes[-1][0] in ['GN', 'NG', 'RY']:
                    changements.append('oi')
                #Anticipation du Ī long final
                elif syllabes[-1][-1] == 'Ī':
                    #Action fermant d'un wau
                    if syllabes[-1][-2] == syllabes[-1][0] == 'W':
                        changements.append('ui')
                    else:
                        changements.append('oi')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                #Rencontre en hiatus d'un Ī long final
                if syllabes[-1] == 'Ī':
                    changements.append('ui')
                #Influence d'ue nasale en position de finale absolue
                elif syllabes[-1] == 'NU':
                    changements.append('o')
                else:
                    changements.append('u')
            elif syllabes[-2][-1] == 'Ú':
                #Rencontre en hiatus d'un Ī long final
                if syllabes[-1] == 'Ī':
                    changements.append('ui')
                elif syllabes[-2][-2] == ' ':
                    changements.append('u')
                #Influence d'ue nasale en position de finale absolue
                elif syllabes[-1] == 'NU':
                    changements.append('o')
                else:
                    changements.append('u')
            elif syllabes[-2][-2] == 'Ú':
                changements.append('u')
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-2][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-2][-1] == 'B':
                #Assimilation à la consonnne suivante
                changements.append('')

            #Gestion de C
            elif syllabes[-2][-1] == 'C':
                #Quelques trucs devront sûrement être changés
                #Amuïssmeent en î
                if syllabes[-2][-2] in ['A', 'Ẹ']:
                    #Cas d'assimilation à un groupe dégageant un yod
                    if syllabes[-1][0] + syllabes[-1][1] == 'TY':
                        changements.append('')
                    elif syllabes[-1][0] + syllabes[-1][1] == 'YU':
                        changements.append('c')
                    else:
                        changements.append('i')
                #Assimilation
                else:
                    changements.append('')

            #Gestion de D
            elif syllabes[-2][-1] == 'D':
                #La dentale sonore s'assibile et se sonorise
                if syllabes[-1][0] == 'Y':
                    changements.append('i')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de F
            elif syllabes[-2][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[-2][-1] == 'G':
                if syllabes[-2] == 'RG':
                    changements.append('')
                #à voir
                elif syllabes[-2][-2] in ['E', 'I']:
                    changements.append('i')
                elif syllabes[-2][-2] in ['A', 'Á', 'O', 'U']:
                    if syllabes[-1][0] == 'Y':
                        if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('i')
                        else:
                            changements.append('')
                    else:
                        changements.append('u')
                else:
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-2][-1] == 'H':
                changements.apped('')

            #Gestion de L
            elif syllabes[-2][-1] == 'L':
                #Présence d'un yod
                if syllabes[-1][0] == 'Y':
                    if syllabes[-2][-2] == 'Á':
                        if syllabes[-1][1] == 'A':
                            changements.append('ill')
                        else:
                            changements.append('il')
                    else:
                        changements.append('ll')
                elif syllabes[-1][0] == 'L':
                    changements.append('')
                #Vocalisation en wau
                else:
                    changements.append('u')

            #Gestion de M
            elif syllabes[-2][-1] == 'M':
                if syllabes[-1][0] in ['B', 'T']:
                    changements.append('n')
                elif syllabes[-1] == 'NO':
                    changements.append('n')
                else:
                    changements.append(syllabes[-2][-1])

            #Gestion de N
            elif syllabes[-2][-1] == 'N':
                if syllabes[-2] == 'GN':
                    changements.append('')
                #Mouillure du N
                elif syllabes[-1][0] == 'Y':
                    changements.append('gn')
                elif syllabes[-1][0] + syllabes[-1][1] == 'DY':
                    changements.append('')
                else:
                    changements.append(syllabes[-2][-1])

            #Gestion de P
            elif syllabes[-2][-1] == 'P':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Q
            elif syllabes[-2][-1] == 'Q':
                #Cas rare où la lettre Q est en fin de syllabe, mais qui devrait être en position explosive
                if syllabes[-1][0] == 'W':
                    if syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                        if syllabes[-2][-2] == 'Í':
                            changements.append('f')
                        else:
                            changements.append('')
                    elif syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-1][-1] in ['T', 'S']:
                        changements.append('')
                    else:
                        changements.append('v')
                else:
                    changements.append('')

            #Gestion de R
            elif syllabes[-2][-1] == 'R':
                if syllabes[-2] in ['BR', 'CR', 'FR', 'MR', 'PR', 'SR', 'TR']:
                    changements.append('')
                #Présence d'un R dans la syllabe suivante
                elif syllabes[-1][0] == 'R':
                    changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[-2][-1])

            #Gestion de S
            elif syllabes[-2][-1] == 'S':
                if syllabes[-2] == 'WS':
                    changements.append('')
                #Présence d'un S en position explosive dans la syllabe suviante
                elif syllabes[-1][0] == 'S':
                    if syllabes[-2][-2] == 'A' and syllabes[-1][1] == 'A':
                        changements.append('s')
                    else:
                        changements.append('')
                elif syllabes[-1][0] + syllabes[-1][1] == 'TY':
                    if syllabes[-1][2] == 'A':
                        changements.append('iss')
                    else:
                        changements.append('is')
                #La sifflante avec un yod dégage vers l'avant une semi-voyelle palatale
                elif syllabes[-1][0] == 'Y':
                    if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                        changements.append('is')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-2][-1] == 'T':
                if syllabes[-2][-2] in ['A', 'Á'] and syllabes[-1][0] == 'Y':
                    if syllabes[-1][1] == syllabes[-1][-1]:
                        if syllabes[-1][1] == 'O':
                            changements.append('c')
                        elif syllabes[-1][1] == 'U':
                            changements.append('s')
                        else:
                            changements.append('')
                    elif syllabes[-1][1] == 'C':
                        changements.append('')
                    else:
                        changements.append('s')
                elif syllabes[-1][0] == 'Y':
                    changements.append('c')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de V
            elif syllabes[-2][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-2][-1] == 'W':
                if syllabes[-2][-2] == 'O':
                    changements.append('u')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de X
            elif syllabes[-2][-1] == 'X':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Y
            elif syllabes[-2][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[-2][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
