class Kandidaat:
    def __init__(self, id, voornaam, achternaam, leeftijd, lijst):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
        self.lijst = lijst
        self.stemmen = 0
        print(f"[Kandidaat aangemaakt] {self.voornaam} {self.achternaam} van {self.lijst}")