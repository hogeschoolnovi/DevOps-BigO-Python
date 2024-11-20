# Bereken van de volgende functies wat hun Grote O complexiteit is.
# Je kunt commentaar gebruiken om de complexiteit er bij te schrijven.

#=============================================
#Opdracht 1
#=============================================
# Dit is een simpel algoritme waarin je het maximale element uit een lijst zoekt.
def vind_max(lijst):
    max_waarde = lijst[0]  # O(1)
    for nummer in lijst:    # O(n), waar n de lengte van de lijst is
        if nummer > max_waarde:  # O(1) voor elke vergelijking
            max_waarde = nummer  # O(1) voor elke toewijzing
    return max_waarde  # O(1)

# Uitwerking :

#  -Regel max_waarde = lijst[0] kost O(1), omdat dit een enkele toewijzing is.
#  -De for-loop doorloopt elk element in de lijst, dat betekent O(n) iteraties in totaal, met n de lengte van de lijst.
#  -De vergelijking if nummer > max_waarde en de toewijzing binnen de if-branch hebben elk een constante tijdscomplexiteit van O(1), maar ze worden n keer uitgevoerd omdat ze binnen de lus zitten.
#
# Totaal:
#
# O(1 * 2) + O(n * 1) = O(n)
#
# Big
# O - complexiteit: O(n)

#=============================================
#Opdracht 2
#=============================================
#Dit is een sorteeralgoritme, waarbij elk element wordt vergeleken met zijn buur en wordt gewisseld indien nodig
def bubble_sort(lijst):
    n = len(lijst)  # O(1)
    for i in range(n):  # O(n), het buitenste aantal iteraties is n
        for j in range(0, n-i-1):  # O(n-i-1), het binnenste aantal wordt elke keer kleiner
            if lijst[j] > lijst[j+1]:  # O(1)
                lijst[j], lijst[j+1] = lijst[j+1], lijst[j]  # O(1)
    return lijst  # O(1)

# Uitwerking :
#
# -Het bepalen van n = len(lijst) kost O(1).
# -De buitenste for-lus draait n keer, dat betekent O(n).
# -De binnenste for-lus zal in het eerste geval n-1 keer draaien, dan n-2 , enzovoort, in een patroon dat vergelijkbaar is met de som van de eerste n gehele getallen:
#       -De tijdscomplexiteit hiervan is O(n(n-1)/2) , wat neerkomt op O(n²) , want lagere orde termen en constante factoren worden genegeerd.
#
# Totaal :
#
# Het algoritme bevat geneste lussen, waardoor de complexiteit O(n²) is.
#
# Big O-complexiteit : O(n²)

#=============================================
#Opdracht 3
#=============================================
#Dit algoritme controleert of een lijst in oplopende volgorde gesorteerd is.
def is_gesorteerd(lijst):
    for i in range(1, len(lijst)):  # O(n), doorloopt alle elementen behalve het eerste
        if lijst[i] < lijst[i - 1]:  # O(1), vergelijking
            return False  # Mogelijke vroege exit
    return True  # O(1), alleen aan het einde

# Uitwerking :
#
# - De for-loop doorloopt n-1 elementen van de lijst, waar n de lengte van de lijst is. Dit betekent O(n).
# - De vergelijking if lijst[i] < lijst[i - 1] wordt O(1) keer uitgevoerd tijdens elke iteratie.
#
# Beste geval : Als de lijst al gesorteerd is, moet de for-lus de hele lijst doorlopen. Dit kost O(n).
# Slechtste geval : Als de lijst helemaal niet gesorteerd is (bijvoorbeeld de eerste twee elementen zijn verkeerd gerangschikt), dan wordt het algoritme onmiddellijk afgebroken en kost het slechts O(1) .
#
# Big O-complexiteit :
#
# Best case : O(1) (indien de lijst heel snel ongelijk blijkt) 
# Worst case : O(n) (wanneer de hele lijst doorlopen moet worden)

#=============================================
#Opdracht 4
#=============================================
#Dit is een recursief algoritme om de fibonacci reeks te berekenen tot een bepaalde graad.
#De uitdaging is hier: Hoe werkt recursie en hoeveel aanroepen worden er gedaan per stap?
def fibonacci(n):
    if n <= 1:
        return n  # O(1), basisgevallen
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursieve aanroepen

# Uitwerking :
#
# - De recursieve aanroeping fibonacci(n - 1) + fibonacci(n - 2) roept zichzelf twee keer aan voor elke invoer. Dit betekent dat de grootte van het probleem exponentieel groeit.
# - Elk Fibonacci-getal leidt tot twee aanroepen en elk daarvan leidt op zijn beurt weer tot twee nieuwe aanroepen, enzovoort. Dit leidt tot een exponentiële groei in het aantal aanroepen.
# - Specifiek is het aantal aanroepen gelijk aan ongeveer het n-de Fibonacci-getal, dat groeisnelheid O(2^n) heeft.
#
# Tijdcomplexiteit : O(2^n)
#
# Let op: Dit is een inefficiënte manier om Fibonacci-getallen te berekenen vanwege de overlap in subproblemen. Een voorbeeld van een efficientere oplossing is memoization



#=============================================
#Opdracht 5
#=============================================
# Dit algoritme doorzoekt een lijst om twee getallen te vinden die optellen tot een bepaald doel.
# Dit wordt hier opgelost met een brute force-aanpak, maar kan geoptimaliseerd worden door een dict te gebruiken
def vind_paar(lijst, doel):
    for i in range(len(lijst)):  # O(n)
        for j in range(i + 1, len(lijst)):  # O(n-i), innerlijke lus afhankelijk van i
            if lijst[i] + lijst[j] == doel:  # O(1)
                return (lijst[i], lijst[j])  # O(1)
    return None  # O(1)

# Uitwerking :
#
# De eerste for-loop draait n keer, wat betekent O(n).
# De tweede for-lus is afhankelijk van de waarde van i. Wanneer i 0 is, zal deze lus n-1 keer draaien, wanneer i 1 is, dan n-2 keer, en zo verder.
# In totaal hebben we de vorm van een dubbele som vergelijkbaar met bubble sort, wat leidt tot een algemene tijdcomplexiteit van O(n²).
#
# Big O-complexiteit : O(n²)


#=============================================
#Opdracht 6
#=============================================
# Dit is een traditioneel matrix-vermenigvuldigingsalgoritme.
# Gegeven twee 2D-lijsten, vermenigvuldig de corresponderende rijen en kolommen.
def matrix_vermenigvuldiging(matrix_a, matrix_b):
    nummer_rijen_a = len(matrix_a)  # O(1)
    nummer_kolommen_a = len(matrix_a[0])  # O(1)
    nummer_kolommen_b = len(matrix_b[0])  # O(1)

    resultaat = [[0 for _ in range(nummer_kolommen_b)] for _ in range(nummer_rijen_a)]  # O(n*m)

    for i in range(nummer_rijen_a):  # O(n)
        for j in range(nummer_kolommen_b):  # O(m)
            for k in range(nummer_kolommen_a):  # O(p)
                resultaat[i][j] += matrix_a[i][k] * matrix_b[k][j]  # O(1)

    return resultaat  # O(1)

# Uitwerking :
#
# - We hebben drie geneste lussen:
#       - De buitenste lus doorloopt n rijen van matrix A.
#       - De middelste lus doorloopt m kolommen van matrix B.
#       - De binnenste lus loopt door p kolommen van matrix A (of rijen van matrix B).
# - Daardoor is de tijdcomplexiteit O(n * m * p), waarbij n, m en p de afmetingen van de matrices zijn.
#
# Big O-complexiteit : O(n * m * p)
#
# Dit complexiteit O(n * m * p) kun je niet zomaar versimpelem tot een van de algemene complexiteiten.
# Dit kan alleen onder specifieke omstandigheden:
# - Als n=m=p : In dit geval worden de drie variabelen gelijk aan elkaar, en kunnen we de tijdcomplexiteit herschrijven als O(n³)
# - Als m en p constante waarden zijn dan zijn hun waarde niet afhankelijk van de grootte van de invoer n  (bijvoorbeeld als je werkt met een vaste matrixgrootte). In dat geval kun je O(n * m * p)  vereenvoudigen naar O(n) , omdat we constante factoren negeren in de context van Big O.
# - Als n  veel groter is dan zowel m  als p , en deze laatste twee in grote mate kleiner of bijna constant blijven, dan kan de tijdcomplexiteit effectief worden beschouwd als O(n) .
# - Stel dat m of p exponentieel groeit ten opzichte van n, bijvoorbeeld als m=2n of p=n!. In dergelijke gevallen zou de tijdcomplexiteit overeenkomen met respectievelijk O(2^n)  of O(n!) , aangezien deze factoren veel dominanter zijn en de algemene complexiteit bepalen
