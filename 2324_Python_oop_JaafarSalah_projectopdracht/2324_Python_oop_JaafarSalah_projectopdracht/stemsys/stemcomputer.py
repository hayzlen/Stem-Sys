import random
from stembiljet import Stembiljet

class StemComputer:
    def __init__(self, usb_stick):
        self.usb_stick = usb_stick
        print(f"[StemComputer aangemaakt] met USB-stick {self.usb_stick.code}")

    def stem(self, kiezer, lijsten, stembus, gewichten):
        if not kiezer.heeft_gestemd:
            gekozen_lijst = random.choices(lijsten, gewichten)[0]
            gekozen_kandidaat = random.choice(gekozen_lijst.kandidaten)
            stembiljet = Stembiljet(kiezer.voornaam + ' ' + kiezer.achternaam, gekozen_lijst, gekozen_kandidaat)
            stembus.ontvang_stembiljet(stembiljet)
            kiezer.heeft_gestemd = True
            print(f"[Stem uitgebracht] Kiezer: {kiezer.voornaam} {kiezer.achternaam}, Lijst: {gekozen_lijst.naam}, Kandidaat: {gekozen_kandidaat.voornaam} {gekozen_kandidaat.achternaam}")
        else:
            print("[Error] Deze kiezer heeft al gestemd.")
