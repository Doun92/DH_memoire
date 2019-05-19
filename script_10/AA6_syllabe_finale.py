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
'CB', 'DC', 'FB', 'GB', 'HB', 'LB', 'MB', 'NB', 'PB', 'RB', 'SB', 'TB', 'VB', 'WB', 'YB',
'BC', 'DC', 'FC', 'GC', 'HC', 'LC', 'MC', 'NC', 'PC', 'RC', 'SC', 'TC', 'VC', 'WC', 'YC',
'BD', 'CD', 'FD', 'GD', 'HD', 'LD', 'MD', 'ND', 'PD', 'RD', 'SD', 'TD', 'VD', 'WD', 'YD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'HJ', 'LJ', 'MJ', 'NJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ', 'WJ', 'YJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'LL', 'ML', 'NL', 'PL', 'RL', 'SL', 'TL', 'VL', 'WL', 'YL',
'BM', 'CM', 'DM', 'FM', 'GM', 'HM', 'LM', 'MM', 'NM', 'PM', 'RM', 'SM', 'TM', 'VM', 'WM', 'YM',
'BN', 'CN', 'DN', 'FN', 'GL', 'HL', 'LN', 'MN', 'NN', 'PN', 'RN', 'SN', 'TN', 'VN', 'WN', 'YN',
'BP', 'CP', 'DP', 'FP', 'GP', 'HP', 'LP', 'MP', 'NP', 'RP', 'SP', 'TP', 'VP', 'WP', 'YP',
'BR', 'CR', 'DR', 'FR', 'GR', 'HR', 'LR', 'MR', 'NR', 'PR', 'RR', 'SR', 'TR', 'VR', 'WR', 'YR',
'BS', 'CS', 'DS', 'FS', 'GS', 'HS', 'LS', 'MS', 'NS', 'PS', 'RS', 'SS', 'TS', 'VS', 'WS', 'YS',
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'WT', 'YT',
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'WW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'WY', 'YY',
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
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'YT',
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'YY',
],


'consonantisme_explosif_complexe_3_lettres' : [
'SBR', 'SCR', 'SPR', 'STR',
],

'préfixes' : ['AD', 'IM',],


}

class SyllabeFinale:

    def __init__(self):
        return

    def syllabe_finale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Consoantisme initial
        if syllabes[-1][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-1][0] == 'B':
                if syllabes[-1] == 'BANT':
                    changements.append('')
                else:
                    #Consonantisme complexe
                    if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                        if syllabes[-1][1] == 'C':
                            changements.append('g')
                        elif syllabes[-1][1] == 'L':
                            if syllabes[-2][-1] == 'M':
                                changements.append('br')
                            else:
                                changements.append(syllabes[-1][0] + syllabes[-1][1])
                        elif syllabes[-1][1] == 'R':
                            if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                                changements.append('vr')
                            #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                            else:
                                changements.append(syllabes[-1][0] + syllabes[-1][1])
                        elif syllabes[-1][1] == 'T':
                            changements.append('d')
                        elif syllabes[-1][1] == 'W':
                            if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                                if syllabes[-1][2] == 'Ī':
                                    changements.append('')
                                else:
                                    changements.append('u')
                            else:
                                changements.append(syllabes[-1][0])
                        #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                        elif syllabes[-1][1] == 'Y':
                            #En milieu palatal
                            if syllabes[-2][-1] == 'Á':
                                if syllabes[-1][2] in ['A', 'O']:
                                    changements.append('')
                                elif syllabes[-1][2] == syllabes[-1][-1] == 'T':
                                    changements.append('t')
                                else:
                                    changements.append('v')
                            else:
                                changements.append('g')
                        else:
                            changements.append(syllabes[-1][0])
                    #Consonantisme simple
                    else:
                        #Consonne en milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Spirantisation en milieu palaral
                            if syllabes[-1][1] in ['A', 'Á', 'Ẹ', 'Ę', 'Í']:
                                if len(syllabes[-1]) > 2 and syllabes[-1][2] == syllabes[-1][-1] == 'T':
                                    if syllabes[-2] == 'A':
                                        changements.append('v')
                                    else:
                                        changements.append('')
                                elif syllabes[-2][-1] == 'Ú':
                                    changements.append('')
                                else:
                                    changements.append('v')
                            else:
                                changements.append('f')
                        #Consonantisme explosif
                        else:
                            if syllabes[-1][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('p')
                            else:
                                changements.append(syllabes[-1][0])

            #Gestion de C
            elif syllabes[-1][0] == 'C':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'L':
                        #L mouillé
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Pas besoin de I s'il est présent dans la voyelle antéposée
                            if syllabes[-2][-1] in ['Ẹ', 'Í']:
                                #Ajout d'un deuxième L en présence d'un nom féminin
                                if syllabes[-1][2] == syllabes[-1][-1] == 'A':
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                changements.append('il')
                        #Après S, la séquence se simplifie en L
                        elif syllabes[-2][-1] == 'S':
                            changements.append('l')
                        elif syllabes[-2][-1] == 'C':
                            changements.append('cl')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'N':
                        changements.append('gn')
                    elif syllabes[-1][1] == 'P':
                        if syllabes[-1][2] in ['O', 'U']:
                            changements.append('qu')
                        else:
                            changements.append('c')
                    elif syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] in ['Í']:
                                changements.append('r')
                            elif syllabes[-2][-1] == 'Á':
                                changements.append('cr')
                            else:
                                changements.append('ir')
                        #Si un Y est antéposé inorganiquement
                        elif syllabes[-2][-1] in ['N', 'R', 'S']:
                            if syllabes[-2][-2] == 'Á':
                                changements.append('cr')
                            else:
                                changements.append('tr')
                        elif syllabes[-2][-1] == 'Y':
                            changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    #Deuxième lettre = S
                    elif syllabes[-1][1] == 'S' == syllabes[-1][-1]:
                        changements.append('z')
                    #Deuxième lettre = T
                    elif syllabes[-1][1] == 'T':
                        changements.append(syllabes[-1][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'Ǫ':
                                changements.append('')
                            else:
                                changements.append('u')
                        else:
                            if syllabes[-1][2] == 'A':
                                changements.append('qu')
                            else:
                                changements.append(syllabes[-1][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-1][2] in ['U', 'O']:
                                if syllabes[-2][-1] == 'Ẹ':
                                    changements.append('c')
                                else:
                                    if syllabes[-1][-1] == 'S':
                                        changements.append('t')
                                    else:
                                        changements.append('ts')
                            elif syllabes[-1][2] == 'A':
                                if syllabes[-2][-1] == 'Ẹ':
                                    changements.append('ss')
                                else:
                                    changements.append('c')
                            else:
                                changements.append('s')
                        else:
                            if syllabes[-2][-1] in ['C', 'M', 'N']:
                                changements.append('c')
                            #Avancement du point d'articulation à cause de la dentale
                            elif syllabes[-2][-1] in ['D', 'T']:
                                changements.append('g')
                            else:
                                changements.append('')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] == 'A' and syllabes[-1][1] == 'Ę':
                            changements.append('c')
                        elif syllabes[-1][1] in ['E', 'Ẹ', 'I', 'Í']:
                            #Palatalisation de C devant E et I (le seul changement de graphie == si c'est à la fin du mot)
                            if syllabes[-1][1] == syllabes[-1][-1] :
                                changements.append('z')
                            elif len(syllabes) > 2 and syllabes[-3][-1] == 'Ẹ':
                                changements.append('s')
                            elif syllabes[-1][-1] == 'S':
                                changements.append('iz')
                            else:
                                changements.append('is')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-1][1] == 'A':
                            if syllabes[-2][-1] in ['A', 'E', 'I']:
                                changements.append('i')
                            #Après O et U
                            else:
                                changements.append('')
                        #Si les syllabes suivantes sont O ou U
                        elif syllabes[-1][1] in ['O', 'U']:
                            #Palatalisation de la vélaire sourde après Á et Í
                            if syllabes[-2][-1] in ['Á', 'A']:
                                changements.append('i')
                            elif syllabes[-2][-1] == 'Ǫ':
                                changements.append('u')
                            #Pour tout le reste
                            else:
                                changements.append('')
                        elif syllabes[-1][1] == 'Ọ':
                            changements.append('g')
                        else:
                            changements.append('')
                    else:
                        #Palatalisation de C devant A
                        if syllabes[-1][1] in ['A', 'Á']:
                            changements.append('ch')
                        elif syllabes[-2][-1] in ["C", 'L', 'M']:
                            changements.append('c')
                        elif syllabes[-2][-1] == 'N':
                            #Palatalisation de C devant A
                            if syllabes[-1][1] == syllabes[-1][-1] in ['A']:
                                changements.append('ch')
                            #Palatalisation de C après une voyelle nasale
                            elif syllabes[-2][-2] + syllabes[-2][-1] == 'EN':
                                changements.append('ch')
                            elif syllabes[-1][1] == syllabes[-1][-1] == 'U':
                                changements.append('')
                            else:
                                changements.append('c')
                        elif syllabes[-2][-2] + syllabes[-2][-1] in ['ĘY', 'ǪY']:
                            changements.append('s')
                        #Palatalisation de C devant E et I (le seul changement de graphie == si c'est à la fin du mot)
                        elif (syllabes[-1][1] == syllabes[-1][-1] in ['E', 'I']) or (syllabes[-1][1] in ['E', 'I'] and syllabes[-1][-1] == 'S'):
                            changements.append('z')
                        #Sonorisation en fin de mot
                        elif syllabes[-2][-1] == 'Y':
                            changements.append('z')
                        elif syllabes[-2][-1] == 'R':
                            changements.append('c')
                        #Devant un U atone (et donc en position de finale absolu)
                        elif syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de D
            elif syllabes[-1][0] == 'D':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'C':
                        if syllabes[-2][-1] == 'N':
                            changements.append('z')
                        else:
                            changements.append('c')
                    elif syllabes[-1][1] == 'L':
                        #Assimilation
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'O' and syllabes[-1][2] == syllabes[-1][-1] in ['A', 'U']:
                                changements.append('dl')
                            else:
                                changements.append('l')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'N':
                        changements.append('dn')
                    elif syllabes[-1][1] == 'R':
                        #Assimilation et simplification entre des voyelles
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'T':
                        changements.append('t')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2] == 'AU':
                                changements.append('')
                            else:
                                changements.append('u')
                        elif syllabes[-1][2] == 'Ī':
                            changements.append('du')
                        else:
                            changements.append(syllabes[-1][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('i')
                        #Mouillure du N
                        elif syllabes[-2][-1] == 'N':
                            changements.append('gn')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-1]) > 2 and syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-1][2] == 'S':
                            changements.append('t')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            if syllabes[-2][-1] == 'Í' and syllabes[-1][1] == 'Ę':
                                changements.append('d')
                            else:
                                changements.append('')
                    #Consonantisme explosif
                    #Les occlusives sonores à l'initiale de la syllabe s'assourdissent si elles aboutissent en finale absolue
                    elif syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-1][1] == syllabes[-1][-1]:
                        #Présence d'un yod
                        if syllabes[-2][-1] in ['P', 'Y']:
                            changements.append('')
                        elif syllabes[-2][-1] == 'G':
                            changements.append('d')
                        else:
                            changements.append('t')
                    else:
                        #En position de syllabe finale, les sonores s'assourdissent
                        if syllabes[-2][-1] in ['N', 'R']:
                            if syllabes[-1][1] in ['E', 'I']:
                                #Si un T est déjà présent, le d s'efface
                                if syllabes[-1][2] == syllabes[-1][-1] == 'T':
                                    changements.append('')
                                else:
                                    changements.append('t')
                            else:
                                changements.append('d')
                        elif syllabes[-2][-1] == 'T':
                            changements.append('t')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de F
            elif syllabes[-1][0] == 'F':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-1][1] in ['L', 'R']:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal, la fricative se sonorise
                        if syllabes[-1][1] in ['A', 'E', 'I']:
                            changements.append('v')
                        elif syllabes[-1][1] == 'Ẹ':
                            changements.append('f')
                        #Sinon, elle s'amuït
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de G
            elif syllabes[-1][0] == 'G':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-1][1] == 'L':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] in ['A', 'Á'] and syllabes[-1][2] in ['A', 'Á']:
                                changements.append('ill')
                            elif syllabes[-2][-1] == 'Ẹ' and syllabes[-1][2] == 'A':
                                changements.append('ll')
                            else:
                                changements.append('il')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'M':
                        changements.append(syllabes[-1][1])
                    #Mouillure du N
                    elif syllabes[-1][1] == 'N':
                        #En position de finale absolue
                        if syllabes[-1][2] == syllabes[-1][-1] != 'A':
                            changements.append('ng')
                        else:
                            changements.append('gn')
                    elif syllabes[-1][1] == 'R':
                        #Les palatales combinées s'affaiblissent toutes en [ir]
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Si le yod est déjà présent, pas besoin de amrquer un i supplémentaire
                            if syllabes[-2][-1] in ['Ę', 'Í']:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        elif syllabes[-2][-1] in ['L', 'N', 'R']:
                            if syllabes[-2][-2] in ['O']:
                                changements.append('gr')
                            else:
                                changements.append('dr')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'T':
                        changements.append('t')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('u')
                        elif syllabes[-1][2] == 'A':
                            changements.append('gu')
                        else:
                            changements.append(syllabes[-1][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Exception si le i est déjà présent dans la diphtongaison de la voyelle tonique
                            if syllabes[-2][-1] in ['Ẹ', 'Í', 'Ọ']:
                                changements.append('')
                            else:
                                changements.append('i')
                        elif syllabes[-2][-1] == 'N':
                            changements.append('g')
                        elif syllabes[-1][2] == syllabes[-1][-1] ==  'U':
                            changements.append('g')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de la vélaire sononre après O et devant A
                        if syllabes[-2][-1] in ['Ọ', 'O'] and syllabes[-1][1] == 'A':
                            changements.append('v')
                        #La palatale sonore s'affaiblit en milieu intervocalique
                        elif syllabes[-1][1] in ['E', 'I']:
                            changements.append('')
                        #La palatale sonore s'affaiblit jusqu'à l'amuössement devant les voyelles toniques
                        elif syllabes[-1][1] in ['Ẹ', 'Ę', 'Í']:
                            #Petite méthode pour tricher lorsqu'il faut proposer une évolution scientifique
                            if syllabes[-2][-1] == 'Í':
                                changements.append('g')
                            else:
                                changements.append('')
                        #Pour l'évolution de l'occulsive palato-vélaire devant A, il faut tenir compte le timbre de la voyelle qui précède
                        elif syllabes[-1][1] in ['A', 'Á']:
                            if syllabes[-2][-1] in ['A', 'E', 'I']:
                                changements.append('i')
                            elif syllabes[-2][-1] == 'O':
                                changements.append('v')
                            #Après 'U'
                            else:
                                changements.append('')
                        #généralement, la vélaire s'amuïse devant O et U, sauf s'il y a un i devant
                        elif syllabes[-1][1] in ['O', 'U']:
                            if syllabes[-2][-1] == 'I':
                                changements.append('i')
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    #Palatalisation de G devant A
                    elif syllabes[-1][1] in ['Á', 'O']:
                        if syllabes[-2][-1] == 'N':
                            changements.append('g')
                        else:
                            changements.append('j')
                    elif syllabes[-2][-1] == 'N':
                        #Position de finale absolue
                        if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('c')
                        elif syllabes[-1][1] in ['Í', 'Á']:
                            changements.append('g')
                        else:
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'H':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'J':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'K':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de L
            elif syllabes[-1][0] == 'L':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'M':
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    #Mouillure du L
                    elif syllabes[-1][1] == 'R':
                        changements.append('dr')
                    elif syllabes[-1][1] == 'W':
                        changements.append('l')
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-1][2] in listes_lettres['voyelles_atones_sans_A']:
                            if syllabes[-2][-1] in ['Ọ', 'Ǫ']:
                                changements.append('il')
                            elif syllabes[-2][-1] == 'L':
                                changements.append('ll')
                            else:
                                changements.append('l')
                        elif syllabes[-1][2] == 'R':
                            changements.append('l')
                        else:
                            changements.append('ll')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-2][-1] == 'M':
                        changements.append('b' + syllabes[-1][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-2][-1] == 'N':
                        if syllabes[-2][-2] == 'Í':
                            changements.append('g' + syllabes[-1][0])
                        else:
                            changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'NY':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après L
                    elif syllabes[-2][-1] == 'L':
                        if syllabes[-2][-2] == 'Ę' and syllabes[-1][1] == 'A':
                            changements.append('ll')
                        else:
                            changements.append('l')
                        # changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'LY':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-2][-1] == 'Z':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-2][-1] in ['S', 'X']:
                        if syllabes[-2][-2] in ['Ę', 'Í']:
                            changements.append('l')
                        else:
                            changements.append('t' + syllabes[-1][0])
                    #Mouillure du L
                    elif syllabes[-2][-1] == 'Y':
                        if syllabes[-2][-2] == 'Á':
                            changements.append('ill')
                        else:
                            changements.append('ll')
                    elif len(syllabes[-2]) > 2 and  syllabes[-2][-3] + syllabes[-2][-2] + syllabes[-2][-1] == 'BLĘ':
                        changements.append('au')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de M
            elif syllabes[-1][0] == 'M':
                if syllabes[-1] == 'MUS':
                    changements.append('')
                elif syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        changements.append('bre')
                    elif syllabes[-1][1] == 'Y':
                        changements.append('g')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    if syllabes[-2][-1] == 'Ǫ' and syllabes[-1][1] == 'E':
                        changements.append('n')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de N
            elif syllabes[-1][0] == 'N':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] + syllabes[-1][2] == 'GR':
                        if syllabes[-1][-1] == 'E':
                            changements.append('ndr')
                        else:
                            changements.append('ndre')
                    elif syllabes[-1][1] + syllabes[-1][2] == 'CR':
                        changements.append('ntr')
                    elif syllabes[-1][1] == 'T':
                        changements.append('nt')
                    #Mouillure du N
                    elif syllabes[-1][1] == 'Y':
                        changements.append('gn')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    #Assimilation à la consonne précédente
                    if syllabes[-2][-1] == 'M':
                        changements.append('')
                    elif syllabes[-2][-1] == 'R':
                        if syllabes[-1][1] in ['A', 'Á']:
                            changements.append('n')
                        else:
                            changements.append('')
                    elif syllabes[-2][-1] == 'Ę' and syllabes[-1][1] == 'A':
                        changements.append('nn')
                    #Mouillure du N
                    elif syllabes[-2][-1] == 'G':
                        changements.append('ng')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de P
            elif syllabes[-1][0] == 'P':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'C':
                        changements.append('c')
                    elif syllabes[-1][1] == 'L':
                        #Les labiales combinées avec l subissent une spirentisation selon les vocales autour
                        if syllabes[-2][-1] in ['Ọ', 'Ǫ']:
                            changements.append('bl')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'S':
                        changements.append('s')
                    elif syllabes[1][1] == 'T':
                        changements.append('t')
                    elif len(syllabes[-2]) > 1 and syllabes[-2][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-2][0])
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-1][1] == 'Y':
                        changements.append('ch')
                    else:
                        changements.append(syllabes[-1][0])
                #Consonantisme simple
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #Affaiblissement jusqu'à se confondre avec la sonore en milieu palatal
                        if syllabes[-1][1] in ['A', 'Á', 'Ẹ', 'Ọ']:
                            changements.append('v')
                        elif len (syllabes[-1]) > 2 and syllabes[-2][-1] == 'Ẹ' and syllabes[-1][1] + syllabes[-1][2] == 'ET':
                            changements.append('')
                        elif syllabes[-2][-1] in ['A', 'Ǫ'] and syllabes[-1][1] == 'U':
                            changements.append('')
                        #Pluriel
                        elif syllabes[-1][1] == 'Ę':
                            if syllabes[-2][-1] == 'A':
                                changements.append('v')
                            else:
                                changements.append('p')
                        else:
                            changements.append('f')
                    #Consonantisme explosif
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de Q
            elif syllabes[-1][0] == 'Q':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-1][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('v')
                        elif syllabes[-1][2] == 'A':
                            changements.append('qu')
                        else:
                            changements.append(syllabes[-1][0])
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de R
            elif syllabes[-1][0] == 'R':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][-1] == 'R':
                        if syllabes[-1][1] == 'D':
                            if syllabes[-1][2] == syllabes[-1][-1] == 'U':
                                changements.append('rt')
                            else:
                                changements.append('rd')
                        elif syllabes[-1][1] == 'Y':
                            changements.append('rg')
                        else:
                            changements.append('R' + syllabes[-1][1])
                    elif syllabes[-1][1] == 'C':
                        if syllabes[-1][2] == syllabes[-1][-1] == 'A':
                            changements.append('rg')
                        else:
                            changements.append('r')
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] == 'Ẹ':
                            changements.append('rg')
                        else:
                            changements.append('r')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-2][-1] == 'M':
                        changements.append('b' + syllabes[-1][0])
                    #Épenthèse d'un D après N
                    elif syllabes[-2][-1] == 'N':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après N mouillé
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'NY':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après L
                    elif syllabes[-2][-1] == 'L':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après L mouillé
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'LY':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un D après une sifflante sonore
                    elif syllabes[-2][-1] == 'Z' or syllabes[-2] == 'SW':
                        changements.append('d' + syllabes[-1][0])
                    #Épenthèse d'un T après une sifflante sourde
                    elif syllabes[-2][-1] in ['S', 'X']:
                        #Épenthèse d'un D après sifflante sonore
                        if syllabes[-2][-2] == 'Ǫ':
                            changements.append('d' + syllabes[-1][0])
                        else:
                            changements.append('t' + syllabes[-1][0])
                    elif syllabes[-2][-1] == 'R':
                        if syllabes[-2][-2] == 'Ǫ' and syllabes[-1][1] == 'A':
                            changements.append('r')
                        #Position de finale absolue
                        elif syllabes[-2][-2] == 'Ę' and syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('r')
                        elif syllabes[-2][-2] == 'A' and syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('')
                        else:
                            changements.append('rr')
                    elif syllabes[-2] == 'LW':
                        changements.append('dr')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de S
            elif syllabes[-1][0] == 'S':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Groupe consonantique complexe de trois lettres
                    if len(syllabes[-1]) > 2 and syllabes[-1][2] in listes_lettres['consonnes_et_semi_consonnes']:
                        changements.append(syllabes[-1][0] + syllabes[-1][1] + syllabes[-1][2])
                    else:
                        if syllabes[-1][1] == 'B':
                            changements.append('sb')
                        elif syllabes[-1][1] == 'C':
                            if syllabes[-1][2] == 'A':
                                changements.append('ch')
                            else:
                                changements.append('c')
                        elif syllabes[-1][1] == 'L':
                            changements.append('sl')
                        elif syllabes[-1][1] == 'M':
                            changements.append('sm')
                        elif syllabes[-1][1] == 'N':
                            changements.append('sn')
                        elif syllabes[-1][1] == 'R':
                            #Épenthèse de T après S
                            if syllabes[-2][-1] == 'S':
                                #Appel d'un e d'appui
                                if syllabes[-1][1] == syllabes[-1][-1]:
                                    changements.append('stre')
                                else:
                                    changements.append('str')
                            elif syllabes[-2][-1] == 'Y':
                                changements.append('sdr')
                            else:
                                changements.append('str')
                        elif syllabes[-1][1] == 'S':
                            changements.append('ss')
                        elif syllabes[-1][1] == 'T':
                            if  len(syllabes[-1]) > 2 and syllabes[-1][2] == 'R':
                                changements.append(syllabes[-1][0] + syllabes[-1][1] + syllabes[-1][2])
                            else:
                                changements.append(syllabes[-1][0] + syllabes[-1][1])
                        #Les éléments en wau perdent généralement leur semi-voyelle
                        elif syllabes[-1][1] == 'W':
                            changements.append(syllabes[-1][0])
                        #La sifflante sourde se palatalise au contact du yod
                        elif syllabes[-1][1] == 'Y':
                            if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                                changements.append('is')
                            elif syllabes[-2][-1] == 'S':
                                changements.append('ss')
                            else:
                                if syllabes[-2][-1] == 'C' and syllabes[-2][-2] == 'A' and syllabes[-3][2] == 'Á':
                                        changements.append('ssi')
                                else:
                                    changements.append('s')
                        else:
                            changements.append(syllabes[-1][1])
                else:
                    #Double ss
                    if (syllabes[-2][-1] in ['A', 'Á'] and syllabes[-1][1] in ['A','Á']) or (len(syllabes[-2]) > 2 and syllabes[-2][-2] + syllabes[-2][-1] in ['AY', 'ÁY'] and syllabes[-1][1] in ['A', 'Á']):
                        changements.append('ss')
                    #Double SS
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] in ['ES', 'ẸS'] and syllabes[-1][1] == 'A':
                        changements.append('ss')
                    #Amuïssement
                    elif syllabes[-2][-1] == 'Ǫ' and syllabes[-1][1] == syllabes[-1][-1] == 'U':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de T
            elif syllabes[-1][0] == 'T':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Avancement du point d'articulation
                    if syllabes[-1][1] == 'C':
                        changements.append('ch')
                    elif syllabes[-1][1] == 'L':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'Ẹ':
                                if syllabes[-1][2] == 'A':
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                changements.append('il')
                        elif syllabes[-2][-1] == 'T':
                            changements.append('ul')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] in ['E', 'O'] and syllabes[-1][2] in ['Á', 'Í']:
                                changements.append('rr')
                            else:
                                changements.append('r')
                        #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'S':
                        #Si la syllabe est uniquement composée de TS
                        if len(syllabes[-1]) == 2:
                            changements.append('')
                        else:
                            changements.append('ts')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'Á':
                                if syllabes[-1][-1] == 'U':
                                    changements.append('s')
                                elif syllabes[-1][-1] == 'A':
                                    changements.append('c')
                                elif syllabes[-1][-1] == 'O':
                                    changements.append('ci')
                                else:
                                    changements.append('')
                            #Le i est déjà présent dans la voyelle qui précède
                            elif syllabes[-2][-1] == 'Í':
                                if syllabes[-1][2] == 'A':
                                    changements.append('c')
                                else:
                                    changements.append('s')
                            else:
                                changements.append('is')
                        else:
                            if syllabes[-2][-1] == 'S':
                                changements.append('')
                            elif syllabes[-2][-2] + syllabes[-2][-1] == 'ĘY':
                                changements.append('s')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #Renforcement de l'attaque devant S
                        if len(syllabes[-1]) > 2 and syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-1][2] == 'S':
                            changements.append('t')
                        elif syllabes[-2][-1] in ['Ę', 'Í', 'Ǫ'] and syllabes[-1][1] == syllabes[-1][-1] == 'A':
                            changements.append('t')
                        #Amuïssement de la dentale en milieu intervocalique
                        else:
                            changements.append('')
                    #Consonantisme explosif
                    else:
                        if syllabes[-2][-2] + syllabes[-2][-1] in ['ǪY'] and syllabes[-1][1] in ['Á', 'A']:
                            changements.append('d')
                        elif syllabes[-2][-2] + syllabes[-2][-1] == 'ỌC' and syllabes[-1][1] == 'A':
                            changements.append('d')
                        elif syllabes[-2][-2] + syllabes[-2][-1] == 'ÁB' and syllabes[-1][1] == 'U':
                            changements.append('d')
                        elif syllabes[-2][-1] in ['G', 'Y'] and syllabes[-2][-2] in ['Ẹ', 'Ọ'] and syllabes[-1][1] in ['O', 'U', 'Ī']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de V
            elif syllabes[-1][0] == 'V':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] == 'L':
                            changements.append('dr')
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-1][1] == 'Y':
                        changements.append('vi')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    #Consonne en milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu vélaire, la consonne subit un amuïssement
                        if syllabes[-1][1] in ['E', 'O', 'U']:
                            if syllabes[-2][-1] == 'I':
                                changements.append('v')
                            else:
                                changements.append('f')
                        elif syllabes[-1][1] in ['Ī', 'I']:
                            changements.append('')
                        else:
                            changements.append('v')
                    else:
                        if syllabes[-2][-1] == 'R':
                            if syllabes[-1][1] == 'U':
                                changements.append('')
                            else:
                                changements.append('v')
                        elif syllabes[-2][-1] == 'L' and syllabes[-1][1] == syllabes[-1][-1] and syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('f')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de W
            elif syllabes[-1][0] == 'W':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    # if syllabes[-1][1] == 'D':
                    #     if syllabes[-2][-1] == 'Q':
                    #         if syllabes[-1][-1] not in listes_lettres['voyelles_atones']:
                    #             changements.append('que')
                    #         else:
                    #             changements.append('qu')
                    #     else:
                    #         changements.append('qu')
                    if syllabes[-1][1] == 'R':
                        #Épenthèse d'un D après L,N ou S(le wau ne compte pas vraiment)
                        if syllabes[-2][-1] in ['L', 'N', 'S']:
                            changements.append('dr')
                        else:
                            changements.append(syllabes[-1][1])
                    elif syllabes[-1][1] == 'T':
                        changements.append('ut')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    if syllabes[-1][-1] == 'Ī':
                        changements.append('')
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] in ['ǪC'] and syllabes[-1][1] in ['O', 'U']:
                        changements.append('')
                    elif syllabes[-2][-1] == 'Q':
                        if syllabes[-1][1] == syllabes[-1][-1] in ['A', 'U']:
                            changements.append('')
                        else:
                            changements.append('u')
                    elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'ĘY' and syllabes[-1][1] == 'A':
                        changements.append('v')
                    elif syllabes[-2][-1] == 'Á' and syllabes[-1][1] =='A':
                        changements.append('v')
                    else:
                        changements.append('')

            #Gestion de X
            elif syllabes[-1][0] == 'X':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles'] and syllabes[-1][1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] == 'A' and syllabes[-1][1] == 'Ī':
                            changements.append('x')
                        elif syllabes[-2][-1] == 'Ę' and syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('s')
                        else:
                            changements.append('ss')
                    else:
                        changements.append('s')

            #Gestion de Y
            elif syllabes[-1][0] == 'Y':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'C':
                        if syllabes[-1][2] in ['A', 'Á']:
                            changements.append('ch')
                        #Spirantisation
                        elif syllabes[-2][-2] + syllabes[-2][-1] == 'ĘD':
                            changements.append('r')
                        elif syllabes[-2][-2] + syllabes[-2][-1] in ['ẸN', 'ỌN']:
                            changements.append('')
                        else:
                            changements.append('g')
                    #Épenthèse d'un D après L
                    elif syllabes[-1][1] == 'D':
                        if syllabes[-1][1] == syllabes[-1][-1]:
                            changements.append('')
                        else:
                            changements.append('d')
                    elif syllabes[-1][1] == 'L':
                        if syllabes[-2][-2] + syllabes[-2][-1] == 'ĘC':
                            changements.append('ill')
                        else:
                            changements.append('l')
                    elif syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] == 'L':
                            changements.append('DR')
                        else:
                            changements.append('r')
                    elif syllabes[-1][1] == 'T':
                        if syllabes[-2][-1] in ['L', 'S', 'Y']:
                            changements.append('t')
                        else:
                            changements.append('d')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] in ['Ę', 'Í', 'Ǫ', 'Ọ']:
                            changements.append('e')
                        else:
                            changements.append('i')
                    #La labiale sonore + yod agit différemment selon son enoturage vocalique
                    elif syllabes[-2][-2] + syllabes[-2][-1] == 'BR':
                        if syllabes[-3][-1] == 'Ẹ':
                            changements.append('')
                        else:
                            changements.append('g')
                    elif syllabes[-2][-1] in ['B', 'V']:
                        #En milieu palatal
                        if syllabes[-2][-2] in ['A', 'Ọ']:
                            if syllabes[-1][1] == syllabes[-1][-1] == 'A':
                                changements.append('')
                            elif syllabes[-1][1] == 'Í':
                                changements.append('')
                            else:
                                changements.append('g')
                        #En milieu vélaire
                        else:
                            changements.append('')
                    #Le yod est déjà présent devant
                    elif syllabes[-2][-1] in ['D', 'Q', 'T']:
                        changements.append('')
                    elif syllabes[-2][-1] in ['L', 'R']:
                        if syllabes[-2] in ['BR', 'TR']:
                            changements.append('')
                        # elif syllabes[-2] == 'BR':
                            # changements.append('g')
                        elif syllabes[-2][-2] == 'Ẹ':
                            if syllabes[-1][1] == syllabes[-1][-1] == 'A':
                                changements.append('')
                            else:
                                changements.append('g')
                        elif syllabes[-1][1] == 'Á':
                            changements.append('j')
                        else:
                            changements.append('')
                    #Histoires de voyelles, c'est un peu compliqué, voir si je peux débrouiller le tout
                    #La labiale sourde + yod se redouble et voit la semi-consonne se durcir en chuintante
                    elif syllabes[-2][-1] == 'P':
                        changements.append('ch')
                    elif syllabes[-1][1] == 'Á':
                        if syllabes[-2][-1] in ['E', 'Ẹ']:
                            changements.append('i')
                        elif syllabes[-2][-1] == 'O':
                            changements.append('li')
                        elif syllabes[-2][-1] == 'G':
                            changements.append('')
                        elif syllabes[-2][-1] == 'C':
                            changements.append('g')
                        else:
                            changements.append('gi')
                    elif syllabes[-2][-1] == 'E':
                        changements.append('g')
                    #Le reste
                    elif syllabes[-2][-1] in ['C', 'G', 'L', 'N', 'R', 'S', 'T', 'Y']:
                        if syllabes[-2][-1] == 'T' and syllabes[-1][1] == syllabes[-1][-1] == 'O':
                            changements.append('i')
                        else:
                            changements.append('')
                    #Spirantisation
                    elif syllabes[-2][-1] == 'D':
                        changements.append('r')
                    #Renforcement du yod en position finale
                    elif syllabes[-1][1] == syllabes[-1][-1] == 'U':
                        if syllabes[-2][-2] == 'Ǫ':
                            changements.append('i')
                        elif syllabes[-2][-2] == 'Ę':
                            changements.append('')
                        else:
                            changements.append('g')
                    else:
                        changements.append('i')

            #Gestion de Z
            elif syllabes[-1][0] == 'Z':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    changements.append(syllabes[-1][0])


        #Vocalisme atone
        #A
        if 'A' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-1][-1] == 'A':
                changements.append('e')
            #Si A se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'A':
                #Cas où la dernière syllabe est la terminaison à la troisième personne de l'indicatif imparfait
                if syllabes[-1] == 'BAT':
                    changements.append('')
                elif syllabes[-1][-1] in ['M', 'N']:
                    changements.append('a')
                else:
                    changements.append('e')
            #Tous les autres cas de figure
            else:
                if syllabes[-1] == 'BANT':
                    changements.append('oie')
                elif syllabes[-1][-2] + syllabes[-1][-1] == 'CS':
                    changements.append('a')
                else:
                    changements.append('e')
        #E
        elif 'E' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-1][-1] == 'E':
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    if syllabes[-2][-2] + syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] in ['VẸDR', 'ǪSPT']:
                        changements.append('')
                    else:
                        changements.append('e')
                #Autres groupes consonatiques qui ont besoin d'un e d'appui
                elif syllabes[-2][-1] + syllabes[-1][0] in ['DC', 'DM', 'LC', 'LR', 'SL', 'SR', 'MC', 'MN', 'MT', 'NR', 'WN', 'WR', 'YN', 'YR']:
                    changements.append('e')
                else:
                    changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'E':
                #Mots au pluriel
                if syllabes[-1][-1] == 'S':
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-1][-1] == 'I':
                if len(syllabes[-1]) > 2:
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Si I se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'I':
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    changements.append('e')
                elif syllabes[-1][0] == 'T' and syllabes[-1][2] == 'S':
                    changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                #Fermeture conditionnée en position de finale absolue
                if syllabes[-2][-1] == 'Í':
                    if len(syllabes) > 2:
                        #Fermeture du mot en [on]
                        changements.append('on')
                    else:
                        changements.append('u')
                else:
                    changements.append('')
            #Si O se trouve en position ouvert
            elif syllabes[-1][-1] == 'O':
                if len(syllabes[-1]) > 2:
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        #Si si cela se termine par un L mouillé
                        if syllabes[-1][0] + syllabes[-1][1] in ['CL', 'CY', 'GR', 'GY']:
                            if syllabes[-2][-1] == 'S':
                                changements.append('e')
                            else:
                                changements.append('')
                        elif syllabes[-1][0] + syllabes[-1][1] == 'TY':
                            changements.append('on')
                        else:
                            changements.append('e')
                    else:
                        changements.append('')
                else:
                    if syllabes[-2][-1] == 'Ú' and syllabes[-1][0] == 'G':
                        changements.append('e')
                    elif syllabes[-1][0] == 'Y':
                        if syllabes[-2][-1] == 'C':
                            changements.append('')
                        #So un mot se termine par la séquence RYO, le r a besoin d'un e d'appui, sauf s'il y a la présence d'un Á tonique précédent
                        elif syllabes[-2][-1] == 'R':
                            if syllabes[-2][-2] == 'Á':
                                changements.append('')
                            else:
                                changements.append('e')
                        else:
                            changements.append('on')
                    else:
                        changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'O':
                if syllabes[-1][-1] == 'S':
                    if syllabes[-2][-1] + syllabes[-1][-3] == 'QW':
                        changements.append('e')
                    else:
                        changements.append('')
                elif syllabes[-1][0] == syllabes[-1][-2]:
                    if syllabes[-2][-1] == 'Ę':
                        changements.append('U')
                    else:
                        changements.append('')
                elif len(syllabes[-1]) > 3:
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        #Si si cela se termine par un L mouillé
                        if syllabes[-1][0] + syllabes[-1][1] in ['CL', 'CY']:
                            changements.append('')
                        else:
                            changements.append('e')
                    else:
                        changements.append('')
                # elif syllabes[-1][-1] == 'S':
                #     changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                if syllabes[-2][-1] == 'Ę':
                    changements.append('u')
                else:
                    changements.append('e')
            #Si U se trouve en position ouvert
            elif syllabes[-1][-1] == 'U':
                #Exceptions dont je ne sais que faire
                if syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] in ['RPS', 'RRD', 'YYL']:
                    changements.append('')
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                elif len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    #Exceptions
                    if syllabes[-1][0] + syllabes[-1][1] in ['CL', 'CT', 'TL']:
                        if syllabes[-2][-1] in ['R', 'S']:
                            changements.append('e')
                        else:
                            changements.append('')
                    elif syllabes[-1][0] + syllabes[-1][1] in ['GY', 'LY', 'TY', 'RY', 'SY']:
                        if syllabes[-2][-1] in ['Ẹ', 'R', 'L']:
                            changements.append('e')
                        else:
                            changements.append('')
                    else:
                        changements.append('e')
                #Autres conditions demandant un e d'appui
                elif len(syllabes[-2]) > 2 and syllabes[-2][-2] + syllabes[-2][-1] + syllabes[-1][0] in ['BRY', 'FRY', 'ẸGD', 'ĘPD', 'ẸNC', 'ĘRY']:
                    changements.append('e')
                elif len(syllabes[-2]) == 2 and syllabes[-1][0] == syllabes[-1][-2] == 'Y':
                    changements.append('e')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-2] + syllabes[-2][-1] + syllabes[-1][0] == 'ẸLL':
                    if syllabes[-2][-3] in ['G']:
                        changements.append('e')
                    else:
                        changements.append('')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['BT', 'CN', 'NC', 'PD', 'PT', 'SN', 'VV', 'WR', 'XM', 'XN', 'NT']:
                    if syllabes[-2][-2] in ['Á', 'E', 'Ẹ', 'Ę', 'Í']:
                        changements.append('')
                    else:
                        changements.append('e')
                elif syllabes[-2][-1] + syllabes[-1][0] == 'ĘW':
                    changements.append('u')
                #Condition qui nécessitent un E d'appui
                elif syllabes[-1][-2] in ['Y']:
                    #Exceptions
                    if syllabes[-2][-1] in ['D', 'G', 'L', 'Q', 'R', 'S', 'T', 'W', 'Y']:
                        if syllabes[-2][-2] == 'Ẹ':
                            changements.append('e')
                        else:
                            changements.append('')
                    else:
                        changements.append('e')
                elif syllabes[-1][0] == syllabes[-1][1]:
                    changements.append('e')
                #Autres conditions demandant un e d'appui
                # elif syllabes[-2][-1] + syllabes[-1][0] in ['CN', 'SN']:
                #     changements.append('e')
                else:
                    changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'U':
                if syllabes[-1] == 'MUS':
                    changements.append('ons')
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                elif len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    #Exceptions : Présence de yod avant
                    if syllabes[-1][0] + syllabes[-1][1] in ['CL', 'LY', 'RY', 'SY', 'TY']:
                        if syllabes[-2][-1] in ['N', 'Ọ', 'R', 'S']:
                            changements.append('e')
                        else:
                            changements.append('')
                    elif syllabes[-1][0] + syllabes[-1][1] == 'CT':
                        changements.append('')
                    else:
                        changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                if syllabes[-2][-1] + syllabes[-1][0] == 'WW':
                    changements.append('')
                else:
                    changements.append('e')

        #Vocalisme tonique (oxyton)
        #Á tonique
        if 'Á' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-1][-1] == 'Á':
                #Loi de Bartsch
                if syllabes[-1][-2] in ['C', 'X']:
                    if syllabes[-2][-1] == 'O':
                        changements.append('e')
                    else:
                        changements.append('ie')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'Á':
                #Présence d'un yod antéposé
                if syllabes[-2][-1] == 'Y':
                    changements.append('ie')
                #Fermeture devant un wau
                elif syllabes[-1][-1] == 'W':
                    changements.append('o')
                #Diphtongaison lorsque c'est un imparfait
                elif syllabes[-1][-1] == 'T':
                    changements.append('oi')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                if syllabes[-1][-2] + syllabes[-1][-1] == 'TS':
                    if len(syllabes[-1]) > 3 and syllabes[-1][-4] == 'Y':
                        changements.append('ie')
                    elif syllabes[-2] == syllabes[0] == 'PRI':
                        changements.append('a')
                    else:
                        changements.append('e')
                else:
                    changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-1]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-1][-1] == 'Ẹ':
                changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-1][-2] == 'Ẹ':
                changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-1]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('ie')
            elif syllabes[-1][-1] == 'Ę':
                changements.append('ie')
            elif syllabes[-1][-2] == 'Ę':
                #Le Ę ouvert échappe à l'action d'une nasale
                if syllabes[-1][-1] == 'M':
                    changements.append('ie')
                elif syllabes[-1][-1] == 'T':
                    changements.append('oi')
                else:
                    changements.append('e')
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('i')
            elif syllabes[-1][-1] == 'Í':
                changements.append('i')
            elif syllabes[-1][-2] == 'Í':
                changements.append('i')
            else:
                changements.append('i')

        #Ī long final
        elif 'Ī' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('')
            elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] in ['ẸW', 'ẸG', 'WS']:
                changements.append('')
            elif syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                if syllabes[-1][0] + syllabes[-1][1] in ['BW', 'DW']:
                    changements.append('i')
                else:
                    changements.append('')
            elif syllabes[-1][-2] in ['L', 'T', 'W', 'X']:
                if syllabes[-2][-1] in ['L', 'N', 'S', 'T']:
                    changements.append('')
                else:
                    changements.append('i')
            else:
                changements.append('')

        #Ọ fermé
        elif 'Ọ' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('ou')
            elif syllabes[-1][-1] == 'Ọ':
                changements.append('ou')
            elif syllabes[-1][-2] == 'Ọ':
                changements.append('o')
            else:
                changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('ue')
            elif syllabes[-1][-1] == 'Ǫ':
                changements.append('ue')
            elif syllabes[-1][-2] == 'Ǫ':
                if syllabes[-1][-3] == 'Y':
                    if syllabes[-1][-1] == 'R':
                        changements.append('o')
                    else:
                        changements.append('ou')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('u')
            elif syllabes[-1][-1] == 'Ú':
                changements.append('u')
            elif syllabes[-1][-2] == 'Ú':
                changements.append('u')
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-1][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-1][-1] == 'B':
                #Assimilation à la consonnne suivante
                changements.append('')

            #Gestion de C
            elif syllabes[-1][-1] == 'C':
                #Quelques trucs devront sûrement être changés
                #Amuïssmeent en î
                if syllabes[-1][-2] in ['A', 'Ẹ']:
                    changements.append('i')
                elif syllabes[-1][-2] == 'N':
                    changements.append('nc')
                #Assimilation
                else:
                    changements.append('')

            #Gestion de D
            elif syllabes[-1][-1] == 'D':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de F
            elif syllabes[-1][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[-1][-1] == 'G':
                if syllabes[-1][-2] == 'R':
                    changements.append('rc')
                #à voir
                elif syllabes[-1][-2] in ['E', 'I']:
                    changements.append('i')
                elif syllabes[-1][-2] in ['A', 'Á', 'O', 'U']:
                    changements.append('u')
                else:
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-1][-1] == 'H':
                changements.apped('')

            #Gestion de L
            elif syllabes[-1][-1] == 'L':
                if syllabes[-1][-2] == 'L':
                    changements.append('l')
                else:
                    changements.append('')

            #Gestion de M
            elif syllabes[-1][-1] == 'M':
                changements.append('n')

            #Gestion de N
            elif syllabes[-1][-1] == 'N':
                changements.append(syllabes[-1][-1])

            #Gestion de P
            elif syllabes[-1][-1] == 'P':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de R
            elif syllabes[-1][-1] == 'R':
                if syllabes[-1] in ['BR', 'CR', 'FR', 'MR', 'SR', 'TR']:
                    changements.append('')
                elif syllabes[-1] == 'YR':
                    changements.append('e')
                #Demande un e d'appui
                elif syllabes[-1][0] + syllabes[-1][1] == 'YO':
                    changements.append('re')
                #Épenthèse d'un d après L
                elif syllabes[-1][0] + syllabes[-1][1] == 'LY':
                    changements.append('dre')
                #Épenthèse d'un D après L
                elif syllabes[-2] == 'LI':
                    changements.append('dre')
                #La vibrante est très stable
                else:
                    changements.append(syllabes[-1][-1])

            #Gestion de S
            elif syllabes[-1][-1] == 'S':
                if syllabes[-1] == 'MUS':
                    changements.append('')
                elif syllabes[-1] == 'CS':
                    changements.append('')
                elif syllabes[-1][0] + syllabes[-1][1] == 'CE':
                    changements.append('')
                elif syllabes[-1][-2] + syllabes[-1][-1] in listes_lettres['consonantisme_implosif_complexe_2_lettres']:
                    if syllabes[-1][-2] == 'C':
                        changements.append('z')
                    elif syllabes[-1][-2] == 'Y':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][-2] + syllabes[-1][-1])
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-1][-1] == 'T':
                if syllabes[-1] == 'BAT':
                    changements.append('t')
                #Pour les verbes
                elif syllabes[-1][-2] == 'N':
                    changements.append('nt')
                elif syllabes[-1][-2] in ['Á', 'E', 'Ę', 'I', 'Í']:
                    changements.append('t')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de V
            elif syllabes[-1][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-1][-1] == 'W':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de X
            elif syllabes[-1][-1] == 'X':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Y
            elif syllabes[-1][-1] == 'Y':
                if syllabes[-1][-2] == 'N':
                    changements.append('ng')
                elif syllabes[-1][-2] == 'Á':
                    changements.append('ille')
                else:
                    #Amüissement de la semi-consonne
                    changements.append('')

            #Gestion de Z
            elif syllabes[-1][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
