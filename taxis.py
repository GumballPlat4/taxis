#Alprogramok
def beolvasas():
    lista=[]
    with open("./adatok/taxis_adatok.txt") as fm:
        for sor in fm:
            lista.append(int(sor.strip()))

    return lista

def kiir(bev_ossz, bev_atl, volt_5, hanyadik_5, index_5, db_5, bev_max):
    print(f"a. {bev_ossz} piculája lett összesen.")
    print(f"b. Átlagosan {bev_atl} piculát keres a taxisunk egy fuvarral.")
    if volt_5:
        print(f"c. Volt a taxisnak ma ötpiculás bevételű fuvara.")
    else:
        print(f"c. Nem volt a taxisnak ma ötpiculás bevételű fuvara.")
    print(f"d. A taxis bevételei közül a(z) {hanyadik_5+1}. volt az ötpiculás.")
    if index_5!=-1:
        print(f"e. A taxis először {index_5+1} utassal keresett öt piculát.")
    else:
        print(f"e. A taxis nem keresett ma öt piculát.")
    print(f"f. {db_5} ötpiculás bevétele volt a taxisnak.")
    print(f"g. {bev_max} volt ma a taxis legjobb fuvarja.")

#Főprogram
#input
bevetelek=beolvasas()

#calculator
bevetel_osszege=sum(bevetelek)
bevetel_atlag=bevetel_osszege/len(bevetelek)
volt_5piculas=5 in bevetelek  #eldöntés
hanyadik_az_5piculas=bevetelek.index(5)  #kiválasztás
#keresés
otos_index=-1
if 5 in bevetelek:
    otos_index=bevetelek.index(5)
db_5=bevetelek.count(5)
bevetel_max=max(bevetelek)

#output
kiir(bevetel_osszege, bevetel_atlag, volt_5piculas, hanyadik_az_5piculas, otos_index, db_5, bevetel_max)