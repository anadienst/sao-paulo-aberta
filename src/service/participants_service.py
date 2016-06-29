participants = []


def add_participant(nome):
    participants.append(nome)


def get_participant(nome):
    position = participants.index(nome)
    print(participants.get(position))


def remove_participant(nome):
    participants.remove(nome)


def count_participant(nome):
    return participants.count(nome)


def update_participant(nome):
    position = participants.index(nome)
    participant = participants.get(position)
    participant.nome = "new_name"
