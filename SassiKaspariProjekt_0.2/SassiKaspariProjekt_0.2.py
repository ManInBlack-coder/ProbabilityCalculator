
hinded = open("./hinded.txt", 'r')
hinded = [int(i.strip("\n")) for i in hinded]


jätkata = True

while jätkata:
    kokku=0
    for i in hinded: #Arvutab mitu hinnet on kokku failis
        kokku += 1
    d = int(input("sisesta hinne: "))
    tn=(sum(hinded)/kokku) #Arvutab keskmise hinde
    a = (round(tn, 0)) #Keskmise hinde ümardab lähimaks täisarvuks
    if d+0.5>=a and d-0.5<=a: #Kui soovitud hinne on 0.5 raadiuses keskmisest hindest(Kui soovitud hinne on 0.5 raadiuses keskmisest hindest on suur tõenäosus)
        print("Sul on suur võimalus saada hindeks "+str(d))
    else:
        print("Sul on väike võimalus saada hindeks "+str(d))

    w = input("Kas soovite teada saada aritimeetilist keskmist? (j/e)")
    if w == "j":
        print("Sinu keskmine hinne on "+str(tn))
 
    q = input("kas soovite programmi uuesti alustada? (j/e) ")
    if q == 'e':
        print("Programm on töö lõpetanud.")
        jätkata = False


    

