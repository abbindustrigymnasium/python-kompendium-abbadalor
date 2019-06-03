import random
import time
from Frågor import totfrågor
from Värden import frågevärden2

# Här anges det totala antalet rundor som ska spelas
print("How many rounds do you want to play?: (1 or 2 rounds)")
totrundor = int(input())
#Ändrar grammatiken beroende på om man valt 1 runda eller inte
if totrundor == 1:
    print("You have chosen to play: " + str(totrundor) + " round!")
else:
    print("You have chosen to play: " + str(totrundor) + " rounds!")
time.sleep(1)

rounds = 0
roundcont = 0
kategori2 = 0


#Kollar om alla rundor har spelats ännu
while rounds < totrundor:
    #Om det inte är den första runda så slumpar den fram 6 siffror
    #Om någon av siffrorna är samma som siffrorna från första rundan slumpas siffrorna igen
    if rounds > 0:
        while roundcont == 0:
            kategori = (random.sample(range(1, 13), 6))
            if not set(kategori).isdisjoint(kategori2):
                roundcont = 0
            else: 
                roundcont = 1
    #Om det är den första rundan så slumpar jag fram 6 siffror mellan 1 och 12 med random
    else:
        kategori = (random.sample(range(1, 12), 6))
        kategori2 = kategori

    #Här väljs kategorierna från de sex siffrorna som valdes innan
    #Sedan tas frågorna i dom kategorierna från "Frågor.py"
    #och sparas i variabler för vilken kategori och poängvärde frågan har
    for fråga in totfrågor[str(kategori[0])]:
        titelA = fråga["titel"]
        if fråga["poäng"] == 200:
            A200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            A400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            A600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            A800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            A1000 = fråga["fråga"]
    for fråga in totfrågor[str(kategori[1])]:
        titelB = fråga["titel"]
        if fråga["poäng"] == 200:
            B200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            B400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            B600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            B800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            B1000 = fråga["fråga"]
    for fråga in totfrågor[str(kategori[2])]:
        titelC = fråga["titel"]
        if fråga["poäng"] == 200:
            C200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            C400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            C600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            C800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            C1000 = fråga["fråga"]
    for fråga in totfrågor[str(kategori[3])]:
        titelD = fråga["titel"]
        if fråga["poäng"] == 200:
            D200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            D400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            D600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            D800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            D1000 = fråga["fråga"]
    for fråga in totfrågor[str(kategori[4])]:
        titelE = fråga["titel"]
        if fråga["poäng"] == 200:
            E200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            E400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            E600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            E800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            E1000 = fråga["fråga"]
    for fråga in totfrågor[str(kategori[5])]:
        titelF = fråga["titel"]
        if fråga["poäng"] == 200:
            F200 = fråga["fråga"]
        elif fråga["poäng"] == 400:
            F400 = fråga["fråga"]
        elif fråga["poäng"] == 600:
            F600 = fråga["fråga"]
        elif fråga["poäng"] == 800:
            F800 = fråga["fråga"]
        elif fråga["poäng"] == 1000:
            F1000 = fråga["fråga"]

    poäng = 0
    antalfrågor = 0
    cont = 0
    #Här definerar jag vilka alternativ som är giltiga för kategori och fråga
    katalt = ["A", "B", "C", "D", "E", "F"]
    frågaalt = ["200", "400", "600", "800", "1000"]
    
    frågevärden = frågevärden2.copy()
    #Här kollas om alla frågor har svarats i denna runda
    while antalfrågor < 30:
        #Den här while-loopen körs så länge som spelaren inte har valt en ny fråga
        while cont == 0:
            katcont = 0
            frågacont = 0
            #Nedanför hämtar jag värden från "Värden.py" för att visa
            #Det är för att jag ska kunna byta ut värdena mot "X" när spelaren har svarat på frågan
            print("                 A                 " + "                 B                 " + "                 C                 " +
                "                 D                 " + "                 E                 " + "                 F                 ")
            print("| " + titelA + " | " + titelB + " | " + titelC +
                " | " + titelD + " | " + titelE + " | " + titelF + " |")
            print("                " + frågevärden["VA200"] + "               " + "                " + frågevärden["VB200"] + "               " + "                " + frågevärden["VC200"] + "               " +
                "                " + frågevärden["VD200"] + "               " + "                " + frågevärden["VE200"] + "               " + "                " + frågevärden["VF200"] + "               ")
            print("                " + frågevärden["VA400"] + "               " + "                " + frågevärden["VB400"] + "               " + "                " + frågevärden["VC400"] + "               " +
                "                " + frågevärden["VD400"] + "               " + "                " + frågevärden["VE400"] + "               " + "                " + frågevärden["VF400"] + "               ")
            print("                " + frågevärden["VA600"] + "               " + "                " + frågevärden["VB600"] + "               " + "                " + frågevärden["VC600"] + "               " +
                "                " + frågevärden["VD600"] + "               " + "                " + frågevärden["VE600"] + "               " + "                " + frågevärden["VF600"] + "               ")
            print("                " + frågevärden["VA800"] + "               " + "                " + frågevärden["VB800"] + "               " + "                " + frågevärden["VC800"] + "               " +
                "                " + frågevärden["VD800"] + "               " + "                " + frågevärden["VE800"] + "               " + "                " + frågevärden["VF800"] + "               ")
            print("                " + frågevärden["VA1000"] + "               " + "                " + frågevärden["VB1000"] + "               " + "                " + frågevärden["VC1000"] + "               " +
                "                " + frågevärden["VD1000"] + "               " + "                " + frågevärden["VE1000"] + "               " + "                " + frågevärden["VF1000"] + "               ")
            time.sleep(1)
            
            #Här väljer spelaren kategori A, B, C, D, E eller F
            while katcont == 0:
                print("Choose a category: (either A, B, C, D, E or F)")
                valdkat = str.upper(input())
                #Här kollar jag om kategorin finns
                if valdkat in katalt:
                    katcont = 1
                else: 
                    print("I didn't quite understand, please choose category A, B, C, D, E or F")
                    katcont = 0
                    time.sleep(1)
            
            #Här väljer spelaren fråga 200, 400, 600, 800 eller 1000
            while frågacont == 0:
                print("Choose a question: (either 200, 400, 600, 800 or 1000)")
                valdfråga = input()
                #Här kollar jag om frågan finns
                if valdfråga in frågaalt:
                    frågacont = 1
                else:
                    print("I didn't quite understand, please choose the point value your question has: 200, 400, 600, 800 or 1000")
                    frågacont = 0
                    time.sleep(1)

            #Här kollar jag om frågan har svarats på redan
            if frågevärden["V" + valdkat + valdfråga] == " X  ":
                print("This question has already been answered, please choose another")
                cont = 0
                time.sleep(1)
            else:
                cont = 1
                time.sleep(1)

        #Här skrivs frågan och kategorin ut
        print(eval("titel" + valdkat))
        print(eval(valdkat + valdfråga))
        time.sleep(1)

        #Här skriver spelaren in sitt svar
        print("Write your answer:")
        valdsvar = str.lower(input())
        valdsvar = valdsvar.strip()

        #Här ändrar jag värdet på en fråga till "X" för att programmet ska kunna se om frågan har blivit svarad på tidigare
        frågevärden["V" + valdkat + valdfråga] = " X  "

        if valdkat == "A":
            valdkat = "0"
        elif valdkat == "B":
            valdkat = "1"
        elif valdkat == "C":
            valdkat = "2"
        elif valdkat == "D":
            valdkat = "3"
        elif valdkat == "E":
            valdkat = "4"
        elif valdkat == "F":
            valdkat = "5"

        #Här letar jag upp rätt fråga i "Frågor.py"
        for fråga in totfrågor[str(kategori[eval(valdkat)])]:
            if fråga["poäng"] == int(valdfråga):
                #Om svaret på frågan är samma som svaret spelaren gav så får hen poängvärdet på frågan
                if valdsvar in fråga["svar"]:
                    poäng = poäng + int(valdfråga)
                    print("Correct!" + "\nYou have won " + valdfråga + " Points!")
                #Om svaren är olika så förlorar spelaren lika mycket poäng
                else:
                    poäng = poäng - int(valdfråga)
                    print("Wrong, The right answer is: " +
                        fråga["svar"][0] + "\nYou have lost " + valdfråga + " Points D:")
                time.sleep(1)
        cont = 0
        #Här räknar jag hur många frågor som har besvarats denna runda
        antalfrågor = antalfrågor + 1
    #Här räknas totala antalet rundor som har spelats
    rounds = rounds + 1
    print("You have answered all questions in this round")
    time.sleep(1)
    #Här ändrar jag grammatiken på medelandet beroende på hur många rundor det är kvar
    if (totrundor - rounds) == 1:
        print("There are " + str((totrundor - rounds)) + " round left")
    else:
        print("There are " + str((totrundor - rounds)) + " rounds left")
    time.sleep(1)
    print("You currently have " + str(poäng) + " points!")
    time.sleep(1)

print("You have completed the game!" + "\nYou got " + str(poäng) + " points")
