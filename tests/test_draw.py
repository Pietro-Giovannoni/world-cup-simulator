import pytest
from src.worldcup.team import Team
from src.worldcup.draw import create_pots

def test_create_pots(algeria: Team, argentina: Team, austria: Team, canada: Team):
    """
    Tests the create_pots function with a valid input.
    """
    teams = [
        algeria, argentina, austria, canada
    ]
    
    pots = create_pots(teams=teams, nations=4, n_pots=2)
    
    assert len(pots) == 2
    assert all(len(pot) == 2 for pot in pots.values())
    assert canada in pots[1] 
    assert argentina in pots[1]
    assert austria in pots[2]
    assert algeria in pots[2]

def test_create_pots_invalid_teams(): 
    with pytest.raises(TypeError):
        create_pots(teams=True)

def test_create_pots_zero_pots():
    with pytest.raises(ValueError):
        create_pots(teams=[], nations=4, n_pots=0)

def test_create_pots_zero_nations():
    with pytest.raises(ValueError):
        create_pots(teams=[], nations=0, n_pots=1)

def test_create_pots_nations_mismatch(argentina):
    with pytest.raises(ValueError):
        create_pots(teams=[argentina], nations=4)

def test_create_pots_not_divisible(teams_j):
    with pytest.raises(ValueError):
        create_pots(teams=teams_j, nations=4, n_pots=3)

def test_create_pots_too_many_hosts(usa, canada, argentina):
    with pytest.raises(ValueError):
        create_pots(
            teams=[usa, canada, argentina],
            nations=3,
            n_pots=3
            )

