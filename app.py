from modelos.interface import Interface
from modelos.vingador import Vingador

def main():
    
    Vingador("Thor", "Thor Odinson", "Deidade", ["Raio", "Força Sobrehumana"], "Raio", ["Fogo", "Magia"], 10000)
    Vingador("Hulk", "Bruce Banner", "Meta-humano", ["Força", "Regeneração"], "Força", ["Radiação Gamma"], 9500)
    Vingador("Capitã Marvel", "Carol Danvers", "Meta-humano", ["Energia", "Voo", "Força"], "Energia", ["Fósforo", "Ácido", "Radiação"], 9900)

    while True:
        Interface.exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca = Interface.solicitar_dados_cadastro()
            try:
                Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
                print(f"{nome_heroi} foi cadastrado com sucesso!")
            except ValueError as e:
                print(e)
        
        elif opcao == "2":
            Interface.listar_vingadores()

        elif opcao == "3":
            vingador = Interface.buscar_vingador()
            if vingador:
                vingador.convocar()
                print(f"{vingador.nome_heroi} foi convocado!")
        
        elif opcao == "4":
            vingador = Interface.buscar_vingador()
            if vingador:
                vingador.aplicar_tornozeleira()

        elif opcao == "5":
            vingador = Interface.buscar_vingador()
            if vingador:
                vingador.aplicar_chip_gps()

        elif opcao == "6":
            vingador = Interface.buscar_vingador()
            if vingador:
                vingador.emitir_mandado()

        elif opcao == "7":
            vingador = Interface.buscar_vingador()
            if vingador:
                Interface.listar_detalhes(vingador)

        elif opcao == "8":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
