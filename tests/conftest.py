from src.worldcup.team import Team
from src.worldcup.group import Group
import pytest

# preparing teams to be used in tests...
@pytest.fixture
def algeria():
    return Team(
        name='Algeria',
        code='ALG',
        confederation='CAF',
        ranking=29,
        host=False
        )

@pytest.fixture
def argentina():
    return Team(
        name='Argentina',
        code='ARG',
        confederation='CONMEBOL',
        ranking=2,
        host=False
        )

@pytest.fixture
def austria():
    return Team(
        name='Austria',
        code='AUT',
        confederation='UEFA',
        ranking=23,
        host=False
        )

@pytest.fixture
def canada():
    return Team(
        name='Canada',
        code='CAN',
        confederation='CONCACAF',
        ranking=30,
        host=True
        )

@pytest.fixture
def curacao():
    return Team(
        name='Curacao',
        code='CUR',
        confederation='CONCACAF',
        ranking=82,
        host=False
        )

@pytest.fixture
def france():
    return Team(
        name='France',
        code='FRA',
        confederation='UEFA',
        ranking=1,
        host=False
        )

@pytest.fixture
def italy():
    return Team(
        name='Italy',
        code='ITA',
        confederation='UEFA',
        ranking=15,
        host=False
        )

@pytest.fixture
def jordan():
    return Team(
        name='Jordan',
        code='JOR',
        confederation='AFC',
        ranking=73,
        host=False
        )

@pytest.fixture
def usa():
    return Team(
        name='USA',
        code='USA',
        confederation='CONCACAF',
        ranking=16,
        host=True
    )



@pytest.fixture
def teams_j(argentina, austria, algeria, jordan):
    return [argentina, austria, algeria, jordan]


# preparing groups to be used in tests...
@pytest.fixture
def empty_group():
    return Group(
        name='A',
        teams=[]
    )

@pytest.fixture
def full_group(teams_j):
    return Group(
        name='J',
        teams=teams_j
    )