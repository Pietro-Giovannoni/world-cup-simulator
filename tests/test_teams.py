from src.worldcup.team import Team
import pytest


def test_team_creation(italy: Team):
    """
    Checks the correct construction of a Team object.
    """
    assert italy.name == 'Italy'
    assert italy.code == 'ITA'
    assert italy.confederation == 'UEFA'
    assert italy.ranking == 15
    assert italy.host is False



def test_team_creation_wrong_name():
    '''
    Checks that a wrong Team object declaration raises an exception.
    '''
    with pytest.raises(TypeError):
        Team(
            name=True,
            code='DEN',
            confederation='UEFA',
            ranking=21,
            host=False
        )

def test_team_creation_wrong_code():
    '''
    Checks that a wrong Team object declaration raises an exception.
    '''
    with pytest.raises(TypeError):
        Team(
            name='Denmark',
            code=123,
            confederation='UEFA',
            ranking=21,
            host=False
        )

def test_team_creation_wrong_confederation():
    '''
    Checks that a wrong Team object declaration raises an exception.
    '''
    with pytest.raises(TypeError):
        Team(
            name='Denmark',
            code='DEN',
            confederation=123,
            ranking=21,
            host=False
        )

def test_team_creation_wrong_ranking():
    '''
    Checks that a wrong Team object declaration raises an exception.
    '''
    with pytest.raises(TypeError):
        Team(
            name='Denmark',
            code='DEN',
            confederation='UEFA',
            ranking='21',
            host=False
        )

def test_team_creation_wrong_host():
    '''
    Checks that a wrong Team object declaration raises an exception.
    '''
    with pytest.raises(TypeError):
        Team(
            name='Denmark',
            code='DEN',
            confederation='UEFA',
            ranking=21,
            host='ABC'
        )
