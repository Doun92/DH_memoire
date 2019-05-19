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
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú", 'W', 'Y'],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes' : ['B', 'C', 'D', 'F', 'G', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z'],

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

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
'SBR', 'SCR', 'SDR', 'SLR', 'SPR', 'STR',
],

}

class SyllabeInitiale:

    def __init__(self):
        return

    def syllabe_initiale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Consoantisme initial
        if syllabes[0][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[0][0] == 'B':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[0][1] in ['L', 'R']:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Les occlusives sonores combinées au yod trouvent leur point d'équilibre dans la zone palatale
                    elif syllabes[0][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de C
            elif syllabes[0][0] == 'C':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] == 'H':
                        changements.append('ch')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[0][1] in ['L', 'R']:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[0][1] == 'Y':
                        #Ajout d'un signe diacritique devant A et O
                        if len(syllabes) > 1 and syllabes[1][0] in ['A', 'O']:
                            changements.append('ç')
                        elif syllabes[0][2] in ['A', 'O']:
                            changements.append('ç')
                        else:
                            changements.append('c')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    #Palatalisation de C devant A
                    if syllabes[0][1] in ['A', 'Á']:
                        #Avancement du point d'articulation
                        # if len(syllabes[0]) > 2 and syllabes[0][2] == 'R':
                            # changements.append('g')
                        # else:
                            changements.append('ch')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de D
            elif syllabes[0][0] == 'D':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[0][1] == 'R':
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[0][1] == 'Y':
                        if syllabes[0][2] == 'A':
                            changements.append('de')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de F
            elif syllabes[0][0] == 'F':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[0][1] in ['L', 'R']:
                        if syllabes[1][0] + syllabes[1][1] == 'GR':
                            changements.append('fl')
                        else:
                            changements.append(syllabes[0][0] + syllabes[0][1])
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de G
            elif syllabes[0][0] == 'G':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[0][1] in ['L', 'R']:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Mouillure du N
                    elif syllabes[0][1] == 'N':
                        changements.append('gn')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[0][1] == 'Y':
                        if syllabes[0][2] == 'Ǫ':
                            changements.append('ge')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    #Palatalisation de G devant A en position initiale absolue
                    if syllabes[0][1] == 'A':
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'H':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][1])
                else:
                    changements.append('')

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'J':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'K':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] == 'W':
                        changements.append('qu')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de L
            elif syllabes[0][0] == 'L':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de M
            elif syllabes[0][0] == 'M':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de N
            elif syllabes[0][0] == 'N':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de P
            elif syllabes[0][0] == 'P':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[0][1] in ['L', 'R']:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[0][1] == 'Y':
                        changements.append('ch')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de Q
            elif syllabes[0][0] == 'Q':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[0][1] == 'W':
                        if syllabes[0][2] in ['A', 'Ọ']:
                            changements.append('c')
                        else:
                            changements.append('qu')
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[0][0])

            #Gestion de R
            elif syllabes[0][0] == 'R':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de S
            elif syllabes[0][0] == 'S':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] + syllabes[0][2] == 'CL':
                        changements.append('escl')
                    elif syllabes[0][1] + syllabes[0][2] == 'TR':
                        changements.append('estr')
                    elif syllabes[0][1] + syllabes[0][2] == 'CR':
                        changements.append('escr')
                    elif syllabes[0][1] == 'C':
                        if syllabes[0][2] in ['A', 'Á']:
                            changements.append('esch')
                        else:
                            changements.append('esc')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #La sifflante sourde se palatalise au contact du yod
                    elif syllabes[0][1] == 'Y':
                        changements.append('s')
                    else:
                        #Prosthèse
                        changements.append('e'+ syllabes[0][0] + syllabes[0][1])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de T
            elif syllabes[0][0] == 'T':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] == 'C':
                        changements.append('c')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[0][1] == 'R':
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[0][1] == 'Y':
                        if syllabes[0][2] in ['A', 'O', 'Ọ']:
                            changements.append('ç')
                        elif syllabes[1][0] in ['A', 'O', 'Ọ']:
                            changements.append('ç')
                        else:
                            changements.append('c')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de V (wau ancien)
            elif syllabes[0][0] == 'V':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    if syllabes[0][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    if syllabes[0][1] == 'A':
                        if len(syllabes[0]) > 2 and syllabes[0][2] in ['D', 'L', 'S']:
                            changements.append('v')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de W (wau récent) (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'W':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    if syllabes[0][1] in ['Á', 'Ẹ', 'Í']:
                        changements.append('gu')
                    else:
                        changements.append('g')

            #Gestion de X (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'X':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de Y (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'Y':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    if syllabes[0][1] == 'Á':
                        changements.append('gi')
                    # elif syllabes[0][1] == 'E':
                    #     changements.append('g')
                    else:
                        changements.append('j')

            #Gestion de Z (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'Z':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

        #Vocalisme contretonique
        #A
        if 'A' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #Situation de hiatus : affaiblissement
                if len(syllabes) > 1 and syllabes[1][0] in ['Ú', 'W']:
                    changements.append('e')
                else:
                    changements.append('a')
            #Si A se trouve en position ouvert
            elif syllabes[0][-1] == 'A':
                #Situation de hiatus : affaiblissement
                if len(syllabes) > 1 and syllabes[1][0] in ['Ọ', 'Ú', 'V', 'W']:
                    if syllabes[0][-2] == 'L':
                        changements.append('a')
                    else:
                        changements.append('e')
                #Fermeture du A contretonique en certaines situations
                elif syllabes[0][-2] in ['C', 'G']:
                    if len(syllabes) > 1 and syllabes[1][0] in ['N', 'P', 'T']:
                        if syllabes[1][1] in ['Ẹ', 'R']:
                            changements.append('e')
                        else:
                            changements.append('a')
                    elif syllabes[1] == 'Ẹ':
                        changements.append('a')
                    else:
                        changements.append('e')
                #Fermeture due à une attaque
                elif syllabes[0][0] + syllabes[0][1] == 'FR':
                    if syllabes[1][0] + syllabes[1][1] == 'GỌ':
                        changements.append('e')
                    else:
                        changements.append('a')
                elif syllabes[0][0] + syllabes[0][1] == 'SM':
                    changements.append('e')
                # elif syllabes[0][0] + syllabes[0][1] in ['FR', 'SM']:
                    # changements.append('e')
                # else:
                    # changements.append('a')
                else:
                    changements.append('a')
            #Si A se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'A':
                if syllabes[0][-1] == 'U':
                    changements.append('o')
                elif syllabes[0][-1] == 'C':
                    if len(syllabes) > 1 and syllabes[1][0]:
                        changements.append('a')
                    else:
                        changements.append('ai')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'SY':
                    changements.append('ai')
                elif syllabes[0][-1] == 'G' == syllabes[-1][-1]:
                    changements.append('o')
                #En présence d'un yod
                elif syllabes[0][-1] in ['X', 'Y']:
                    changements.append('ai')
                #Influence d'une nasale
                elif syllabes[0][-1] == 'N':
                    # if syllabes[1][1] == 'Y':
                        # changements.append('ai')
                    if syllabes[1][0] == 'B':
                        changements.append('ai')
                    elif syllabes[1][0] + syllabes[1][1] in ['DY', 'SY']:
                        changements.append('ai')
                    else:
                        changements.append('a')
                elif syllabes[0][-1] == 'P':
                    if syllabes[1][0] == 'W':
                        changements.append('o')
                    else:
                        changements.append('a')
                elif syllabes[0][-1] == 'S':
                    if len(syllabes[0]) > 2 and syllabes[0][-3] == syllabes[0][0] == 'C':
                        changements.append('a')
                    elif len(syllabes) > 1 and syllabes[1][1] == 'Y':
                        changements.append('ai')
                    elif syllabes[0][0] + syllabes[0][1] == 'TR':
                        changements.append('e')
                    else:
                        changements.append('a')
                elif syllabes[0][-1] == 'T':
                    if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                        changements.append('ai')
                    else:
                        changements.append('a')
                #Action fermante due due au wau
                elif len(syllabes) > 1 and syllabes[0][-1] == 'W' and syllabes[1][0] == 'W':
                    if len(syllabes[0]) > 2 and syllabes[0][0] == 'S' or syllabes[1][1] == 'S':
                        changements.append('e')
                    else:
                        changements.append('o')
                else:
                    changements.append('a')
            #Tous les autres cas de figure
            else:
                if (len(syllabes[0]) > 2 and syllabes[0][-3] + syllabes[0][-2] == 'AU') or (len(syllabes[0]) > 3 and syllabes[0][-4] + syllabes[0][-3] == 'AU'):
                    if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                        changements.append('oi')
                    else:
                        changements.append('o')
                elif len(syllabes[0]) > 2 and syllabes[0][-2] + syllabes[0][-1] == 'PD':
                    changements.append('o')
                elif len(syllabes) == 1 and syllabes[0][-2] + syllabes[0][-1] == 'ST':
                    changements.append('ai')
                else:
                    changements.append('a')

        #E
        elif 'E' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                if syllabes[1][0] + syllabes[1][1] == 'XÍ':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si E se trouve en position ouvert
            elif syllabes[0][-1] == 'E':
                changements.append('e')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'E':
                if syllabes[0][-1] == 'Y':
                    changements.append('ei')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['NY', 'TY']:
                    changements.append('ei')
                elif len(syllabes) > 1 and syllabes[0][-1] == 'W' and syllabes[1][0] == 'W':
                    changements.append('')
                else:
                    changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')

        #I
        elif 'I' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('i')
            #Si I se trouve en position ouvert
            elif syllabes[0][-1] == 'I':
                changements.append('i')
            #Si I se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'I':
                changements.append('i')
            #Tous les autres cas de figure
            else:
                changements.append('i')

        #O
        elif 'O' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #Situation de hiatus avec un Ú tonique : affaiblissement
                if syllabes[1][0] == 'Ú':
                    changements.append('e')
                else:
                    changements.append('o')
            #Si O se trouve en position ouvert
            elif syllabes[0][-1] == 'O':
                #Situation de hiatus avec un Ú tonique : affaiblissement
                if len(syllabes) > 1 and syllabes[1][0] == 'Ú':
                    changements.append('e')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'DY':
                    changements.append('u')
                else:
                    changements.append('o')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'O':
                #Présence d'un wau
                if syllabes[0][-1] == 'W':
                    if syllabes[0][-3] == 'L':
                        changements.append('o')
                    else:
                        changements.append('e')
                elif syllabes[0][-1] == 'Y':
                    changements.append('ou')
                else:
                    changements.append('o')
            #Tous les autres cas de figure
            else:
                changements.append('o')

        #U
        elif 'U' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('u')
            #Si U se trouve en position ouvert
            elif syllabes[0][-1] == 'U':
                #Si c'est une diphtongue
                if syllabes[0][-2] == 'A':
                    changements.append('')
                else:
                    changements.append('u')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'U':
                changements.append('u')
            #Tous les autres cas de figure
            else:
                changements.append('u')

        #Vocalisme tonique
        #Á tonique
        if 'Á' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #Absence de diphtongaison due à une nasale
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'BW':
                    changements.append('o')
                else:
                    changements.append('a')
            #Si A tonique se trouve en position ouverte
            elif syllabes[0][-1] == 'Á':
                if syllabes[0][0] + syllabes[0][1] == 'ST':
                    changements.append('e')
                elif syllabes[0][0] + syllabes[0][1] == 'SW':
                    changements.append('a')
                #Loi de Bartsch
                elif syllabes[0][-2] in ['X', 'C']:
                    changements.append('ie')
                #Absence de diphtongaison due à une nasale
                elif len(syllabes) > 1 and syllabes[1][0] in ['C', 'M', 'N']:
                    if syllabes[1][1] in ['R', 'Y']:
                        changements.append('a')
                    else:
                        changements.append('ai')
                #Présence d'un yod
                elif len(syllabes) > 1 and syllabes[1][1] == 'Y':
                    changements.append('ai')
                #Ouverture due à un yod
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CE', 'CL']:
                    changements.append('a')
                #Fermuture de Á tonique libre à cause de l'action fermante d'un wau en position finale
                elif len(syllabes) == 2 and syllabes[1][0] == 'W':
                    changements.append('ou')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'Á':
                #Absence de diphtongaison du à une nasale
                if syllabes[0][-1] == 'N':
                    if syllabes[0][0] + syllabes[0][1] in ['GR', 'QW']:
                        changements.append('a')
                    elif syllabes[1][0] + syllabes[1][1] == 'CR':
                        changements.append('a')
                    else:
                    # if syllabes[0][-1] in ['M', 'N']:
                        # changements.append('a')
                    # else:
                        changements.append('ai')
                elif len(syllabes) > 1 and syllabes[0][-1] == 'S' and syllabes[1][0] == 'Y':
                    changements.append('ai')
                #Fermeture devant un wau
                elif syllabes[0][-1] == 'W':
                    changements.append('o')
                #Fermeture à cause de la palatale précédente
                elif len(syllabes[0]) > 2 and syllabes[0][0] == syllabes[0][-3] == 'C':
                    changements.append('e')
                #Anticipation d'un Ī long final
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Cas particulier face à un Q en dernière position alors qu'il devrait appartenir à la prochaine syllabe
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'QW':
                    changements.append('e')
                elif len(syllabes) == 1 and syllabes[0][-1] == 'T':
                    changements.append('e')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                if syllabes[0][-3] + syllabes[0][-2] == 'ÁN':
                    changements.append('ai')
                elif syllabes[0][-2] + syllabes[0][-1] == 'PT':
                    changements.append('e')
                else:
                    changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[0]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #Sous l'influence d'un Ī long final (métaphonie)
                if syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                #Au contact direct avec un Ī long final (métaphonie)
                elif syllabes[1] == syllabes[-1] == 'Ī':
                    changements.append('i')
                #Influence d'un yod
                elif syllabes[1] == 'BR' and syllabes[2][0] == 'Y':
                    changements.append('i')
                #Au contact d'autre éléments dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] == 'CR':
                    changements.append('e')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[0][-1] == 'Ẹ':
                #Sous l'influence d'un Ī long final (métaphonie)
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    if syllabes[1][0] + syllabes[1][1] == 'BW':
                        changements.append('u')
                    else:
                        changements.append('i')
                #Au contact direct avec un Ī long final (métaphonie)
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] == 'Ī':
                    changements.append('i')
                #Au contact d'autre éléments dégageant un yod
                elif len(syllabes) > 1 and len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] == 'CR':
                    changements.append('e')
                #Monophtongaison en position finale
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] in ['SIT', 'SU']:
                    changements.append('i')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'LY':
                    changements.append('i')
                #Nasalisation
                elif len(syllabes) > 1 and syllabes[1][0] == 'N':
                    if syllabes[1] == syllabes[-1] == 'NIT':
                        changements.append('i')
                    #Diphtongaison face à la fin d'un mot
                    elif len(syllabes) == 2 and (syllabes[1][1] == syllabes[1][-1] == 'A'):
                        changements.append('ei')
                    else:
                        changements.append('e')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[0][-2] == 'Ẹ':
                #Sous l'influence d'un Ī long final (métaphonie)
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    #Fermeture à cause d' wau
                    if syllabes[-1][-2] == 'W':
                        if syllabes[0][-1] == 'N':
                            changements.append('i')
                        else:
                            changements.append('ui')
                    else:
                        changements.append('i')
                #Présence d'un yod
                elif syllabes[0][-1] == 'Y':
                    #Puissance articulatoire plus frande grâce au groupe consonatique complexe en position explosive
                    if syllabes[0][0] + syllabes[0][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        if syllabes[1] == 'MUS':
                            changements.append('i')
                        else:
                            changements.append('ei')
                    #Présence d'un N mouillé
                    elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['GN', 'NC']:
                        changements.append('ei')
                    else:
                        changements.append('i')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'LY':
                    if syllabes[1][1] == 'R':
                        changements.append('ie')
                    else:
                        changements.append('i')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['DW', 'GW', 'WW']:
                    if syllabes[1][1] == 'R':
                        changements.append('u')
                    else:
                        changements.append('eu')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'DY':
                    changements.append('')
                elif syllabes[0][-1] == 'N':
                    if len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'CR':
                        changements.append('ei')
                    elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'GW':
                        changements.append('a')
                    elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['WE', 'WR']:
                        changements.append('i')
                    else:
                        changements.append('e')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] == 'SCR':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[0]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #Au contact direct avec un Ī long final
                if syllabes[1] == syllabes[-1] == 'Ī':
                    changements.append('i')
                #Au contact d'un yod géminé
                elif syllabes[1][0] == 'Y':
                    changements.append('i')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                elif syllabes[1] == 'O':
                    changements.append('je')
                else:
                    changements.append('ie')
            elif syllabes[0][-1] == 'Ę':
                #Au contact direct avec un Ī long final
                if syllabes[1] == syllabes[-1] == 'Ī':
                    changements.append('i')
                #Au contact d'un yod géminé
                elif syllabes[1][0] == 'Y':
                    changements.append('i')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XI', 'ST', 'CT', 'SY', 'XY',]:
                    changements.append('i')
                elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] + syllabes[1][2] == 'TWĪ':
                    changements.append('ui')
                else:
                    changements.append('ie')
            elif syllabes[0][-2] == 'Ę':
                #Au contact d'un yod géminé
                if syllabes[0][-1] == 'Y':
                    changements.append('i')
                #Influence d'un Ī long final
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['DY', 'TY', 'XI', 'ST', 'CT', 'SY', 'XY',]:
                    if syllabes[1][1] == 'A':
                        changements.append('e')
                    else:
                        changements.append('i')
                #Influence fermante d'un wau
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['QW', 'WW']:
                    if syllabes[0][-2] == syllabes[0][0] or syllabes[0][0] == 'S':
                        changements.append('i')
                    else:
                        changements.append('iu')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['LY', 'PD', 'PY']:
                    changements.append('ie')
                elif len(syllabes) > 1 and syllabes[0][-1] == 'P' and syllabes[1][0] == 'D':
                    changements.append('ei')
                #Certaines formes obscures se forment lorsque des occlusives secondaires se transforment en yod (p.36 pour l'exemple DCY)
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] in ['DCY', 'TTY', 'PTY', 'RTY']:
                    changements.append('ie')
                #Le Ę ouvert échappe à l'action d'une nasale
                elif syllabes[0][-1] in ['M']:
                    changements.append('ie')
                elif syllabes[0][-1] == ' ':
                    changements.append('ie')
                else:
                    changements.append('e')
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[0]:
            if len(syllabes[0]) == 1:
                changements.append('i')
            elif syllabes[0][-1] == 'Í':
                changements.append('i')
            elif syllabes[0][-2] == 'Í':
                changements.append('i')
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[0]:
            if len(syllabes[0]) == 1:
                #Sous l'influence d'un Ī long final (métaphonie)
                if syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                #Au contact direct avec un Ī long final (métaphonie)
                elif syllabes[1] == syllabes[-1] == 'Ī':
                    changements.append('ui')
                #Au contact d'un yod géminé
                elif syllabes[1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                #Ouverture face à la séquence CL
                elif len(syllabes) == 2 and syllabes[1][0] + syllabes[1][1] == 'CL':
                    changements.append('ue')
                elif syllabes[1][0] + syllabes[1][1] == 'LY':
                    changements.append('o')
                else:
                    changements.append('ou')
            elif syllabes[0][-1] == 'Ọ':
                #Au contact direct avec un Ī long final (métaphonie)
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] == 'Ī':
                    if syllabes[1][0] + syllabes[1][1] == 'LW':
                        changements.append('oi')
                    else:
                        changements.append('ui')
                #Sous l'influence d'un Ī long final (métaphonie)
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    if syllabes[1][0] + syllabes[1][1] == 'LW':
                        changements.append('oi')
                    else:
                        changements.append('u')
                #Au contact d'un yod géminé
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes) > 1 and len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes) > 1 and len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XI', 'CT', 'ST', 'SY', 'XY', 'PR']:
                    changements.append('ui')
                #Aperture de la bouche en présence d'un groupe consonantiquenasal complexe
                elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] == 'MN':
                    changements.append('a')
                #Influence d'une nasale
                elif len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('o')
                elif len(syllabes[0]) > 1 and syllabes[0][0] + syllabes[0][1] == 'SP':
                    changements.append('o')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['GN', 'LW']:
                    changements.append('oi')
                else:
                    changements.append('ou')
            elif syllabes[0][-2] == 'Ọ':
                #Sous l'influence d'un Ī long final (métaphonie)
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    #Présence d'une double consonne
                    if syllabes[0][-1] == syllabes[1][0] :
                        changements.append('ui')
                    elif syllabes[0][-1] in ['L', 'T']:
                        changements.append('oi')
                    else:
                        changements.append('u')
                #Au contact d'un yod géminé
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[0][-1] == 'B':
                        changements.append('o')
                    elif syllabes[0][-1] in ['L', 'N']:
                        changements.append('oi')
                    else:
                        changements.append('ui')
                #Au contact d'un yod préposé
                elif syllabes[0][-1] == 'Y':
                    if len(syllabes) > 1 and syllabes[1][0] == 'C' or syllabes[0][-1] == syllabes[-1][-1]:
                        changements.append('oi')
                    elif len(syllabes) > 1 and syllabes[1][0] == 'T':
                        changements.append('ui')
                    else:
                        changements.append('u')
                #Au contact d'un yod géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes) > 1 and len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes) > 1 and len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XI', 'CT', 'ST', 'SY', 'XY',]:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['XI', 'CT', 'GT', 'ST', 'SY', 'XY', 'YT']:
                    changements.append('ui')
                #Au contact d'un n mouillé
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['GN', 'NG', 'LT', 'TW', 'LW']:
                    changements.append('oi')
                #Au contact d'autres N mouillés
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] in ['YGN', 'YNG']:
                    changements.append('oi')
                #Ouverture suite à l'influence de nasales
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'MN':
                    changements.append('a')
                #fermetureen fin de mot
                elif syllabes[0][-1] == 'S' == syllabes[-1][-1]:
                    changements.append('eu')
                elif syllabes[0][-1] == 'N':
                    if syllabes[0][0] == syllabes[0][-2]:
                        changements.append('o')
                    elif len(syllabes) > 1 and syllabes[1][0] == 'C':
                        changements.append('oi')
                    else:
                        changements.append('o')
                else:
                    changements.append('o')
            else:
                changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[0]:
            if len(syllabes[0]) == 1:
                #Absence de diphtongaison du à une nasale
                if syllabes[1][0] == 'N':
                    changements.append('o')
                #Influence d'un Ī long final
                elif syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Influence d'un l mouillé
                elif syllabes[1][0] + syllabes[1][1] == 'LY':
                    changements.append('o')
                #Au contact d'un yod géminé
                elif syllabes[1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                #Au contact d'autre éléments dégageant un yo
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] == 'CR':
                    changements.append('u')
                #Influence fermante d'un wau
                elif syllabes[1] == syllabes[-1] and syllabes[1][0] + syllabes[1][1] == 'CA':
                    changements.append('ou')
                else:
                    changements.append('ue')
            elif syllabes[0][-1] == 'Ǫ':
                if syllabes[1] == syllabes[-1] == 'CU':
                    changements.append('ie')
                #Absence de diphtongaison du à une nasale
                elif syllabes[1][0] == 'N':
                    changements.append('o')
                #Arrondissement dû à l'attaque
                elif syllabes[0][0] + syllabes[0][1] == 'SC':
                    changements.append('o')
                elif syllabes[0][0] == syllabes[0][-2] == 'R':
                    changements.append('o')
                #Influence fermante d'un wau
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1] == syllabes[-1] and syllabes[1][0] + syllabes[1][1] == 'CA':
                    changements.append('ou')
                #Au contact d'un yod géminé
                elif syllabes[1][0] == 'Y':
                    changements.append('ui')
                #Au contact d'un géminé provenant de BY, VY, DY, GY, GI et GE
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CW', 'VY', 'DY', 'GY', 'GI', 'GE']:
                    changements.append('ui')
                #Influence d'un Ī long final
                elif syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Au contact d'un élément ou d'un groupe consonantique comportant ou dégageant un yod
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] in ['XA', 'XI', 'CT', 'SY', 'XY', 'ST']:
                    changements.append('ui')
                #Au contact d'autre éléments dégageant un yo
                elif len(syllabes[1]) >= 2 and syllabes[1][0] + syllabes[1][1] == 'CR':
                    changements.append('u')
                elif len(syllabes) > 1 and syllabes[1] == 'GN':
                    changements.append('oi')
                else:
                    changements.append('ue')
            elif syllabes[0][-2] == 'Ǫ':
                #Au contact d'un N mouillé
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CY', 'GN', 'NG']:
                    changements.append('oi')
                #Anticipation du Ī long final
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[-1][-1] == 'Ī':
                    if syllabes[0][-1] + syllabes[1][0] in ['CW', 'QW']:
                        changements.append('ui')
                    else:
                    #Action fermant d'un wau
                    # if syllabes[-1][-2] == syllabes[-1][0] == 'W':
                    #     changements.append('ui')
                        changements.append('oi')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'WN':
                    changements.append('ue')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['FW', 'WL']:
                    changements.append('oe')
                #Au contact d'un yod
                elif syllabes[0][-1] == 'Y':
                    changements.append('ui')
                #Au contact d'un yod
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'WY':
                    changements.append('u')
                #Influence fermante d'un yod ou d'un wau
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CW', 'QW']:
                    changements.append('ieu')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CT', 'DY']:
                    changements.append('u')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'LY':
                    changements.append('uei')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] in ['LLR', 'LGR']:
                    changements.append('ou')
                elif syllabes[0][-1] == 'X':
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] == 'STY':
                    changements.append('ui')
                else:
                    changements.append('o')
            else:
                if syllabes[0][-2] == 'Y':
                    changements.append('ui')
                else:
                    changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[0]:
            if len(syllabes[0]) == 1:
                #Rencontre en hiatus d'un Ī long final
                if syllabes[1] == syllabes[-1] and 'Ī' == syllabes[-1]:
                    changements.append('ui')
                else:
                    changements.append('u')
            elif syllabes[0][-1] == 'Ú':
                #Rencontre en hiatus d'un Ī long final
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] and 'Ī' == syllabes[-1]:
                    changements.append('ui')
                else:
                    changements.append('u')
            elif syllabes[0][-2] == 'Ú':
                if syllabes[0][-1] == 'W' and syllabes[1][0] == 'W':
                    changements.append('iu')
                elif syllabes[0][-1] == 'Y':
                    changements.append('ui')
                else:
                    changements.append('u')
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[0][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[0][-1] == 'B':
                #Pésence d'un wau
                if len(syllabes) > 1 and syllabes[1][0] == 'W':
                    if syllabes[0][-2] in ['Á', 'Ẹ']:
                        changements.append('')
                    else:
                        changements.append('u')
                #Spirantisation de B face à un groupe dégageant un yod
                if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('v')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'TR':
                    changements.append('z')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'TL':
                    changements.append('u')
                #Assimilation à la consonnne suivante
                else:
                    changements.append('')

            #Gestion de C
            elif syllabes[0][-1] == 'C':
                if len(syllabes) > 1 and syllabes[1] == syllabes[-1] == 'MUS':
                    if syllabes[0][-2] == 'A':
                        changements.append('is')
                    else:
                        changements.append('s')
                #dégageemnt de yod
                elif len(syllabes) > 1 and syllabes[1][0] == 'T':
                    if syllabes[1][1] == 'Y' or syllabes[0][-2] in ['Ę', 'Ọ']:
                        changements.append('')
                    elif syllabes[0][-3] == 'Y':
                        changements.append('')
                    else:
                        changements.append('i')
                #Amuïssmeent en î
                elif len(syllabes) > 1 and syllabes[1][0] == 'C':
                    changements.append('')
                elif syllabes[0][-2] in ['A', 'Á', 'Ẹ']:
                    #Cas d'assimilation à un groupe dégageant un yod
                    if len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CR', 'TY']:
                        changements.append('')
                    elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'YA':
                        changements.append('C')
                    #La palatale sourde combinée à un yod subit un redoublement puis une assibilation
                    elif len(syllabes) == 2 and syllabes[1][0] + syllabes[1][1] == 'YO' and syllabes[-1][1] == syllabes[-1][-1]:
                        changements.append('z')
                    else:
                        changements.append('')
                elif syllabes[0][-2] == 'N':
                    changements.append('nc')
                #Assimilation
                else:
                    changements.append('')

            #Gestion de D
            elif syllabes[0][-1] == 'D':
                #La dentale sonore s'assibile et se sonorise
                if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[1][1] == 'Á':
                        changements.append('')
                    else:
                        changements.append('i')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de F
            elif syllabes[0][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[0][-1] == 'G':
                if len(syllabes) > 1 and syllabes[1][0] == 'G':
                    changements.append('')
                #à voir
                elif syllabes[0][-2] in ['E', 'Ẹ']:
                    if syllabes[1][0] == 'W':
                        changements.append('')
                    else:
                        changements.append('i')
                elif syllabes[0][-2] in ['A', 'Á', 'O', 'U']:
                    changements.append('u')
                elif syllabes[0][-2] == 'I':
                    changements.append('')
                else:
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[0][-1] == 'H':
                changements.append('')

            #Gestion de L
            elif syllabes[0][-1] == 'L':
                #Si la première syllabe est un préfixe
                if len(syllabes) > 1 and syllabes[1][0] == ' ':
                    changements.append('l')
                elif len(syllabes) > 1 and syllabes[1][0] == 'C':
                    if syllabes[0][-2] in ['A', 'Ọ']:
                        changements.append('u')
                    else:
                        changements.append('l')
                #Présence d'un yod
                elif len(syllabes) > 1 and syllabes[1][0] == 'L':
                    changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] == 'M':
                    if syllabes[0][-2] == 'A':
                        changements.append('u')
                    else:
                        changements.append('r')
                elif len(syllabes) > 1 and syllabes[1][0] == 'T':
                    if syllabes[0][-2] in ['A', 'Ǫ']:
                        changements.append('u')
                    else:
                        changements.append('l')
                elif len(syllabes) > 1 and syllabes[1][0] == 'W':
                    changements.append('l')
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[0][-2] in ['Ẹ', 'Ọ']:
                        changements.append('l')
                    elif syllabes[1] == syllabes[-1] and syllabes[1][1] == syllabes[1][-1] == 'U':
                        changements.append('l')
                    elif syllabes[0][-2] == 'O':
                        changements.append('ill')
                    elif syllabes[0][-2] == 'Ę':
                        changements.append('u')
                    else:
                        changements.append('ll')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CE', 'GR', 'PÍ', 'QW', 'RE', 'WĪ', 'VU']:
                    if syllabes[0][-2] == 'Ọ':
                        changements.append('u')
                    elif syllabes[0][-2] == 'Ǫ':
                        changements.append('')
                    else:
                        changements.append('l')
                elif syllabes[0][-2] + syllabes[0][-1] == 'LL':
                    changements.append('l')
                #Vocalisation en wau
                else:
                    changements.append('u')

            #Gestion de M
            elif syllabes[0][-1] == 'M':
                if len(syllabes) > 1 and syllabes[1][0] in ['B', 'D', 'Q', 'T']:
                    if syllabes[0][-2] in ['Ọ', 'Ǫ']:
                        changements.append('m')
                    else:
                        changements.append('n')
                elif syllabes[1][0] == 'C':
                    changements.append('n')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'PT':
                    changements.append('n')
                elif len(syllabes) > 1 and syllabes[1][0] == 'M':
                    if syllabes[1][1] == 'Y':
                        changements.append('n')
                    else:
                        changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('n')
                elif syllabes[0][-1] == syllabes[-1][-1]:
                    changements.append('n')
                else:
                    changements.append(syllabes[0][-1])

            #Gestion de N
            elif syllabes[0][-1] == 'N':
                #Mouillure du N
                if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[0][-2] == 'Í':
                        changements.append('ng')
                    else:
                        changements.append('gn')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'DY':
                    changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] == 'N':
                    changements.append('')
                elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] + syllabes[1][2] == 'STR':
                    changements.append('')
                else:
                    changements.append(syllabes[0][-1])

            #Gestion de P
            elif syllabes[0][-1] == 'P':
                if syllabes[1][0] == 'D':
                    changements.append('d')
                #Spirantisation
                elif syllabes[0][-2] == 'O' and syllabes[1][0] == 'M':
                    changements.append('v')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de Q
            elif syllabes[0][-1] == 'Q':
                #Cas rare où la lettre Q est en fin de syllabe, mais qui devrait être en position explosive
                if syllabes[1][0] == 'W':
                    if syllabes[1] == syllabes[-1] and syllabes[1][1] == syllabes[-1][-1] and syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                        changements.append('')
                    elif syllabes[1] == syllabes[-1] and syllabes[1][1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[1][-1] in ['T', 'S']:
                        changements.append('')
                    elif syllabes[1][1] == syllabes[-1][-1] == 'T':
                        changements.append('')
                    else:
                        changements.append('v')
                elif syllabes[1][0] == 'Y':
                    if syllabes[1][1] in ['A', 'Á']:
                        changements.append('c')
                    else:
                        changements.append('z')
                else:
                    changements.append('')

            #Gestion de R
            elif syllabes[0][-1] == 'R':
                #Présence d'un R dans la syllabe suivante
                if len(syllabes) > 1 and syllabes[1][0] == 'R':
                    if (syllabes[0][-2] in ['A', 'Á'] and syllabes[1][1] in ['C', 'U', 'Ú']):
                        changements.append('r')
                    else:
                        changements.append('')
                elif syllabes[0] == 'CR':
                    changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[0][-1])
                    # changements.append('')

            #Gestion de S
            elif syllabes[0][-1] == 'S':
                #Consonantisme implosif complexe
                if syllabes[0][-2] + syllabes[0][-1] == 'RS':
                    changements.append(syllabes[0][-2] + syllabes[0][-1])
                elif syllabes[0][-2] + syllabes[0][-1] == 'NS':
                    changements.append('ns')
                #Présence d'un S en position explosive dans la syllabe suviante
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if len(syllabes[0]) > 2 and len(syllabes[1]) > 2 and syllabes[0][-2] in ['A', 'Á'] and syllabes[1][0] + syllabes[1][1] in ['YÁ', 'YA']:
                        changements.append('s')
                    elif syllabes[0][-2] == 'A' and syllabes[1][1] in ['A', 'Á', 'Ę']:
                        changements.append('s')
                    else:
                        changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[0][-2] == 'A' and syllabes[1][1] == 'Á':
                        changements.append('ss')
                    else:
                        changements.append('')
                #La sifflante avec un yod dégage vers l'avant une semi-voyelle palatale
                # elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    # changements.append('is')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[0][-1] == 'T':
                if syllabes[0][-2] + syllabes[0][-1] in ['LT', 'NT', 'ST']:
                    changements.append(syllabes[0][-2] + syllabes[0][-1])
                # elif syllabes[0][-2] + syllabes[0][-1] == 'NT':
                    # changements.append(syllabes[0][-2] + syllabes[0][-1])
                #Position finale absolue
                elif syllabes[0][-1] == syllabes[-1][-1]:
                    changements.append('t')
                #Spirantisation face à un yod
                elif syllabes[1][0] == 'Y':
                    changements.append('s')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de V
            elif syllabes[0][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[0][-1] == 'W':
                if syllabes[0][-2] in ['A', 'E', 'O']:
                    changements.append('u')
                elif syllabes[0][-2] == 'Í' and syllabes[1][0] == 'R':
                    changements.append('v')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de X
            elif syllabes[0][-1] == 'X':
                #Assimilation à la consonne suivante
                changements.append('s')

            #Gestion de Y
            elif syllabes[0][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[0][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
