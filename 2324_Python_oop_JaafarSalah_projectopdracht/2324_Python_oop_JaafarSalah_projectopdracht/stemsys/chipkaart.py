class Chipkaart:
    def __init__(self, id):
        self.id = id
        self.initialized = False
        self.kiezer_id = None
        print(f"[Chipkaart aangemaakt] ID: {self.id}")

    def initialize(self, kiezer_id):
        self.initialized = True
        self.kiezer_id = kiezer_id
        print(f"[Chipkaart geinitialiseerd] ID: {self.id} voor kiezer {self.kiezer_id}")

    def reset(self):
        self.initialized = False
        self.kiezer_id = None
        print(f"[Chipkaart gereset] ID: {self.id}")

    def __str__(self) -> str:
        if self.initialized:
            return f"[Chipkaart geinitialiseerd] {self.id} voor kiezer {self.kiezer_id}"
        else:
            return f"[Chipkaart gereset] {self.id}"