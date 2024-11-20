# Bereken van de volgende functies wat hun Grote O complexiteit is.
# Je kunt commentaar gebruiken om de complexiteit er bij te schrijven.

#=============================================
#Opdracht 1
#=============================================
# Dit is een simpel algoritme waarin je het maximale element uit een lijst zoekt.
def vind_max(lijst):
    max_waarde = lijst[0]
    for nummer in lijst:
        if nummer > max_waarde:
            max_waarde = nummer
    return max_waarde


#=============================================
#Opdracht 2
#=============================================
#Dit is een sorteeralgoritme, waarbij elk element wordt vergeleken met zijn buur en wordt gewisseld indien nodig
def bubble_sort(lijst):
    n = len(lijst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lijst[j] > lijst[j+1]:
                lijst[j], lijst[j+1] = lijst[j+1], lijst[j]
    return lijst


#=============================================
#Opdracht 3
#=============================================
#Dit algoritme controleert of een lijst in oplopende volgorde gesorteerd is.
def is_gesorteerd(lijst):
    for i in range(1, len(lijst)):
        if lijst[i] < lijst[i - 1]:
            return False
    return True


#=============================================
#Opdracht 4
#=============================================
#Dit is een recursief algoritme om de fibonacci reeks te berekenen tot een bepaalde graad.
#De uitdaging is hier: Hoe werkt recursie en hoeveel aanroepen worden er gedaan per stap?
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



#=============================================
#Opdracht 5
#=============================================
# Dit algoritme doorzoekt een lijst om twee getallen te vinden die optellen tot een bepaald doel.
# Dit wordt hier opgelost met een brute force-aanpak, maar kan geoptimaliseerd worden door een dict te gebruiken
def vind_paar(lijst, doel):
    for i in range(len(lijst)):
        for j in range(i + 1, len(lijst)):
            if lijst[i] + lijst[j] == doel:
                return (lijst[i], lijst[j])
    return None



#=============================================
#Opdracht 6
#=============================================
# Dit is een traditioneel matrix-vermenigvuldigingsalgoritme.
# Gegeven twee 2D-lijsten, vermenigvuldig de corresponderende rijen en kolommen.
def matrix_vermenigvuldiging(matrix_a, matrix_b):
    nummer_rijen_a = len(matrix_a)
    nummer_kolommen_a = len(matrix_a[0])
    nummer_kolommen_b = len(matrix_b[0])

    resultaat = [[0 for _ in range(nummer_kolommen_b)] for _ in range(nummer_rijen_a)]

    for i in range(nummer_rijen_a):
        for j in range(nummer_kolommen_b):
            for k in range(nummer_kolommen_a):
                resultaat[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return resultaat

