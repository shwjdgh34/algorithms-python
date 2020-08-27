from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name: Text, skills: List[Text], load: int):
        self._name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id: Text, restrictions: List[Text]):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return[agent.load for agent in agents if agent.load < 3]

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        pass
        # raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        filteredAgents = super()._filter_loaded_agents(agents)
        leastLoad = 3
        if not agents:
            raise NoAgentFoundException

        leastLoaded = agents[0]
        for agent in filteredAgents:
            if agent.load < leastLoad:
                leastLoad = agent.load
                leastLoaded = agent
        return leastLoaded

        # class LeastFlexibleAgent(FinderPolicy):
        #     def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        #         raise NotImplemented
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
agent3 = Agent(name="C", skills=["English", "Japanese"], load=3)

nono = FinderPolicy()
print(nono._filter_loaded_agents([agent1, agent2, agent3]))
