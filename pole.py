auticko = ["Nissan", "BMW", "Dodge"]

dalsiAuticko = input("Zadejte dalsi znacku auta")
auticko.append(dalsiAuticko)

auticko.sort()

auticko.reverse()

for polozka in auticko:
    print(polozka)

print(len(auticko))

