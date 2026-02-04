"""
Írjon programot vasarlas.py néven, ami billentyűzetről bekéri egy 
termék árát forintban, az euro árfolyamát és egy euro összeget, 
majd kiírja a minta szerint, hogy a beírt euroért meg tudjuk-e 
vásárolni a terméket. 

Minta:
Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 50
A terméket meg tudod vásárolni!

Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 5.15
Nincs elég euród a termék megvásárlására!

"""
termek_ar = int(input("Kérem  termék árát forintban!: "))
eur_arfolyam = float(input("Kérem az euro árfolyamát: "))
eurom_van = float(input("Mennyi euróval rendelkezel?: "))

termek_ara_euroban = termek_ar / eur_arfolyam
#print(termek_ara_euroban)
if termek_ar / eur_arfolyam <= eurom_van:
    print("A terméket meg tudod vásárolni!")
else:
    print("Nincs elég euród a termék megvásárlására!")