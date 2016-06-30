#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.agent import Agent
from service import agent_service


def agent_form():
    agent = Agent()
    agent.name = raw_input("Nome do agente:\n")
    agent.address = raw_input("Endereço do agente:\n")
    agent.telephone = raw_input("Telefone do agente:\n")
    agent.category = raw_input("Categoria a qual o agente pertence:\n")
    agent_service.add_agent(agent)


def show_agents():
    print("Dados cadastrados\n")
    for agent in agent_service.agents:
        show_agent_infos(agent)


def show_agent_infos(agent):
    print(agent.name)
    print(agent.address)
    print(agent.telephone)
    print(agent.category)


def show_agent():
    name = raw_input("Informe o nome do agente\n")
    agent = agent_service.find_agent_by_name(name)
    show_agent_infos(agent)


def remove_agent():
    name = raw_input("Informe o nome do agente\n")
    success = agent_service.remove_agent(name)
    if success:
        print("Agente removido com sucesso!\n")
    else:
        print("Agente não cadastrado")


def update_agent():
    name = raw_input("Informe o nome do agente\n")
    agent = agent_service.find_agent_by_name(name)
    if agent is not None:
        agent.name = raw_input("Nome do agente:\n")
        agent.address = raw_input("Endereço do agente:\n")
        agent.telephone = raw_input("Telefone do agente:\n")
        agent.category = raw_input("Categoria a qual o agente pertence:\n")


def main_menu():
    print("Informe o número da opção")
    print("1 - Cadastrar agente")
    print("2 - Remover agente")
    print("3 - Buscar agente por nome")
    print("4 - Atualizar agente")
    print("5 - Listar agentes")

    option = raw_input("Opção:\n")
    option = int(option)

    if option == 1:
        agent_form()
        main_menu()

    elif option == 2:
        remove_agent()
        main_menu()

    elif option == 3:
        show_agent()
        main_menu()

    elif option == 4:
        update_agent()
        main_menu()

    elif option == 5:
        show_agents()
        main_menu()


if __name__ == '__main__':
    main_menu()
