
class Stembiljet:
    def __init__(self, kiezer_id, gekozen_lijst, gekozen_kandidaat):
        self.kiezer_id = kiezer_id
        self.gekozen_lijst = gekozen_lijst
        self.gekozen_kandidaat = gekozen_kandidaat
        print(f"\033[96m[Stembiljet aangemaakt]\033[0m Kiezer: {self.kiezer_id}, Lijst: {self.gekozen_lijst.naam}, Kandidaat: {self.gekozen_kandidaat.voornaam} {self.gekozen_kandidaat.achternaam}")

