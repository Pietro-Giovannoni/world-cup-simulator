from dataclasses import dataclass

@dataclass
class Team:
    """
    object representing a participant nation.

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

    def __post_init__(self):
        '''
        Checks that all object attributes have the desired type.
        '''
        if not isinstance(self.name, str):
            raise TypeError(f"Expected name as str, got {type(self.name).__name__} instead.")
        
        if not isinstance(self.code, str):
            raise TypeError(f"Expected code as str, got {type(self.code).__name__} instead.")
        
        if not isinstance(self.confederation, str):
            raise TypeError(f"Expected confederation as str, got {type(self.confederation).__name__} instead.")
        
        if not isinstance(self.ranking, int):
            raise TypeError(f"Expected ranking as int, got {type(self.ranking).__name__} instead.")
        
        if not isinstance(self.host, bool):
            raise TypeError(f"Expected host as bool, got {type(self.host).__name__} instead.")