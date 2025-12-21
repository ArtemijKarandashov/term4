from datetime import datetime

class Rates():
    def __init__(self, charcode: str = None, value: float = None, nominal: int = None):
        self.charcode = charcode
        self.value = value
        self.nominal = nominal
        self.added = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))