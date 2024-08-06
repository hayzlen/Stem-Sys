import random
import uuid
from kiezer import Kiezer
from kandidaat import Kandidaat
from lijst import Lijst
from stembus import Stembus
from stemcomputer import StemComputer
from usbstick import USBStick
from chipkaart import Chipkaart


#ik heb gezocht om via faker random namen te genereren maar het is me niet gelukt, dus dat was een handige oplossing
random_voornaam = [
    "Olivia", "Emma", "Louise", "Mila", "Lina", "Alice", "Anna", "Mia", "Nora", "Lucie",
    "Sofia", "Julia", "Eva", "Chloe", "Ella", "Sarah", "Lola", "Clara",
    "Elise", "Camille", "Victoria", "Juliette",
    "Noah", "Arthur", "Liam", "Louis", "Lucas", "Adam", "Jules", "Victor", "Finn", "Leon",
    "Alexander", "Maxime", "Gabriel", "Shady", "Oscar", "Thomas", "Sebastian", "Mathis",
    "Hugo", "Elias", "Mohamed", "Nathan", "Tom", "Daan", "Samuel","Hayzlen","Mami","Sadek","Saad","Pego","Ayman"
]

random_achternaam = [
    "Peeters", "Janssens", "Maes", "Jacobs", "Mertens",
    "Willems", "Goossens", "Wouters", "Claes", "Vermeulen",
    "Dupont", "Dubois", "Lambert", "Martens", "Michiels",
    "Vandenberghe", "De Smet", "Dumont", "Desmet", "Declercq",
    "Devos", "Van Damme", "De Wilde", "Verhoeven", "Van den Broeck",
    "De Bruyn", "Segers", "Lemmens", "Van Dyck", "Aerts"
]

class Kiessysteem:
    def __init__(self):
        self.kiezers = self.maak_kiezer(1200)
        self.lijsten = self.maak_lijsten(4)
        self.stembus = Stembus(USBStick("opstartcodes"))
        self.stemcomputers = [StemComputer(USBStick("opstartcodes")) for _ in range(3)]
        self.chipkaarten = [Chipkaart(i) for i in range(60)]  # 60 chipkaarten maken
        print("\033[94m[Kiessysteem opgestart]\033[0m")

    def maak_kiezer(self, aantal):
        kiezers = []
        for _ in range(aantal):
            voornaam = random.choice(random_voornaam)
            achternaam = random.choice(random_achternaam)
            leeftijd = random.randint(18, 90)
            kiezer = Kiezer(voornaam + ' ' + achternaam, voornaam, achternaam, leeftijd)
            if kiezer not in kiezers:
                kiezers.append(kiezer)
        return kiezers

    def maak_lijsten(self, aantal):
        lijsten = []
        for i in range(aantal):
            lijst = Lijst(f"Lijst {chr(65 + i)}")
            kandidaten = []
            for _ in range(10):  # Aantal kandidaten per lijst
                voornaam = random.choice(random_voornaam)
                achternaam = random.choice(random_achternaam)
                leeftijd = random.randint(18, 90)
                kandidaat = Kandidaat(voornaam + ' ' + achternaam, voornaam, achternaam, leeftijd, lijst.naam)
                kandidaten.append(kandidaat)
            lijst.kandidaten = kandidaten
            lijsten.append(lijst)
        return lijsten

    def stemproces(self):
        print("[Stemproces gestart]")
        gewichten = [random.random() for _ in self.lijsten]
        totaal = sum(gewichten)
        gewichten = [gewicht / totaal for gewicht in gewichten]

        for kiezer in self.kiezers:
            beschikbare_computers = [sc for sc in self.stemcomputers if not kiezer.heeft_gestemd]
            if beschikbare_computers:
                stemcomputer = random.choice(beschikbare_computers)
                stemcomputer.stem(kiezer, self.lijsten, self.stembus, gewichten)

        resultaten_lijsten, resultaten_kandidaten = self.stembus.tel_stemmen()
        self.genereer_html_output(resultaten_lijsten, resultaten_kandidaten)
        print("\033[94m[Stemproces voltooid]\033[0m")

    def genereer_html_output(self, resultaten_lijsten, resultaten_kandidaten):
        sorted_resultaten_lijsten = {lijst: stemmen for lijst, stemmen in sorted(resultaten_lijsten.items(), key=lambda item: item[1], reverse=True)}

        print("\nStemmen per Partij:")
        print("Partij          Aantal stemmen       Zetels")
        for lijst, stemmen in sorted_resultaten_lijsten.items():
            zetels = stemmen // 50
            print(f"{lijst:<15}{stemmen:<20}{zetels:<5}")

        sorted_resultaten_kandidaten = sorted(resultaten_kandidaten.items(), key=lambda x: x[1], reverse=True)
        print("\nStemmen per Kandidaat:")
        print("Kandidaat                      Aantal stemmen")
        for kandidaat_id, stemmen in sorted_resultaten_kandidaten:
            for lijst in self.lijsten:
                kandidaat = next((k for k in lijst.kandidaten if k.id == kandidaat_id), None)
                if kandidaat:
                    print(f"{kandidaat.voornaam} {kandidaat.achternaam} ({lijst.naam}) {' ' * (30 - len(kandidaat.voornaam) - len(kandidaat.achternaam) - len(lijst.naam))}{stemmen}")

        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Uitslag Stemmen</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 20px;
                    background-color: #f8f9fa;
                    color: #343a40;
                }
                h1 {
                    text-align: center;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    margin-bottom: 20px; 
                    color: #007bff;
                }
                table {
                    border-collapse: collapse;
                    width: 100%;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    background-color: #ffffff;
                    margin-bottom: 20px;
                    border: 1px solid #d3d3d3;
                    border-spacing: 2;
                }
                th, td {
                    border: 1px solid #d3d3d3;
                    text-align: left;
                    padding: 12px;
                }
                th {
                    background-color: #007bff;
                    color: #ffffff;
                    font-weight: bold;
                    text-transform: uppercase;
                }
                tr:nth-child(even) {
                    background-color: #f2f2f2;
                }
                tr:hover {
                    background-color: #e9ecef;
                }
            </style>
        </head>
        <body>
            <h1>Uitslag Stemmen</h1>
            <h2>Stemmen per Lijst</h2>
            <table>
                <tr>
                    <th>Lijst</th>
                    <th>Aantal stemmen</th>
                    <th>Zetels</th>
                </tr>
        """

        zetels_per_lijst = {lijst: stemmen // 50 for lijst, stemmen in sorted_resultaten_lijsten.items()}

        for lijst, stemmen in sorted_resultaten_lijsten.items():
            html_content += f"""
                <tr>
                    <td>{lijst}</td>
                    <td>{stemmen}</td>
                    <td>{zetels_per_lijst[lijst]}</td>
                </tr>
            """

        html_content += """
            </table>
            <h2>Stemmen per Kandidaat</h2>
            <table>
                <tr>
                    <th>Kandidaat</th>
                    <th>Aantal stemmen</th>
                </tr>
        """

        sorted_resultaten_kandidaten = sorted(resultaten_kandidaten.items(), key=lambda x: x[1], reverse=True)
        for kandidaat_id, stemmen in sorted_resultaten_kandidaten:
            for lijst in self.lijsten:
                kandidaat = next((k for k in lijst.kandidaten if k.id == kandidaat_id), None)
                if kandidaat:
                    html_content += f"""
                        <tr>
                            <td>{kandidaat.voornaam} {kandidaat.achternaam} ({kandidaat.lijst})</td>
                            <td>{stemmen}</td>
                        </tr>
                    """

        html_content += """
            </table>
        </body>
        </html>
        """

        with open("Resultaten.html", "w") as file:
            file.write(html_content)
        print("\033[92m[HTML-output gegenereerd]\033[0m ----> naar Resultaten.html")