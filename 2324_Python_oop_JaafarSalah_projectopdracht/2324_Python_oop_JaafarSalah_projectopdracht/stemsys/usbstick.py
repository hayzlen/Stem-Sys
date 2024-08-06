class USBStick:
    def __init__(self, code):
        self.code = code
        print(f"[USBStick aangemaakt] met code {self.code}")

    def __str__(self) -> str:
        return f"[USBStick aangemaakt] met code {self.code}"