from dataclasses import dataclass, field
from src.worldcup.team import Team
from src.worldcup.group import Group

@dataclass
class Tournament:
    """
    Object representing the state of a tournament.
    """
    teams: list[Team] = field(default_factory=list)
    groups: list[Group] = field(default_factory=list)