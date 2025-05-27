#pozdrav
def pozdrav():
    print("ahoj")
 
pozdrav()
#dnesni den
def dnesniDen():
    print("dnes je úterý")
 
dnesniDen()
#cisla 1 az 5
def cisla():
    ciselka = [1, 2, 3, 4, 5]
    print(ciselka)
 
cisla()
#obdelnik z hvezd
def hvezdy():
    print("* * * * * * * * *")
    print("*               *")
    print("*               *")
    print("*               *")
    print("* * * * * * * * *")
 
hvezdy()
#nalada dne
def naladaDne():
    print("dnesni denni nalada je slunecno")
 
naladaDne()
#konec
def konec():
    print("tot vse, zase nekdy ahoj")
 
konec()

volba = input()

if volba == "1":
    pozdrav()
elif volba == "2":
    dnesniDen()
elif volba == "3":
    cisla()
elif volba == "4":
    hvezdy()
elif volba == "5":
    naladaDne()
else:
    konec()