
def przyklad1():
    a = []
    for x in range(10):
        a.append(x**2)
    print(a)
    b = []
    for y in range(6):
        b.append(3**y)
    print(b)
    c = []
    for z in a:
        if z % 2 == 1:
            c.append(z)
    print(c)
# przyklad1()


def przyklad2():
# #wersja z python comprehension
    a = [x**2 for x in range(10)]
    b = [3**i for i in range(6)]
    c = [x for x in a if x % 2 == 1]
    print(a)
    print(b)
    print(c)
# przyklad2()


def przyklad3():
    # wersja z pętlą
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista = []
    for i in liczby:
        if i % 2 == 0:
            lista.append(i)
    print("Liczby parzyste uzyskane z wykorzystaniem pętli")
    print(lista)
    print()
    # wersja z python comprehension
    lista2 = [i for i in liczby if i % 2 == 0]
    print(lista2)
    # wersja z zagnieżdżonymi pętlami
    lista = []
    for i in [1, 2, 3]:
        for j in [4, 5, 6]:
            lista.append((i, j))
    print(lista)
    # wersja z python comprehension
    lista2 = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
    print(lista2)

# przyklad3()

def przyklad4():
    # wersja z pętlą
    skroty = {"PZU": "Państwowy zakład ubezpieczeń",
              "ZUS": "Zaklad ubezpieczeń społecznych",
              "PKO": "Państwowa kasa oszczędności"}
    odwrocone = {}
    for key, value in skroty.items():
        odwrocone[value] = key
    print(odwrocone)
    # wersja z python comprehension
    odwrocone2 = {value: key for key, value in skroty.items()}
    print(odwrocone2)

# przyklad4()

#
#
# funkcje
#
#

def row_kwadratowe(a,b,c):
    import math
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("brak pierwiastków")
        return -1
    elif delta == 0:
        print("jedne pierwiastek")
        x = (-b) / (2 * a)
        return x
    else:
        print("dwa pierwiaski")
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
    return x1, x2

# print(row_kwadratowe(6, 1, 3))
# print(row_kwadratowe(1, 2, 1))
# print(row_kwadratowe(1, 4, 1))


# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,47}
# C = {x: x∈B i x jest liczbą podzielną przez 2}
def zadanie1():
    a = [1-x for x in range(1,10)]
    b = [4 ** i for i in range(8)]
    c = [x for x in b if x % 2 == 0]
    print(a)
    print(b)
    print(c)

# zadanie1()


# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj
# nową listę, która będzie zawierała tylko parzyste elementy
def zadanie2():
    import random
    lista1 = []
    for i in range(10):
        n = random.randint(1, 100)
        lista1.append(n)
    print('lista 1', lista1)
    lista2 = [i for i in lista1 if i % 2 == 0]
    print('lista 2', lista2)

# zadanie2()


# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość
# - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
def zadanie3():
    produkty ={
        'jablka':'kilogramy',
        'awokoado':'sztuki',
        'gruszki':'sztuki',
        'woda':'litry'
    }
    print(produkty)
    # produkty2 = {value: key for key, value in produkty.items()}
    produkty2 = [i for i in produkty.values() if i=='sztuki']
    # produkty2 = [i for i in produkty if i.values() == 'sztuki']
    print(produkty2)

# zadanie3()



# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
def zadanie4():
    def trojkat(a,b,c):
        if a*a + b*b == c*c:
        # if pow(a)+pow(b)==pow(c):
            print('trojkat prostokatny')
        else: print('trojkat nie jest prostokatny')
    print(trojkat(3,4,5))

# zadanie4()



# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
def zadanie5():
    def trapez(a,b,h):
        pole = (a+b)*(h/2)
        print(pole)
    trapez(10,10,5)

# zadanie5()


# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
def zadanie6():
    def iloczyn(a = 1, b = 4, ile = 10):
        for i in range(ile):
            print(a)
            a=a*b

    iloczyn(2,4,5)
    iloczyn()
# zadanie6()




# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.


# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz to
# nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.


# Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi a drugi
# niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.


# Zad10.
# Z przedziału od 0 do 100 wygeneruj liczby podzielne przez 4 i zapisz je do pliku.



