# modelos/vingador.py
class Vingador:
    lista_de_vingadores = []

    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = [poder.strip() for poder in poderes]  # Remove espaços extras
        self.poder_principal = poder_principal
        self.fraquezas = [fraqueza.strip() for fraqueza in fraquezas]  # Remove espaços extras
        self.nivel_forca = nivel_forca

        # Adiciona o vingador à lista
        Vingador.lista_de_vingadores.append(self)

    def __str__(self):
        # Representação legível de todos os atributos do vingador
        return (
            f"Nome do herói: {self.nome_heroi}\n"
            f"Nome real: {self.nome_real}\n"
            f"Categoria: {self.categoria.capitalize()}\n"
            f"Poderes: {', '.join(self.poderes)}\n"
            f"Poder Principal: {self.poder_principal}\n"
            f"Fraquezas: {', '.join(self.fraquezas)}\n"
            f"Nível de Força: {self.nivel_forca.capitalize()}\n"
        )
