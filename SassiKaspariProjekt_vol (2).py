import operator as op 


hinded = [2,2,2,2,2,2,2,2,2,2,2,2,5]
hinded = open("C:\\Users\\ARVUTI5\\Desktop\\Niga\\hinded.txt", 'r')
print(hinded)



jätkata = True

while jätkata:
    d = float(input("sisesta hinne: "))

    tn = (op.countOf(hinded,d) * d / sum(hinded)) * 100 

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
    print("Tõenäosuse protsent: ", tn)

    q = input("kas jätkata (j/e) ")
    if q == 'e':
        jätkata = False

    