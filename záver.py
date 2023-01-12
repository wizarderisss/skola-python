zoznam=[ #Doplňte ďalšími aspoň 5 skladbami (dlzka<10min) /1b
    ["Lana Del Rey","Lolita","3:40"],
    ["Lana Del Rey","Blue Jeans","3:29"],
    ["Cascada","Everytime We Touch","3:17"],
    ["Cascada","Runaway","3:30"],
    ["Linkin Park","From the Inside","2:54"],
    ["Linkin Park","Runaway","3:04"],
    ["Oasis","Wonderwall","4:19"],
    ["Alkaline Trio","Krystalline","3:30"],
    ["Avril Lavigne","Runaway","3:49"],
    ["Avril Lavigne","Bite Me","2:40"]
]

#Pokiaľ možno, píšte len tam kde sú ... a odkomentovávajte si volania a printy. Nemeňte inú štruktúru.
#Ak sa bojíte o nerozhodnú známku, dolu je bonusové zadanie. 

#Funkcia, ktorá vráti zoznam s upravenými dĺžkami v sekundách v celočíselnom tvare. /2b
#Napr. -> [...,["Avril Lavigne","Runaway",229],["Avril Lavigne","Bite Me",160],...]
#Ďalej s takto upraveným zoznamom budeme stále pracovať. Všimnite si, že ho využívam pri volaní každej ďalšej funkcie.
#Ak si neviete rady s ňou, vytvorte si z1 ručne a pokračujte. Lepšie stratiť bodík či dva za túto funkciu, než nemať žiadne.
def dlzky(pole):
    ...

#z1=dlzky(zoznam)
#print(z1)



#Funkcia, ktorá vráti zoznam skladieb dlhších než zadaný čas v minútach. /1b
def dlhsie(pole,cas_v_min):
    ...

#z2=dlhsie(z1,4)
#print(z2)



#Funkcia, ktorá vráti zoznam skladieb kratších než zadaný čas v minútach. /1b
def kratsie(pole,cas_v_min):
    ...

#z3=kratsie(z1,3)
#print(z3)



#Funkcia, ktorá vráti zoznam skladieb, ktorých autor obsahuje písmeno m. /1.5b
#Pozor na skutočnosť, že ak je m na začiatku, je veľké.
#Rozoznávajte obsahovať znak a presne sa rovnať názvu, to sú dve odlišné veci.
def meno_bez_m(pole):
    ...

#z4=meno_bez_m(z1)
#print(z4)



#Funkcia, ktorá vráti zoznam skladieb so zadaným názvom. /1b
def vsetky_s_menom(pole,meno:
    ...

#z5=vsetky_s_menom(z1,"Runaway")
#print(z5)



#Funkcia, ktorá vráti zoznam skladieb, ktorých autor sa začína na dané písmeno. /1b
def autor_na(pole,autor):
    ...

#z6=autor_na(z1,"L")
#print(z6)



#Funkcia, ktorá vráti celkovú dĺžku v sekundách. /1.5b
def dlzka(pole):
    ...

#d=dlzka(z1)
#print(d)


#BONUS 1
#Naprogramujte funkciu vypis(pole), ktorou nahradíte funkciu print() a bude uhľadená na výpis tabuľky skladieb.

#BONUS 2
#Naprogramujte funkciu zorad(pole), ktorá vráti vzostupne zoradený zoznam skladieb podľa dĺžky.
