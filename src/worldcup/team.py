from dataclasses import dataclass

@dataclass
class Team:
    name: str
    code: str
    confederation: str
    ranking: int