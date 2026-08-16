class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None, None, None, None, 
                       None, None, None, None, None, None]

    def ascii_letra(self, letra):
        if letra == "A":
            return 65
        elif letra == "B":
            return 66
        elif letra == "C":
            return 67
        elif letra == "D":
            return 68
        elif letra == "E":
            return 69
        elif letra == "F":
            return 70
        elif letra == "G":
            return 71
        elif letra == "I":
            return 73
        elif letra == "J":
            return 74
        elif letra == "L":
            return 76
        elif letra == "M":
            return 77
        elif letra == "N":
            return 78
        elif letra == "O":
            return 79
        elif letra == "P":
            return 80
        elif letra == "R":
            return 82
        elif letra == "S":
            return 83
        elif letra == "T":
            return 84
        
        # 0: RN -> MS -> GO -> SC -> None
        # 1: AL -> BA -> RO -> MT -> None
        # 2: MA -> SE -> AC -> AM -> ES -> PR -> None
        # 3: PI -> TO -> SP -> None
        # 4: AO -> RR -> None
        # 5: AP -> PA -> RS -> None
        # 6: CE -> PB -> RJ -> None
        # 7: DF -> None
        # 8: MG -> None
        # 9: PE -> None

    def funcao_hash(self, sigla):
        sigla = sigla.upper()
        if sigla == "DF":
            posicao = 7
        else:
            char_1 = self.ascii_letra(sigla[0])
            char_2 = self.ascii_letra(sigla[1])
            posicao = (char_1 + char_2) % 10
        return posicao

    def inserir(self, sigla, nomeEstado):
        novo_nodo = Nodo(sigla, nomeEstado)
        posicao = self.funcao_hash(sigla)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo


    def imprimirTabela(self):
        for posicao in range(10):
            nodo_atual = self.tabela[posicao]
            if nodo_atual is None:
                print(f"{posicao}: None")
            else:
                print(f"{posicao}:", end=" ")
                while nodo_atual is not None:
                    print(f"{nodo_atual.sigla}", end=" -> ")
                    nodo_atual = nodo_atual.proximo
                print("None") # Quebra de linha após imprimir todos os nodos na posição


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
# Estado ficticio
tabela.inserir("AO", "Aimeê Olinek")
tabela.imprimirTabela()