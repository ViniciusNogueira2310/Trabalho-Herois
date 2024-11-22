class Vingador:

    lista_vingadores = []

    categorias_permitidas = ["Humano", "Meta-humano", "Androide", "Deidade", "Alienígena"]

    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        
        if categoria not in Vingador.categorias_permitidas:
            raise ValueError(f"Categoria inválida. As categorias permitidas são: {', '.join(Vingador.categorias_permitidas)}.")
        
        if not (0 <= nivel_forca <= 10000):
            raise ValueError("Nível de força deve ser entre 0 e 10000.")
        
        
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self._convocado = False
        self._tornozeleira_aplicada = False
        self._chip_gps_aplicado = False

        
        Vingador.lista_vingadores.append(self)

    def convocar(self):
        self._convocado = True

    def aplicar_tornozeleira(self):
        if self._convocado:
            self._tornozeleira_aplicada = True
            if self.nome_heroi == "Thor" or self.nome_heroi == "Hulk":
                print(f"{self.nome_heroi} resiste à tornozeleira, mas a aplicação foi bem-sucedida!")
            else:
                print(f"Tornozeleira aplicada em {self.nome_heroi}.")
        else:
            print(f"{self.nome_heroi} não foi convocado. Não é possível aplicar a tornozeleira.")

    def aplicar_chip_gps(self):
        if self._tornozeleira_aplicada:
            self._chip_gps_aplicado = True
            print(f"Chip GPS aplicado em {self.nome_heroi}.")
        else:
            print(f"Não é possível aplicar o chip GPS sem a tornozeleira em {self.nome_heroi}.")

    def emitir_mandado(self):
        print(f"Mandado de prisão emitido para {self.nome_heroi}.")

    def listar_detalhes(self):
        return {
            "Nome do Herói": self.nome_heroi,
            "Nome Real": self.nome_real,
            "Categoria": self.categoria,
            "Poderes": self.poderes,
            "Poder Principal": self.poder_principal,
            "Fraquezas": self.fraquezas,
            "Nível de Força": self.nivel_forca,
            "Status de Convocação": "Convocado" if self._convocado else "Não Convocado",
            "Status da Tornozeleira": "Aplicada" if self._tornozeleira_aplicada else "Não Aplicada",
            "Status do Chip GPS": "Aplicado" if self._chip_gps_aplicado else "Não Aplicado"
        }

    @classmethod
    def buscar_vingador(cls, nome):
        for vingador in cls.lista_vingadores:
            if nome.lower() in (vingador.nome_heroi.lower(), vingador.nome_real.lower()):
                return vingador
        return None
