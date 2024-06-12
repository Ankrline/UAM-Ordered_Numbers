class Lista:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)


class Pilha:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def esta_vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)


class Fila:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)


# Passo 1
lista = Lista()
for i in range(1, 6):
    lista.inserir(i)

# Passo 2
pilha = Pilha()
for _ in range(lista.tamanho()):
    pilha.inserir(lista.remover())

# Passo 3
fila = Fila()
for _ in range(pilha.tamanho()):
    fila.inserir(pilha.remover())

# Passo 4
for i in range(6, 11):
    lista.inserir(i)

# Passo 5
for _ in range(lista.tamanho()):
    pilha.inserir(lista.remover())

for _ in range(pilha.tamanho()):
    fila.inserir(pilha.remover())

# Passo 6
print("Números na fila:")
while not fila.esta_vazia():
    print(fila.remover())
