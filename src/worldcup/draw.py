from src.worldcup.team import Team

def create_pots(teams: list[Team], nations: int=48, n_pots: int=4) -> dict[int, list[Team]]:
    """
    Organize participating teams into seeding pots.

    Args:
        teams (list[Team]): Participating teams.
        nations (int): Expected number of participating teams.
        n_pots (int): Number of seeding pots.

    Returns:
        dict[int, list[Team]]: Mapping from pot number to the teams assigned to it.

    Raises:
        ValueError: If the input is inconsistent.
    """

    if not isinstance(teams, list):
        raise TypeError("teams must be a list.")
    
    if not all(isinstance(team, Team) for team in teams):
        raise TypeError("Every element of teams must be a Team object.")

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