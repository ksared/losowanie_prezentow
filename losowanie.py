from random import *
osoby = []
print("Losowanie Bożonarodzeniowe!")
print("Ile osób chcesz wylosować?")
liczba_osob = int(input())
for i in range(liczba_osob):
    print("Proszę wpisać imię osoby nr " + str(i+1))
    osoba = input()
    osoby.append(osoba)

pomocnicza_tabela = [-2]

for x in osoby:
    czy_wylosowano = True
    losowa_liczba = -1
    while(losowa_liczba==osoby.index(x) or czy_wylosowano == True):
        losowa_liczba = randint(0, liczba_osob-1)
        for i in pomocnicza_tabela:
            if(i==losowa_liczba):
                czy_wylosowano = True
                break
            else:
                czy_wylosowano = False
    print("osoba " + x + " Wylosowała " + osoby[losowa_liczba])
    pomocnicza_tabela.append(losowa_liczba)
