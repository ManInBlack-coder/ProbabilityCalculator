
hinded = open("./hinded.txt", 'r')
hinded = [int(i.strip("\n")) for i in hinded]


jätkata = True

while jätkata:
    d = int(input("sisesta hinne: "))
    
    tn = (hinded.count(d) * d / sum(hinded)) * 100 

    if d == 5:
        if tn > 50:
            print("sul on võimalus saada kokkuvõtvaks hindeks 5 ")
        if d == 5:
            if tn < 50:
                print("sul on väike võimalus saada kokkuvõtvaks hindeks 5")

    if d == 4:
        if tn > 50:
            print("sul on võimalus saada kokkuvõtvaks hindeks 4")
        if d == 4:
            if tn < 50:
                print("sul on väike võimalus saada kokkuvõtvaks hindeks 4")

    if d == 3:
        if tn > 50:
            print("sul on võimalus saada kokkuvõtvaks hindeks 3")
        if d == 3:
            if tn < 50:
                print("sul on väike võimalus saada kokkuvõtvaks hindeks 3")

    if d == 2:
        if tn > 50:
            print("sul on tõenäosus läbi kukkuda. ")
        if d == 2:
            if tn < 50:
                print("sul on väike võimalus saada kokkuvõtvaks hindeks 2.")

    if d == 1:
        if tn > 50:
            print("Läbi kukkunud.")
        if d == 1:
            if tn < 50:
                print("sul on väike võimalus saada kokkuvõtvaks hindeks 1.")
    print("Tõenäosuse protsent: ", round(tn, 2), "%")

    w = input("Kas soovite teada saada aritimeetilist keskmist? (j/e)")
    if w == "j":
        if hinded.count(d) == 0:
            print("Arv puudub hinnetelehelt")
        else:
            ak = sum(hinded) / len(hinded)
            print(round(ak, 2))
 
    q = input("kas soovite programmi uuesti alustada? (j/e) ")
    if q == 'e':
        print("Programm on töö lõpetanud.")
        jätkata = False

    