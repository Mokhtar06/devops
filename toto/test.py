# nombre premier
#
# n = int(input("entrer n :"))
# pre=True
# for i in range(2,n):
#     if(n%i==0):
#         pre=False
# if(pre==True):
#     print("est premier")
# else:
#     print("n'est pas premier")




#       triangle

# n = int(input("n ="))
# for i in range(0, n):
#     for j in range(0, i):
#         print("*", end="")
#     print("")
# n = int(input("n ="))
# for i in range (n):
#     print("*"*i)


#       palindrome

# chain = str(input("chain :"))
# Long = len(chain)
# d = Long//2
# pal=False
# for i in range(0,d):
#     if chain[i]==chain[Long-i-1]:
#         pal=True
# if pal==True:
#     print("Plindromme")
# else:
#     print("non palindrom")
# def est_palyndrom(chaine):
#     n=len(chaine)
#     d=n//2
#     pal=False
#     for i in range(0, d):
#         if chaine[i]==chaine[n - i - 1]:
#             pal=True
#     if pal==True:
#         print("palynderome")
#     else:
#         print("nom palyndrome")
# chaine=input("chaine = ")
# j=est_palyndrom(chaine)
# print(j)

# matrice symetrique

# def symetrique(m):
#     n=len(m)
#     for i in range(n):
#         for j in range(i+1, n):
#             if m[i][j] != m[j][i]:
#                 return False
#     return True
# m=[[1, 2, 3],[2, 4, 5],[3, 5, 6]]
# if symetrique(m):
#     print("hh")
# else:
#     print("jj")







#   Exam pratique

# from openpyxl import load_workbook, Workbook
# from matplotlib import pyplot as plt

# Etudiants = {'Ahmed': 10, 'Sidi': 20}
# Etudiants['Mariem'] = 20

# for key in Etudiants.values():
#     print(f"{key} et ")


# def resultatsFinaux(nom_fichier, regions):
#     wb = load_workbook(nom_fichier)
#     ws = wb.active
#     resultats = {}
#     # ['Nouakchott','Nouadhibou','Rosso']
#     for row in ws.iter_rows(min_row=2, values_only=True):
#         results_Candidats = {}
#         # print(ws.max_column)
#         for i in range(len(regions)):
#             results_Candidats[regions[i]] = row[i + 1]
#         resultats[row[0]] = results_Candidats
#     return resultats
# l = ['Nouakchott', 'Nouadhibou', 'Rosso']
# resultats = resultatsFinaux("Fichier.xlsx", l)
# print(resultats)

#
# def Afficher_resultats(resultats):
#     for candidat, results_Candidats in resultats.items():
#         print(f'****{candidat}*****')
#         for region, nb_votes in results_Candidats.items():
#             print(f'Region : {region} -Voix : {nb_votes}')
# l = ['Nouakchott', 'Nouadhibou', 'Rosso']
# resultats = resultatsFinaux("Fichier.xlsx", l)
# Afficher_resultats(resultats)


# def afficher_graphique(resultats):
#     for candidat, results_Candidats in resultats.items():
#         regions = list(results_Candidats.keys())
#         voix = list(results_Candidats.values())
#         plt.pie(voix, labels = regions,startangle=90, shadow = True, explode = (0, 0, 0.1, 0),radius = 1.2, autopct = '%1.1f%%')
#         plt.xlabel("Region")
#         plt.ylabel("Voix")
#         plt.title(f'{candidat}')
#         plt.show()
# l = ['Nouakchott', 'Nouadhibou', 'Rosso']
# resultats = resultatsFinaux("Fichier.xlsx", l)
# afficher_graphique(resultats)





print("hello world")

