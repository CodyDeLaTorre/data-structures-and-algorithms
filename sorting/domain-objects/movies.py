movies = [
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



def sort_movie_by_yr(lst):
  new_lst = sorted(lst, key=lambda movie: movie["year"])
  new_lst.reverse()
  titles = list(map(lambda movie: movie['title'], new_lst))
  return titles


def sort_movie_by_name(lst):
  def format_title(title):
    ignore_words = ["A", "An", "The"]
    title_parts = title.split()
    if title_parts[0] in ignore_words:
        title_parts = title_parts[1:]
    return " ".join(title_parts)
  new_lst = sorted(lst, key=lambda movie: format_title(movie["title"]))
  titles = list(map(lambda movie: movie['title'], new_lst))
  return titles

# print(sort_movie_by_yr(movies))
print(sort_movie_by_name(movies))
