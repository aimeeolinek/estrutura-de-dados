class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None # Aponta para o próximo nodo da lista

    def __repr__(self):
        return self.numero

class ListaEncadeadaSimples:
    def __init__(self):
        # Head aponta para o primeiro elemento da lista.
        # A lista começa vazia.
        self.head = None
        self.proximo_verde = 1
        self.proximo_amarelo = 201

    def inserir(self):
        # Solicita a cor do cartão e padroniza a entrada para letras maiúsculas.
        cor = input("Informe a cor do cartão (A/V): ").upper()

        # Verifica se a cor informada é válida.
        if cor not in ["A", "V"]:
            print("Cor inválida. Use 'A' para amarelo ou 'V' para verde.")
            return
        
        # Atribui o próximo número disponível de acordo com a cor.
        if cor == "V":
            numero = self.proximo_verde
            self.proximo_verde += 1
        elif cor == "A":
            numero = self.proximo_amarelo
            self.proximo_amarelo += 1

        # Cria um novo nodo com o número e a cor do cartão.
        novo_nodo = Nodo(numero, cor)

        # Se a lista estiver vazia, o novo nodo se torna o primeiro elemento.
        if self.head is None:
            self.head = novo_nodo

        # Cartões verdes são inseridos no final da fila.
        elif cor == "V":
            self.inserirSemPrioridade(novo_nodo)

        # Cartões amarelos são inseridos antes dos cartões verdes.
        elif cor == "A":
            self.inserirComPrioridade(novo_nodo)

    def inserirSemPrioridade(self, novo_nodo):
        # Começa o percurso pelo primeiro nodo da lista.
        nodo_atual = self.head

        # Percorre a lista até encontrar o último nodo.
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo

        # O último nodo passa a apontar para o novo nodo.
        nodo_atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        # Se o primeiro nodo for verde, o novo amarelo passa a ser o primeiro.
        if self.head.cor == "V":
            novo_nodo.proximo = self.head 
            self.head = novo_nodo 

        # Caso já existam cartões amarelos, percorre até o último amarelo.
        elif self.head.cor == "A":
            nodo_atual = self.head
            while nodo_atual.proximo != None and nodo_atual.proximo.cor == "A":
                nodo_atual = nodo_atual.proximo

            # Insere o novo cartão depois dos amarelos e antes dos verdes.
            novo_nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = novo_nodo

    def imprimirListaEspera(self):
        # Percorre todos os nodos da lista, começando pelo head,
        # e imprime a cor e o número de cada paciente.
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
            # O primeiro paciente é removido fazendo o head apontar para o próximo nodo.
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

