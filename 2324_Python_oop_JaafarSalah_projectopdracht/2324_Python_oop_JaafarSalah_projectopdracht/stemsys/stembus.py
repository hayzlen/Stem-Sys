class Stembus:
    def __init__(self, usb_stick):
        self.usb_stick = usb_stick
        self.stembiljetten = []
        print(f"[Stembus aangemaakt] met USB-stick {self.usb_stick.code}")

    def ontvang_stembiljet(self, stembiljet):
        self.stembiljetten.append(stembiljet)
        print(f"[Stembiljet ontvangen] van kiezer {stembiljet.kiezer_id}")

    def tel_stemmen(self):
        print("\033[91m[Stemmen tellen begonnen]\033[0m")
        stemmen_per_lijst = {}
        stemmen_per_kandidaat = {}
        

        for stembiljet in self.stembiljetten:
            lijst_naam = stembiljet.gekozen_lijst.naam
            kandidaat_id = stembiljet.gekozen_kandidaat.id

            if lijst_naam not in stemmen_per_lijst:
                stemmen_per_lijst[lijst_naam] = 0
            stemmen_per_lijst[lijst_naam] += 1

            if kandidaat_id not in stemmen_per_kandidaat:
                stemmen_per_kandidaat[kandidaat_id] = 0
            stemmen_per_kandidaat[kandidaat_id] += 1

        print("\033[91m[Stemmen tellen voltooid]\033[0m")
        return stemmen_per_lijst, stemmen_per_kandidaat

