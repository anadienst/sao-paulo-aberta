participantes = ["felipe"]
def adicionar_participantes(nome):
    participantes.append(nome)

def ler_participantes(nome):
    position = participantes.index(nome)
    print(participantes.get(position))

def remover_participantes(nome):
    participantes.remove(nome)

def contagem_participantes(nome):
    return participantes.count(nome)

def update_particpante(nome):
    position = participantes.index(nome)
    participante = participantes.get(position)
    participante.nome = "novo_nome"



