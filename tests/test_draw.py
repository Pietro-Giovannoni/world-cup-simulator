import pytest

from src.worldcup.draw import can_add_team, create_pots, _create_groups, _draw_pot
from src.worldcup.group import Group
from src.worldcup.team import Team
from random import Random


# create_pots()
def test_create_pots(algeria: Team, argentina: Team, austria: Team, canada: Team):
    """
    Tests the `create_pots` function with a valid input.
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
        create_pots(teams=True) # pyright: ignore[reportArgumentType]

def test_create_pots_invalid_nations():
    with pytest.raises(TypeError):
        create_pots(teams=[], nations='four', n_pots=1) # pyright: ignore[reportArgumentType]

def test_create_pots_invalid_n_pots():
    with pytest.raises(TypeError):
        create_pots(teams=[], nations=4, n_pots='two') # pyright: ignore[reportArgumentType]

def test_create_pots_zero_pots():
    with pytest.raises(ValueError):
        create_pots(teams=[], nations=4, n_pots=0)

def test_create_pots_zero_nations():
    with pytest.raises(ValueError):
        create_pots(teams=[], nations=0, n_pots=1)

def test_create_pots_nations_mismatch(argentina: Team):
    '''
    Tests than creating pots where the declared number of nations
    is different than the actual one, raises an exception.
    '''
    with pytest.raises(ValueError):
        create_pots(teams=[argentina], nations=4)

def test_create_pots_not_divisible(teams_j: list):
    '''
    Tests that creating pots where the number of nations is not divisible by the number of pots
    raises an exception, because it would cause incomplete pots.
    '''
    with pytest.raises(ValueError):
        create_pots(teams=teams_j, nations=4, n_pots=3)

def test_create_pots_too_many_hosts(usa: Team, canada: Team, argentina: Team):
    with pytest.raises(ValueError):
        create_pots(
            teams=[usa, canada, argentina],
            nations=3,
            n_pots=3
            )



# can_add_team()
def test_can_add_team(argentina: Team, empty_group: Group):
    """
    Tests the `can_add_team` function with a valid input.
    """
    assert can_add_team(team=argentina, group=empty_group) is True

def test_can_add_team_wrong_team(empty_group: Group):
    """
    Tests the `can_add_team` function with a wrong team.
    """
    with pytest.raises(TypeError):
        can_add_team(team=1, group=empty_group) # pyright: ignore[reportArgumentType]

def test_can_add_team_wrong_group(argentina: Team):
    """
    Tests the `can_add_team` function with a wrong group.
    """
    with pytest.raises(TypeError):
        can_add_team(team=argentina, group=3) # pyright: ignore[reportArgumentType]

def test_can_add_team_full_group(italy: Team, full_group: Group):
    """
    Tests the `can_add_team` function with an already full group.
    """
    assert can_add_team(team=italy, group=full_group) is False

def test_can_add_team_double_team(austria: Team, usa: Team):
    """
    Tests the `can_add_team` function with a team that is already in the group.
    """
    group_a = Group(
        name='A',
        teams=[austria, usa],
        capacity=3
    )
    assert can_add_team(team=austria, group=group_a) is False

def test_can_add_team_too_many_uefa(austria: Team, france: Team, italy: Team):
    """
    Tests the `can_add_team` function with more than two UEFA nations.
    """
    euro_group = Group(
        name='B',
        teams=[austria, france]
    )

    assert can_add_team(team=italy, group=euro_group) is False

def test_can_add_team_too_many_non_uefa(curacao: Team, usa: Team):
    """
    Tests the `can_add_team` function with more than one non-UEFA nation.
    """
    american_group = Group(
        name='C',
        teams=[usa]
    )

    assert can_add_team(team=curacao, group=american_group) is False

def test_can_add_team_second_uefa(argentina: Team, france: Team, italy: Team):
    """
    Tests the `can_add_team` function with a second UEFA nation.
    """
    wc_group = Group(
        name='A',
        teams=[argentina, france]
    )
    assert can_add_team(team=italy, group=wc_group) is True


# _create_groups()
def test_create_groups(algeria: Team, argentina: Team, austria: Team, canada: Team):
    '''
    Tests the `_create_groups()` function with a valid input.
    '''
    sample_pot = create_pots(
        teams=[algeria, argentina, austria, canada],
        nations=4,
        n_pots=2
        )
    groups = _create_groups(sample_pot)

    assert len(groups) == 2
    assert list(groups.keys()) == ['A', 'B']
    assert isinstance(groups['A'], Group)
    assert isinstance(groups['B'], Group)
    assert groups['A'].name == 'A'
    assert groups['B'].name == 'B'
    assert groups['A'].teams == []
    assert groups['B'].teams == []

def test_create_groups_wrong_pots():
    '''
    Tests the `_create_groups()` function with a wrong `pots`.
    '''
    with pytest.raises(TypeError):
        _create_groups(pots = 'No')

def test_create_groups_empty_pots():
    '''
    Tests the `_create_groups()` function with empty `pots`.
    '''
    with pytest.raises(ValueError):
            _create_groups(pots = {})

def test_create_groups_partially_empty_pots(argentina: Team):
    '''
    Tests the `_create_groups()` function with partially empty `pots`.
    '''
    with pytest.raises(ValueError):
            _create_groups(pots = {1:[argentina], 2:[]})

def test_create_groups_different_sizes(argentina: Team, italy: Team, france: Team):
    '''
        Tests the `_create_groups()` function with unevenly sized `pots`.
    '''
    with pytest.raises(ValueError):
                _create_groups(pots = {1:[argentina], 2:[france, italy]})

# _draw_pot()
def test_draw_pot_successful(algeria: Team, argentina: Team, austria: Team, canada: Team):
    '''
    Tests the `_draw_pot()` function with a successful result.
    '''
    pots = create_pots(
        teams=[algeria, argentina, austria, canada],
        nations=4, 
        n_pots=2
        )
    groups = _create_groups(pots)
    rng = Random(38)

    assert  _draw_pot(pot=pots[1], groups=groups, rng=rng) is True
    assert all(len(group.teams) == 1 for group in groups.values())
    assert _draw_pot(pot=pots[2], groups=groups, rng=rng) is True
    assert all(len(group.teams) == 2 for group in groups.values())


def test_draw_pot_dead_end(canada: Team, curacao: Team, france: Team, usa: Team):
    '''
    Tests the `_draw_pot()` function with teams that lead to a dead end.
    '''
    pots = create_pots(
            teams=[canada, curacao, france, usa],
            nations=4, 
            n_pots=2
            )
    groups = _create_groups(pots)
    rng = Random(38)

    assert _draw_pot(pot=pots[1], groups=groups, rng=rng) is True
    assert _draw_pot(pot=pots[2], groups=groups, rng=rng) is False

