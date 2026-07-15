from src.worldcup.team import Team

def load_teams(file_path: str) -> list[Team]:
    """
    Loads teams from a CSV file and returns a list of teams.
    """ 
    teams = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            name, code, confederation, ranking, host = line.strip().split(',')
            team = Team(
                name=name, 
                code=code,
                confederation=confederation, 
                ranking=int(ranking),
                host=host=="True"
                )
            teams.append(team)
    return teams

