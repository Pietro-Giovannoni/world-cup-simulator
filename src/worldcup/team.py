from dataclasses import dataclass

@dataclass
class Team:
    name: str
    federation: str
    ranking: int