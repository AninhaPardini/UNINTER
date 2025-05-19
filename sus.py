class Paciente:
    def __init__(self, num, cor):
        self.numero = num
        self.cor = cor
        self.proximo = None

def inserirSemPrioridade(nodo):
    global head
    if head is None:
        head = nodo
    else:
        atual = head
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = nodo

def inserirComPrioridade(nodo):
    global head
    if head is None or head.cor == "V":
        nodo.proximo = head
        head = nodo
    else:
        atual = head
        while atual.proximo is not None and atual.proximo.cor == "A":
            atual = atual.proximo
        nodo.proximo = atual.proximo
        atual.proximo = nodo

contador_A = 200
contador_V = 0
head = None

def inserir():
    global contador_A, contador_V, head
    while True:
        cor = input("Informe a cor do cartão (A/V): ").upper()
        if cor == "A":
            contador_A += 1
            numero = contador_A
            nodo = Paciente(numero, cor)
            inserirComPrioridade(nodo)
            break
        elif cor == "V":
            contador_V += 1
            numero = contador_V
            nodo = Paciente(numero, cor)
            inserirSemPrioridade(nodo)
            break
        else:
            print("Cor inválida. Use apenas A ou V.")

def imprimirListaEspera():
    atual = head
    if head is None:
        print("Não há pacientes na fila.")
    print("Pacientes na fila:")
    while atual is not None:
        print(f"Cartão: {atual.cor}, Número: {atual.numero}")
        atual = atual.proximo


def atenderPaciente():
    global head
    if head is None:
        print("Fila vazia. Nenhum paciente para chamar.")
    else:
        print(f"Chamando paciente do cartão {head.cor}, número {head.numero}")
        head = head.proximo

def menu():
    while True:
        print("\nMENU")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir()
        elif opcao == "2":
            imprimirListaEspera()
        elif opcao == "3":
            atenderPaciente()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente de novo.")

if __name__ == "__main__":
    menu()