from modelos.vingador import Vingador

def pressionar_enter_para_continuar():
    input("\nPressione Enter para voltar ao menu...")

class Interface:
    @staticmethod
    def exibir_menu():
        print('''
██╗░░░██╗██╗███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗
██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
''')
        print("=== Menu ===")
        print("1 - Cadastrar Vingador")
        print("2 - Listar Vingadores")
        print("3 - Convocar Vingador")
        print("4 - Aplicar Tornozeleira")
        print("5 - Aplicar Chip GPS")
        print("6 - Emitir Mandado de Prisão")
        print("7 - Listar Detalhes de Vingador")
        print("8 - Sair")

    @staticmethod
    def solicitar_dados_cadastro():
        nome_heroi = input("Nome do herói: ")
        nome_real = input("Nome real: ")
        categoria = input("Categoria (Humano, Meta-humano, Androide, Deidade, Alienígena): ")
        poderes = input("Poderes (separados por vírgula): ").split(",")
        poder_principal = input("Poder principal: ")
        fraquezas = input("Fraquezas (separados por vírgula): ").split(",")
        nivel_forca = int(input("Nível de força (0 a 10000): "))
        
        return nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca
    
    @staticmethod
    def cadastrar_vingador():
        nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca = Interface.solicitar_dados_cadastro()

        categorias_permitidas = ["Humano", "Meta-humano", "Androide", "Deidade", "Alienígena"]
        if categoria not in categorias_permitidas:
            print("Categoria inválida. O cadastro não pode ser realizado.")
            return

        if any(vingador.nome_heroi == nome_heroi for vingador in Vingador.lista_vingadores):
            print(f"Já existe um Vingador com o nome de herói '{nome_heroi}'. Tente outro nome.")
            return

        vingador = Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
        Vingador.lista_vingadores.append(vingador)

        print(f"\nO Vingador {nome_heroi} foi cadastrado com sucesso!")

        pressionar_enter_para_continuar()

    @staticmethod
    def listar_vingadores():
        if not Vingador.lista_vingadores:
            print("Nenhum vingador registrado.")
        else:
            for vingador in Vingador.lista_vingadores:
                print(f"{vingador.nome_heroi} ({vingador.nome_real}) - Categoria: {vingador.categoria}")
        
        pressionar_enter_para_continuar()  

    @staticmethod
    def listar_detalhes(vingador):
        if vingador:
            detalhes = vingador.listar_detalhes()
            for chave, valor in detalhes.items():
                print(f"{chave}: {valor}")
        else:
            print("Vingador não encontrado para exibição dos detalhes.")
        
        pressionar_enter_para_continuar()  

    @staticmethod
    def buscar_vingador():
        nome = input("Digite o nome do herói ou nome real: ")
        vingador = Vingador.buscar_vingador(nome)
        if vingador:
            return vingador
        else:
            print(f"Vingador com nome '{nome}' não encontrado.")
            return None

    @staticmethod
    def convocar_vingador():
        vingador = Interface.buscar_vingador()
        if vingador:
            vingador._convocado = True
            print(f"{vingador.nome_heroi} foi convocado com sucesso!")
        
        pressionar_enter_para_continuar()  

    @staticmethod
    def aplicar_tornozeleira():
        vingador = Interface.buscar_vingador()
        if vingador and vingador._convocado:
            vingador._tornozeleira_aplicada = True
            if vingador.nome_heroi == "Thor" or vingador.nome_heroi == "Hulk":
                print(f"A tornozeleira foi aplicada em {vingador.nome_heroi}, mas eles resistiram com força!")
            else:
                print(f"A tornozeleira foi aplicada em {vingador.nome_heroi} com sucesso!")
        else:
            print("Não é possível aplicar a tornozeleira. O Vingador não foi convocado.")

        pressionar_enter_para_continuar() 

    @staticmethod
    def aplicar_chip_gps():
        vingador = Interface.buscar_vingador()
        if vingador and vingador._tornozeleira_aplicada:
            vingador._chip_gps_aplicado = True
            print(f"Chip GPS aplicado com sucesso em {vingador.nome_heroi}.")
        else:
            print("Erro: A tornozeleira não foi aplicada. Não é possível adicionar o chip GPS.")
        
        pressionar_enter_para_continuar() 
