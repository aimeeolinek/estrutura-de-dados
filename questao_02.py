class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None
        # Aponta para o próximo estado da lista

class TabelaHash:
    def __init__(self):
        # Cria 10 posições, inicialmente vazias.
        # Cada posição representa o início (head) de uma lista encadeada.
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        # Padroniza a sigla para letras maiúsculas.
        sigla = sigla.upper()
        # Por determinação do enunciado, DF sempre ocupa a posição 7.
        if sigla == "DF":
            posicao = 7
        else:
            # Obtém os valores ASCII das duas letras da sigla.
            char_1 = ord(sigla[0])
            char_2 = ord(sigla[1])
            # Calcula a posição utilizando a soma dos valores ASCII 
            # e o resto da divisão por 10
            posicao = (char_1 + char_2) % 10
        return posicao

    def inserir(self, sigla, nomeEstado):
        # Cria um nodo contendo a sigla e o nome do estado.
        novo_nodo = Nodo(sigla, nomeEstado)
        # A função hash determina em qual posição da tabela o nodo será inserido.
        posicao = self.funcao_hash(sigla)

        # O novo nodo aponta para o atual primeiro elemento da lista.
        # Isso permite tratar possíveis colisões através do encadeamento.
        novo_nodo.proximo = self.tabela[posicao]
        # O novo nodo passa a ser o primeiro elemento da lista.
        self.tabela[posicao] = novo_nodo

    def imprimirTabela(self):
        # Percorre as 10 posições da tabela hash.
        for posicao in range(10):
            # O conteúdo da posição representa o primeiro nodo da lista.
            nodo_atual = self.tabela[posicao]
            if nodo_atual is None:
                print(f"{posicao}: None")
            else:
                print(f"{posicao}:", end=" ")
                # Percorre todos os nodos da lista encadeada daquela posição.
                while nodo_atual is not None:
                    print(f"{nodo_atual.sigla}", end=" -> ")
                    nodo_atual = nodo_atual.proximo
                print("None") # Indica o final da lista.

tabela = TabelaHash()
# Sul
tabela.inserir("PR", "Paraná")
tabela.inserir("SC", "Santa Catarina")
tabela.inserir("RS", "Rio Grande do Sul")
# Sudeste
tabela.inserir("SP", "São Paulo")
tabela.inserir("RJ", "Rio de Janeiro")
tabela.inserir("MG", "Minas Gerais")
tabela.inserir("ES", "Espírito Santo")
# Centro-Oeste
tabela.inserir("DF", "Distrito Federal")
tabela.inserir("GO", "Goiás")
tabela.inserir("MT", "Mato Grosso")
tabela.inserir("MS", "Mato Grosso do Sul")
# Norte
tabela.inserir("AM", "Amazonas")
tabela.inserir("TO", "Tocantins")
tabela.inserir("RR", "Roraima")
tabela.inserir("AC", "Acre")
tabela.inserir("PA", "Pará")
tabela.inserir("AP", "Amapá")
tabela.inserir("RO", "Rondônia")
# Nordeste
tabela.inserir("BA", "Bahia")
tabela.inserir("AL", "Alagoas")
tabela.inserir("PE", "Pernambuco")
tabela.inserir("PB", "Paraíba")
tabela.inserir("SE", "Sergipe")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("CE", "Ceará")
tabela.inserir("MA", "Maranhão")
tabela.inserir("PI", "Piauí")
# Estado fictício
tabela.inserir("AO", "Aimeê Olinek")
tabela.imprimirTabela()