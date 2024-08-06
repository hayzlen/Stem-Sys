class Lijst:
    def __init__(self, naam):
        self.naam = naam
        self.kandidaten = []
        self.stemmen = 0
        print(f"[Lijst aangemaakt] {self.naam}")

    def voeg_kandidaat_toe(self, kandidaat):
        if kandidaat not in self.kandidaten:
            self.kandidaten.append(kandidaat)
            print(f"[Kandidaat toegevoegd] {kandidaat.voornaam} {kandidaat.achternaam} aan {self.naam}")
            return True
        else:
            print(f"[Fout] Kandidaat {kandidaat.voornaam} {kandidaat.achternaam} bestaat al in {self.naam}")
            return False

    def stem_op(self, kandidaat):
        kandidaat.stemmen += 1
        self.stemmen += 1
        print(f"[Stem uitgebracht] op {kandidaat.voornaam} {kandidaat.achternaam} van {self.naam}")