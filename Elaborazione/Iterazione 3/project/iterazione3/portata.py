class Portata:
    portate = [
        {'id': 1, 'nome': 'Pizza Margherita', 'prezzo': 6.0},
        {'id': 2, 'nome': 'Bistecca alla fiorentina', 'prezzo': 20.0},
        {'id': 3, 'nome': 'Lasagna', 'prezzo': 8.0},
        {'id': 4, 'nome': 'Insalata mista', 'prezzo': 4.0},
    ]

    def __init__(self, id, nome, prezzo):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.nome} ({self.prezzo} euro)"

    @classmethod
    def getPortataByName(cls, nome):
        for portata in cls.portate:
            if portata['nome'] == nome:
                return cls(portata['id'], portata['nome'], portata['prezzo'])
        return None