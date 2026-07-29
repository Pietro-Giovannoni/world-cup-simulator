from pathlib import Path

from rich.console import Console
from rich.table import Table

from src.worldcup.data_loader import load_teams
from src.worldcup.draw import create_pots, draw_groups
from src.worldcup.group import Group


def display_groups(groups: dict[str, Group]) -> None:
    '''
    Displays the groups resulting from a group stage draw.
    '''
    table = Table(title='World Cup group stage draw')
    table.add_column('Group', style='bold')
    table.add_column('Team', style='bold')
    table.add_column('Code')
    table.add_column('Confederation')
    table.add_column('Ranking', justify='right')

    for group_name, group in groups.items():
        for i, team in enumerate(group.teams):
            table.add_row(
                group_name,
                team.name,
                team.code,
                team.confederation,
                str(team.ranking),
                end_section = (i==len(group.teams)-1)
            )

    Console().print(table)


def main():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / 'data' / 'teams.csv'

    teams = load_teams(str(csv_path))
    pots = create_pots(teams=teams)
    groups = draw_groups(pots=pots, seed=47, max_attempts=10)

    display_groups(groups)


if __name__ == '__main__':
    main()
