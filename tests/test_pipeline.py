from pathlib import Path

from src.worldcup.data_loader import load_teams
from src.worldcup.draw import create_pots, draw_groups


def test_full_pipeline():
    csv_path = Path(__file__).resolve().parents[1] / "data" / "teams.csv"

    teams = load_teams(str(csv_path))
    pots = create_pots(teams=teams, nations=48, n_pots=4)
    groups = draw_groups(pots=pots, seed=47, max_attempts=10)

    assert len(teams) == 48
    assert len(pots) == 4
    assert len(groups) == 12
    assert all(len(group.teams)==4 for group in groups.values())

    all_codes = [team.code for team in teams]
    drawn_codes = [team.code for group in groups.values() for team in group.teams]
    assert sorted(all_codes) == sorted(drawn_codes)

    for group in groups.values():
        confs = [team.confederation for team in group.teams]
        for conf in set(confs):
            if conf=='UEFA':
                assert confs.count(conf) <= 2
            else:
                assert confs.count(conf) <= 1
