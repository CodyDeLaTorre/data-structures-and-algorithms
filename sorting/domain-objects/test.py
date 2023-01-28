import pytest
from movies import sort_movie_by_yr
from movies import sort_movie_by_name

# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]


def test_sort_by_yr(movies):
  result = sort_movie_by_yr(movies)
  assert result == ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

def test_sort_by_name(movies):
  result = sort_movie_by_name(movies)
  assert result == ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]


@pytest.fixture
def movies():
  return [
  {
    "title": "Beetlejuice",
    "year": 1988,
    "genres": ["Comedy", "Fantasy"],
  },
  {
    "title": "The Cotton Club",
    "year": 1984,
    "genres": ["Crime", "Drama", "Music"],
  },
  {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Crocodile Dundee",
    "year": 1986,

    "genres": ["Adventure", "Comedy"],
  },
  {
    "title": "Valkyrie",
    "year": 2008,
    "genres": ["Drama", "History", "Thriller"],
  },
  {
    "title": "Ratatouille",
    "year": 2007,
    "genres": ["Animation", "Comedy", "Family"],
  },
  {
    "title": "City of God",
    "year": 2002,

    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Memento",
    "year": 2000,

    "genres": ["Mystery", "Thriller"],
  },
  {
    "title": "The Intouchables",
    "year": 2011,

    "genres": ["Biography", "Comedy", "Drama"],
  },
  {
    "title": "Stardust",
    "year": 2007,
    "genres": ["Adventure", "Family", "Fantasy"],
  },
]
