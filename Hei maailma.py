# Ohjelmisto, joka kysyy suorakaiteen
# kannan ja korkeuden, ja laskee
# niiden perusteella pinta-alan

kanta = float(input("Anna kanta: "))
korkeus = float(input("Anna korkeus: "))
# lasketaan ala
ala = kanta * korkeus

# Tulostetaan vastaus
print(f"Suorakaiteen pinta-ala {ala:.2f}")