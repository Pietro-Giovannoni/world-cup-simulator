from random import Random, shuffle
from string import ascii_uppercase

from src.worldcup.group import Group
from src.worldcup.team import Team

UEFA='UEFA' # constant

def create_pots(teams: list[Team], nations: int=48, n_pots: int=4) -> dict[int, list[Team]]:
    """
    Organize participating teams into seeding pots.

    Args:
        teams (list[Team]): Participating teams.
        nations (int): Expected number of participating teams.
        n_pots (int): Number of seeding pots.

    Returns:
        dict[int, list[Team]]: Mapping from pot number to the teams assigned to it.
    """

    if not isinstance(teams, list):
        raise TypeError("teams must be a list.")

    if not all(isinstance(team, Team) for team in teams):
        raise TypeError("Every element of teams must be a Team object.")

    if not isinstance(nations, int):
        raise TypeError("nations must be an integer.")

    if not isinstance(n_pots, int):
        raise TypeError("n_pots must be an integer.")

    if n_pots <= 0:
        raise ValueError("Number of pots must be positive.")

    if nations <= 0:
        raise ValueError("Number of nations must be positive.")

    if len(teams) != nations:
        raise ValueError(f"Must have {nations} teams in this tournament.")

    if nations % n_pots != 0:
        raise ValueError(f"The number of nations must be divisible by {n_pots}.")

    teams_per_pot = nations // n_pots

    # separating host nations from qualified ones
    hosts = [nation for nation in teams if nation.host]
    qualified = [nation for nation in teams if not nation.host]

    # cannot place all hosts in first pot if they are too many.
    if len(hosts) > teams_per_pot:
        raise ValueError("Too many host nations!")


    # create as many pots as dictated by n_pots.
    pots = {
        pot: []
        for pot in range(1, n_pots+1)
    }

    # host nations go in the first pot.
    pots[1].extend(hosts)

    # other nations are placed in ascending order of ranking.
    qualified = sorted(
        qualified,
        key=lambda nation: nation.ranking
    )

    for nation in qualified:
        for pot in pots.values():
            if len(pot) < teams_per_pot:
                pot.append(nation)
                break


    # Check that every team has been assigned to some pot.
    if sum(len(pot) for pot in pots.values()) != nations:
        raise RuntimeError("Not all teams have been assigned.")

    return pots


def can_add_team(team: Team, group: Group) -> bool:
    """
    Checks whether the selected team can be added to the selected group, according to FIFA rules.\\
    Default number of teams per group is 4.
    """

    if not isinstance(team, Team):
        raise TypeError(f'Expected Team, got {type(team).__name__} instead.')

    if not isinstance(group, Group):
        raise TypeError(f'Expected Group, got {type(group).__name__} instead.')

    if group.capacity <= 0:
        raise ValueError('Group capacity must be positive.')

    if len(group.teams) >= group.capacity or team in group.teams:
        return False

    # how many occurrences of this confederation are there in the group?
    conf_count = sum(
        team.confederation == member.confederation
        for member in group.teams
    )

    # a group cannot have more than two UEFA nations
    if team.confederation == UEFA:
        return conf_count < 2

    # a group cannot have more than one non-UEFA nation
    return conf_count < 1


def _create_groups(pots: dict[int, list[Team]]) -> dict[str, Group]:
    '''
    (Private) Creates groups to be populated during the draw.
    Args:
        pots (dict[int, list[Team]]): The pots to draw groups from.

    Returns:
        groups (dict[str, Group]): The groups named using capital letters.
    '''
    if not isinstance(pots, dict):
        raise TypeError(f'Expected pots as dict, got {type(pots).__name__} instead.')

    if not all(isinstance(pot, list) for pot in pots.values()):
        raise TypeError('All pots values must be lists.')

    if not all(isinstance(team, Team) for pot in pots.values() for team in pot):
        raise TypeError('All pots values must be lists of Team objects.')

    if len(pots) == 0 or any(len(pot)==0 for pot in pots.values()):
        raise ValueError('Some pots are empty.')

    pot_sizes = [len(pot) for pot in pots.values()]
    if len(set(pot_sizes)) != 1:
        raise ValueError('Not every pot has the same amount of teams.')


    n_groups = len(next(iter(pots.values())))
    groups = {
        ascii_uppercase[i] : Group(name=ascii_uppercase[i], teams=[], capacity=len(pots))
        for i in range(n_groups)
    }
    return groups




def draw_groups(pots: dict[int, list[Team]], seed: int|None = None) -> dict[str, Group]:
    """
    Draws group stage groups from the given pots.

    Args:
        pots (dict[int, list[Team]]):    The pots to draw groups from.
        seed (int or None):         Optional seed for the random number generator.

    Returns:
        groups (dict[str, Group]):  The groups ordered by name.
    """
    # validation
    if not isinstance(seed, int) and seed is not None:
        raise TypeError(f'Expected seed as int, got {type(seed).__name__} instead.')

    groups = _create_groups(pots)
    return groups
