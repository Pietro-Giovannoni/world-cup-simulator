from dataclasses import dataclass

@dataclass
class Team:
    """
    class for participant nations.

    Args:
        name (str): Full nation name;
        code (str): Short nation name;
        confederation (str): Belonging continental confederation;
        ranking (int): Current position in the FIFA nationals ranking.
        host (bool): Whether this nations hosts the tournament.
    """
    name: str
    code: str
    confederation: str
    ranking: int
    host: bool