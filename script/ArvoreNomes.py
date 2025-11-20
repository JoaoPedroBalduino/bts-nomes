from no import No

class ArvoreNomes:
    """Árvore Binária de Busca para armazenar nomes em ordem alfabética"""
    
    def __init__(self):
        self.raiz = None
    
    def inserir(self, nome):
        """Insere um nome na árvore"""
        self.raiz = self._inserir_recursivo(self.raiz, nome)
        print(f"✓ Nome '{nome}' inserido com sucesso!")
    
    def _inserir_recursivo(self, atual, nome):
        """Método recursivo privado para inserção"""
        if atual is None:
            return No(nome)
        
        if nome.lower() < atual.nome.lower():
            atual.esquerda = self._inserir_recursivo(atual.esquerda, nome)
        elif nome.lower() > atual.nome.lower():
            atual.direita = self._inserir_recursivo(atual.direita, nome)
        else:
            print("Nome já existe na árvore!")
        
        return atual

    def listar_em_ordem(self):
        print("\n Nomes em ordem alfabética:")
        print("-"*40)
        if self.raiz is None:
            print("(Árvore vazia)")
        else:
            self._listar_em_ordem_recursivo(self.raiz)
        print()

    def _listar_em_ordem_recursivo(self, no):
        """Percurso in-order: esquerda → raiz → direita"""
        if no is not None:
            self._listar_em_ordem_recursivo(no.esquerda)
            print(f"-> {no.nome}")
            self._listar_em_ordem_recursivo(no.direita)

    def listar_reversa(self):
        print("\n Nomes em ordem decrescente")
        print("-"*40)
        if self.raiz is None:
            print("(Árvore vazia)")
        else:
            self._lista_reversa_recursivo(self.raiz)
        print()

    def _lista_reversa_recursivo(self, no):
        """Percurso reverso: direita → raiz → esquerda"""
        if no is not None:
            self._lista_reversa_recursivo(no.direita)
            print()
            self._lista_reversa_recursivo(no.esquerda)

    def buscar(self, nome):
        return self._buscar_recursivo(self.raiz, nome):

    def _buscar_recursivo(self, atual, nome):
        if atual is None:
            return False
        if nome.lower() == atual.nome.lower():
            return True
        elif nome.lower() < atual.nome.lower():
            return self._buscar_recursivo(atual.esquerta, nome)
        else:
            return self._buscar_recursivo(atual.direita, nome)

    def contar(self):
        return self._contar_recursivo(self.raiz)

    def _contar_recursivo(self, no):
        if no is None:
            return 0
        return 1 + self._contar_recursivo(no.esquerda) + self._contar_recursivo(no.direita)

