class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __repr__(self):
        return self.numero

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
        self.proximo_verde = 1
        self.proximo_amarelo = 201

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()
        if cor not in ["A", "V"]:
            print("Cor inválida. Use 'A' para amarelo ou 'V' para verde.")
            return
        if cor == "V":
            numero = self.proximo_verde
            self.proximo_verde += 1
        elif cor == "A":
            numero = self.proximo_amarelo
            self.proximo_amarelo += 1
        novo_nodo = Nodo(numero, cor)
        if self.head is None:
            self.head = novo_nodo
        else:
            if cor == "V":
                self.inserirSemPrioridade(novo_nodo)
            elif cor == "A":
                self.inserirComPrioridade(novo_nodo)

    def inserirSemPrioridade(self, novo_nodo):
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if self.head.cor == "V":
            novo_nodo.proximo = self.head 
            self.head = novo_nodo 

        elif self.head.cor == "A":
            nodo_atual = self.head
            while nodo_atual.proximo != None and nodo_atual.proximo.cor == "A":
                nodo_atual = nodo_atual.proximo
            novo_nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = novo_nodo

    def imprimirListaEspera(self):
        if self.head != None:
            nodo_atual = self.head
            print("Pacientes na fila de espera:")
            while nodo_atual != None:
                print(f"{nodo_atual.cor}{nodo_atual.numero}")
                nodo_atual = nodo_atual.proximo
        else:
            print("Não há pacientes na fila de espera.")

    def atenderPaciente(self):
        if self.head != None:
            primeiro_fila = self.head
            print(f"Chamando paciente: {primeiro_fila.cor}{primeiro_fila.numero}")
            self.head = self.head.proximo
        else:
            print("Não há pacientes na fila de espera.")
            
lista = ListaEncadeadaSimples()
while True:
    print("1- Adicionar paciente a fila")
    print("2- Mostrar pacientes na fila")
    print("3- Chamar paciente")
    print("4- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        lista.inserir()
    elif opcao == "2":
        lista.imprimirListaEspera()
        pass
    elif opcao == "3":
        lista.atenderPaciente()
        pass
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

