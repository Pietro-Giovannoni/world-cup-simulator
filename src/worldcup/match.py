from dataclasses import dataclass
from turtle import home

from src.worldcup.team import Team


@dataclass
class Match:
    '''
    Object representing a match.

    Attributes:
        home (Team): home team.
        away (Team): away team.
        home_score (int): home team score.
        away_score (int): away team score.
        extra_time (bool): whether extra time is played.
        penalties (tuple[int, int]): match score after penalties, if played.
    '''
    home: Team
    away: Team
    home_score: int | None = None
    away_score: int | None = None
    extra_time: bool = False
    penalties: tuple[int, int] | None = None

    @property
    def winner(self) -> Team | None:
        '''
        If a match has been played, this (@property) function returns the winning team.
        '''
        if self.home_score is None or self.away_score is None:
            return None

        if self.home_score > self.away_score:
            return self.home

        if self.home_score < self.away_score:
            return self.away

        if self.penalties:
            if self.penalties[0] > self.penalties[1]:
                return self.home
            return self.away

        return None



    def __post_init__(self):
        '''
        Checks that all object attributes have the desired type.
        '''
        if not isinstance(self.home, Team):
            raise TypeError(f"Expected home as Team, got {type(self.home).__name__} instead.")

        if not isinstance(self.away, Team):
            raise TypeError(f"Expected away as Team, got {type(self.away).__name__} instead.")

        if self.home == self.away:
            raise ValueError("A team cannot play against itself.")

        for score in (self.home_score, self.away_score):
            if score is not None and not isinstance(score, int):
                raise TypeError("Scores must be integers or None.")

            if score is not None and score < 0:
                raise ValueError("Scores cannot be negative.")

        if not isinstance(self.extra_time, bool):
            raise TypeError(f"Expected extra_time as bool, got {type(self.extra_time).__name__} instead.")

        if self.penalties is not None:
            if not isinstance(self.penalties, tuple):
                raise TypeError('penalties must be None or a tuple.')

            if not all(isinstance(score, int) for score in self.penalties):
                raise TypeError('penalties scores must be integers.')

            if len(self.penalties) != 2:
                raise ValueError('penalties must contain exactly two values.')

            if any(score<0 for score in self.penalties):
                raise ValueError('penalties scores cannot be negative.')

            if self.penalties[0] == self.penalties[1]:
                raise ValueError('penalties cannot end in a draw.')

            if self.home_score != self.away_score:
                raise ValueError('Penalties can only occur after a draw.')

            if self.extra_time is False:
                raise ValueError('Penalties can only occur after extra-time.')
