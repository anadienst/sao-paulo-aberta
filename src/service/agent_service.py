agents = []


def add_agent(agent):
    agents.append(agent)


def remove_agent(name):
    agent = find_agent_by_name(name)
    if agent is not None:
        agents.remove(agent)
        return True
    return False


def find_agent_by_name(name):
    for agent in agents:
        if agent.name == name:
            return agent
    return None

