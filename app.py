import json
import os  # Importando a biblioteca os para limpar a tela

class ListaManager:
    def __init__(self):
        self.listas = {}

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

    def criar_lista(self, nome):
        if nome not in self.listas:
            self.listas[nome] = []
            print(f"Lista '{nome}' criada com sucesso.")
        else:
            print(f"Lista '{nome}' já existe.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        self.limpar_tela()  # Limpa a tela após a operação

    def adicionar_item(self, indice, item):
        nome = list(self.listas.keys())[indice]
        if nome in self.listas:
            self.listas[nome].append(item)
            print(f"Item '{item}' adicionado à lista '{nome}'.")
        else:
            print(f"Lista '{nome}' não encontrada.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        self.limpar_tela()  # Limpa a tela após a operação

    def mostrar_lista(self, indice):
        nome = list(self.listas.keys())[indice]
        if nome in self.listas:
            print(f"Lista '{nome}': {self.listas[nome]}")
        else:
            print(f"Lista '{nome}' não encontrada.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        self.limpar_tela()  # Limpa a tela após a operação

    def salvar_listas(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(self.listas, f)
        print(f"Listas salvas em '{arquivo}'.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        self.limpar_tela()  # Limpa a tela após a operação

    def carregar_listas(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.listas = json.load(f)
            print(f"Listas carregadas de '{arquivo}'.")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        self.limpar_tela()  # Limpa a tela após a operação

    def listar_opcoes(self):
        self.limpar_tela()  # Limpa a tela antes de mostrar as listas
        if not self.listas:
            print("Nenhuma lista disponível.")
        else:
            print("Listas disponíveis:")
            for i, nome in enumerate(self.listas.keys()):
                print(f"{i + 1}. {nome}")

def main():
    manager = ListaManager()
    
    while True:
        manager.limpar_tela()  # Limpa a tela antes de mostrar o menu
        print("\n1. Criar lista")
        print("2. Adicionar item à lista")
        print("3. Mostrar lista")
        print("4. Salvar listas")
        print("5. Carregar listas")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            manager.limpar_tela()  # Limpa a tela antes de criar lista
            nome = input("Nome da lista: ")
            manager.criar_lista(nome)
        elif escolha == '2':
            if not manager.listas:
                print("Nenhuma lista disponível para adicionar itens.")
                input("Pressione Enter para continuar...")
            else:
                manager.listar_opcoes()  # Mostra as listas disponíveis
                indice = int(input("Escolha o número da lista (ou 0 para voltar): ")) - 1
                if indice == -1:
                    continue  # Volta ao menu principal
                manager.adicionar_item(indice, input("Item a adicionar: "))
        elif escolha == '3':
            if not manager.listas:
                print("Nenhuma lista disponível para mostrar.")
                input("Pressione Enter para continuar...")
            else:
                manager.listar_opcoes()  # Mostra as listas disponíveis
                indice = int(input("Escolha o número da lista (ou 0 para voltar): ")) - 1
                if indice == -1:
                    continue  # Volta ao menu principal
                manager.mostrar_lista(indice)
        elif escolha == '4':
            manager.limpar_tela()  # Limpa a tela antes de salvar listas
            arquivo = input("Nome do arquivo para salvar (ou 0 para voltar): ")
            if arquivo == '0':
                continue  # Volta ao menu principal
            manager.salvar_listas(arquivo)
        elif escolha == '5':
            manager.limpar_tela()  # Limpa a tela antes de carregar listas
            arquivo = input("Nome do arquivo para carregar (ou 0 para voltar): ")
            if arquivo == '0':
                continue  # Volta ao menu principal
            manager.carregar_listas(arquivo)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
            manager.limpar_tela()  # Limpa a tela após a operação

if __name__ == "__main__":
    main()