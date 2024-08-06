import random

class Kiezer:
    def __init__(self, id, voornaam, achternaam, leeftijd):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
        self.heeft_gestemd = False
        print(f"[Kiezer aangemaakt] {self.voornaam} {self.achternaam}, leeftijd: {self.leeftijd}")

    def stem(self, lijsten, gewichten):
        if not self.heeft_gestemd:
            gekozen_lijst = random.choices(lijsten, gewichten)[0]
            gekozen_kandidaat = random.choice(gekozen_lijst.kandidaten)
            gekozen_lijst.stem_op(gekozen_kandidaat)
            self.heeft_gestemd = True
            print(f"[Kiezer gestemd] {self.voornaam} {self.achternaam} heeft gestemd op {gekozen_kandidaat.voornaam} {gekozen_kandidaat.achternaam}")
        else:
            print(f"[Fout] Kiezer {self.voornaam} {self.achternaam} heeft al gestemd.")