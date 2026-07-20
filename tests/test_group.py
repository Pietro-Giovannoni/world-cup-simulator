from src.worldcup.group import Group
from src.worldcup.team import Team
import pytest


def test_group_creation(argentina: Team):
    """
    Checks the correct construction of a Group object.
    """
    group_a = Group(
        name='A',
        teams=[argentina]
    )
    assert group_a.name == 'A'
    assert group_a.teams == [argentina]


def test_group_creation_wrong_name(argentina: Team):
    with pytest.raises(TypeError):
        Group(
            name=5,
            teams=[argentina]
        )


def test_group_creation_wrong_team(argentina: Team):
    with pytest.raises(TypeError):
        Group(
            name='A',
            teams=argentina
        )


def test_group_creation_too_many_teams(argentina: Team, austria: Team, algeria: Team, jordan: Team, curacao: Team):
    """
    Checks that creating a group with more than four teams raises an exception.
    """
    with pytest.raises(ValueError):
        Group(
            name='A',
            teams=[argentina, austria, algeria, jordan, curacao]
        )


def test_group_adding_double_team(full_group: Group, argentina: Team):
    """
    Checks that adding a team twice to the same group raises an exception.
    """
    with pytest.raises(ValueError):
        full_group.add_team(argentina)


def test_group_adding_wrong_team(argentina: Team):
    """
    Checks that adding an invalid team to a group raises an exception.
    """
    with pytest.raises(TypeError):
        group_a = Group(
            name='A',
            teams=[argentina]
        )
        group_a.add_team('austria')


def test_group_adding_fifth_team(full_group: Group, curacao: Team):
    """
    Checks that adding a fifth team to a group raises an exception.
    """
    with pytest.raises(ValueError):
        full_group.add_team(curacao)



