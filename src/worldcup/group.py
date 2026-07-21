from dataclasses import dataclass, field
from src.worldcup.team import Team

@dataclass
class Group:
    """
    Object for group stage groups.

    Attributes:
        name (str): Group name.
        teams (list[Team]): List of participating nations.
                            Default value is a fresh empty list, for every new instance. \\
                            This is to prevent different Group objects from sharing the same `teams` default value.
        capacity (int): Group capacity; defualt is 4.
    """
    name: str
    teams: list[Team] = field(default_factory=list)
    capacity: int = 4


    def __post_init__(self):
        '''
        Checks that all object attributes have the desired type.
        '''
        if not isinstance(self.name, str):
            raise TypeError(f"Expected name as str, got {type(self.name).__name__} instead.")

        if not isinstance(self.teams, list):
            raise TypeError(f"Expected teams as list, got {type(self.teams).__name__} instead.")

        if not all(isinstance(nation, Team) for nation in self.teams):
            raise TypeError("All elements in teams must be Team objects.")

        if not isinstance(self.capacity, int):
            raise TypeError(f"Expected capacity as int, got {type(self.capacity).__name__} instead.")

        if self.capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")

        if len(self.teams) > self.capacity:
            raise ValueError(f"A group cannot contain more than {self.capacity} teams.")



    def add_team(self, team: Team):
        '''
        Adds a new team to this group.\\
        Group must have maximum 4 teams and the new one must different from the ones already in.
        '''

        if len(self.teams) >= self.capacity:
            raise ValueError("Group already full.")

        if not isinstance(team, Team):
            raise TypeError(f"Expected Team, got {type(team).__name__} instead.")

        if team in self.teams:
            raise ValueError("Team already in this group.")

        self.teams.append(team)
