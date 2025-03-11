#načtení od uživatele
nacteniTextu = input("Zadejte: ")
nacteniCisla = int(input("Zadejte: "))
#přetypování
cislo = int(input())
#podmínky(if, elif, else)
if (cislo==10):
    print("číslo je 10")
elif(cislo==15):
    print("číslo je 15")
else:
    print("číslo je divný")
#logické operátory
if(cislo>5 and cislo<10):
    print("číslo je větší než 5, ale menší než 10")
#vypsání
print("text")
print(cislo)
print("text", cislo)
#okomentování všeho + podpis v komentáři na github
#načtení - načítá číslo nebo text od uživatele
#přetypování - mění datové typy např. ze stringu na boolean apod.
#podmínky - vypíše číslo podle toho jestli je v daném rozmezí nebo ne
#logické operátory - jsou to spojovací výrazy jako spojky v češtině, např. and
#vypsání - vypíše text do konzole/terminálu
#podpis - Erik Šnajdr 1.B A2
#github příkazy
#git add * 
#git commit -m "..."
#git push