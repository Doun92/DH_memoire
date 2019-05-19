"""
Ce script unit tous les autres scrits qui s'occupent de tâches plus ponctuelles.
Il parcourt chaque mot, lettre par lettre ou syllabe par syllabe, selon les particularités de chacun.

auteur : Daniel Escoval
license : license UNIL
"""

class EvolutionPhonetique:

    def __init__(self):
        return

    def evolution_phonetique(self):

        from syllabifier import Syllabifier
        syllabifier = Syllabifier()

        from AA1_syllabe_initiale import SyllabeInitiale
        syllabe_initiale = SyllabeInitiale()

        from AA2_syllabe_contrepénultième import SyllabeContrepenultieme
        syllabe_contrepenultieme = SyllabeContrepenultieme()

        from AA3_syllabe_contrefinale import SyllabeContrefinale
        syllabe_contrefinale = SyllabeContrefinale()

        from AA4_syllabe_antépénultième_tonique import SyllabeAntePenultieme
        syllabe_ante_penultieme = SyllabeAntePenultieme()

        from AA5_syllabe_pénultième import SyllabePenultieme
        syllabe_penultieme = SyllabePenultieme()

        from AA6_syllabe_finale import SyllabeFinale
        syllabe_finale = SyllabeFinale()

        syllabes = syllabifier.syllabify(self)
        print(syllabes)

        changements = list()


        #Première syllabe et/ou préfixe
        if len(syllabes) > 0:
            changements.append(syllabe_initiale.syllabe_initiale(self))

        #Syllabe contrepénultième
        if len(syllabes) > 5:
            changements.append(syllabe_contrepenultieme.syllabe_contrepenultieme(self))

        #Syllabe contrefinale
        if len(syllabes) > 4:
            changements.append(syllabe_contrefinale.syllabe_contrefinale(self))

        #Anté-pénultième syllabe
        if len(syllabes) > 3:
            changements.append(syllabe_ante_penultieme.syllabe_ante_penultieme(self))

        #Pénultième syllabe
        if len(syllabes) > 2:
            changements.append(syllabe_penultieme.syllabe_penultieme(self))

        #Dernière syllabe
        if len(syllabes) > 1:
            changements.append(syllabe_finale.syllabe_finale(self))

        flat_list = [item for sublist in changements for item in sublist]
        # print(flat_list)



        output = "".join(flat_list)
        # print(output)
        output = output.lower()

        return output



# def main():
#
#     #Importation de librairies diverses
#     import re
#     import collections
#
#     #Importation du dictionnaire de tous les mots du texte
#     # from dictionary import dict
#     # from Mariale_1_dict import dict
#     from Moine_dict import dict
#     keys = dict.keys()
#     values = dict.values()
#     # print(keys)
#     # print(values)
#
#     every_word = open('AA_every_word.txt', 'w', encoding = 'utf-8')
#     catch = open('AA_catch.txt', 'w+', encoding = 'utf-8')
#     dont_catch = open('AA_dont_catch.txt', 'w+', encoding = 'utf-8')
#
#     # print(len(dict_Marie))
#
#     for key in keys:
#         print_final = EvolutionPhonetique.evolution_phonetique(key)
#
#         every_word.write('\n %s > %s \n \n' % (key, print_final) + '----------------------------------------- \n' )
#         # print(key)
#         # print(dict_Marie[key])
#         # print(print_final)
#
#         if print_final == dict[key] or print_final in dict[key]: #Ce serait ici qu'il faudrait modifier
#             catch.write('\n %s > %s == %s \n \n' % (key, print_final, dict[key]) + '----------------------------------------- \n')
#         else:
#             dont_catch.write(('\n %s > %s != %s \n \n' % (key, print_final, dict[key]) + '----------------------------------------- \n'))
#
# main()

# print(EvolutionPhonetique.evolution_phonetique("A COSTÚDMÁRU")) # acotumé
# print(EvolutionPhonetique.evolution_phonetique("A DỌNC")) # adonc
# print(EvolutionPhonetique.evolution_phonetique("HÁBYO")) # ai
# print(EvolutionPhonetique.evolution_phonetique("HÁBYT")) # ait
# print(EvolutionPhonetique.evolution_phonetique("AMĘT")) # amoit
# print(EvolutionPhonetique.evolution_phonetique("APPĘLLARMUS")) # apelleront
# print(EvolutionPhonetique.evolution_phonetique("A PǪRTAT")) # aporta
# print(EvolutionPhonetique.evolution_phonetique("A RE TENÚTS")) # aretenuz
# print(EvolutionPhonetique.evolution_phonetique("APĘC")) # avec
# print(EvolutionPhonetique.evolution_phonetique("A VÍSU")) # avis
# print(EvolutionPhonetique.evolution_phonetique("ABĘT")) # avoit
# print(EvolutionPhonetique.evolution_phonetique("BENẸDÍTA")) # beneoite
# print(EvolutionPhonetique.evolution_phonetique("BĘNE")) # bien
# print(EvolutionPhonetique.evolution_phonetique("CASCÚNA")) # chascune
# print(EvolutionPhonetique.evolution_phonetique("COMẸNTYAVĪ")) # comencié
# print(EvolutionPhonetique.evolution_phonetique("CǪRE")) # cuer
# print(EvolutionPhonetique.evolution_phonetique("DITTAS")) # dites
# print(EvolutionPhonetique.evolution_phonetique("DỌLCA")) # douce
# print(EvolutionPhonetique.evolution_phonetique("DỌLCAMẸNTE")) # doucement
# print(EvolutionPhonetique.evolution_phonetique("ẸN OÁTS")) # enoez
# print(EvolutionPhonetique.evolution_phonetique("ENTẸNDĘT")) # entendoit
# print(EvolutionPhonetique.evolution_phonetique("ẸN TEGRÍNAMẸNTE")) # enterinement
# print(EvolutionPhonetique.evolution_phonetique("ESVẸGLATS")) # esveillez
# print(EvolutionPhonetique.evolution_phonetique("ỌCLOS")) # euz
# print(EvolutionPhonetique.evolution_phonetique("EPẸSCPOS")) # evesques
# print(EvolutionPhonetique.evolution_phonetique("FÁCRE")) # faire
# print(EvolutionPhonetique.evolution_phonetique("FẸCS")) # foiz
# print(EvolutionPhonetique.evolution_phonetique("FÚRUNT")) # furent
# print(EvolutionPhonetique.evolution_phonetique("GENÍTRÍXA")) # genitrix
# print(EvolutionPhonetique.evolution_phonetique("EXÍT")) # issi
# print(EvolutionPhonetique.evolution_phonetique("LAUDAS")) # loes
# print(EvolutionPhonetique.evolution_phonetique("MATTÍNAS")) # matines
# print(EvolutionPhonetique.evolution_phonetique("MỌNYCOS")) # moines
# print(EvolutionPhonetique.evolution_phonetique("MOSTĘRYU")) # mostier
# print(EvolutionPhonetique.evolution_phonetique("ÁWWUNT")) # ont
# print(EvolutionPhonetique.evolution_phonetique("ÁWWIT")) # ot
# print(EvolutionPhonetique.evolution_phonetique("AUDÍ")) # oï
# print(EvolutionPhonetique.evolution_phonetique("PARLAT")) # parlé
# print(EvolutionPhonetique.evolution_phonetique("PRECÍỌSSA")) # precïose
# print(EvolutionPhonetique.evolution_phonetique("PROPHĘTTA")) # prophete
# print(EvolutionPhonetique.evolution_phonetique("QWÁNTU")) # quant
# print(EvolutionPhonetique.evolution_phonetique("CANTÍQWOS")) # quantiques
# print(EvolutionPhonetique.evolution_phonetique("RE GARDÁ")) # reguardé
# print(EvolutionPhonetique.evolution_phonetique("RESPǪNDÍT")) # respondit
# print(EvolutionPhonetique.evolution_phonetique("REVĘRTÍT")) # revertit
# print(EvolutionPhonetique.evolution_phonetique("SÁCRAS")) # sacrez
# print(EvolutionPhonetique.evolution_phonetique("SÁNCTOS")) # sainz
# print(EvolutionPhonetique.evolution_phonetique("SENĘSSTRA")) # senestre
# print(EvolutionPhonetique.evolution_phonetique("SERVÍS")) # servis
# print(EvolutionPhonetique.evolution_phonetique("SÍDĘT")) # sidoit
# print(EvolutionPhonetique.evolution_phonetique("SĘS")) # soies
# print(EvolutionPhonetique.evolution_phonetique("TORNA")) # torna
# print(EvolutionPhonetique.evolution_phonetique("VẸGYLÁRE")) # veiller
# print(EvolutionPhonetique.evolution_phonetique("VẸGYLĘT")) # veilloit
# print(EvolutionPhonetique.evolution_phonetique("VENĘT")) # venoit
# print(EvolutionPhonetique.evolution_phonetique("VĘNIT")) # vient
print(EvolutionPhonetique.evolution_phonetique("VEDẸRE")) # vooir
