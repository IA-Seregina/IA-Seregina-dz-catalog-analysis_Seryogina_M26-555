import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    ratings = []
    for n in movies:
        ratings.append(n["rating"])
    avg_rating = round((sum(ratings)/len(ratings)), 1)

    return avg_rating        

def catalog_age_stats(movies, current_year=2026):
    years = []
    for n in movies:
        years.append(current_year - n["year"])
    oldest = max(years)
    youngest = min(years)
    avg = math.ceil((youngest+oldest)/2)
    
    return (oldest, youngest, avg)

def duration_in_hours(minutes):
    h = minutes//60
    m = minutes%60
    time = f"{h}ч {m}м"
                                                                                                                                                                                             
    return time

def rating_tier(rating):
    match rating:
        case x if 7<=x<=8.9:
            return "шедевр" if x >= 9 else "хорошо"
        case x if 5<=x<=6.9:
            return "средне"
        case _:
            return "слабо"
        

def decade_label(year):
    match year:
        case year if year>2020:
            return "новые"
        case year if 2015<=year<=2020:
            return "недавние"
        case _:
            return "старые"

# Stage 3

for n in movies:
    if "comedy" in n["genres"]:
        continue
    else:
        print(n["title"])

i = 0

while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i])
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    c = 0
    for n in movies:
        if n["duration_min"] > 120:
            c+=1

    return c

# Stage 4

def normalize_title(title):
    words = []
    for word in title.split():
        word = word[0].upper() + word[1:]
        words.append(word)
    title = " ".join(words)

    return title

def make_slug(title):
    words = []
    for word in title.split():
        word = word.lower()
        words.append(word)
    slug = "-".join(words)

    return slug

def format_report_line(movie):
    return f'"{movie["title"]}" ({movie["year"]}) - {movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, жанры: {", ".join(sorted(movie["genres"]))}'


# Stage 5

def titles_sorted_by_rating(movies):
    ordered = sorted(movies, key = lambda item: item["rating"], reverse=True)
    titles = []
    for n in ordered:
        titles.append(n["title"])

    return titles

def top_n_by_rating(movies, n=3):
    titles = []
    for m in movies:
        pair = (m["title"], m["rating"])
        titles.append(pair)
    ordered = sorted(titles, key = lambda item: item[1], reverse=True)
    answer = ordered[0:3]

    return answer

# Stage 6

def count_by_genre(movies):
    genres = {}
    for n in movies:
        for genre in n["genres"]:
            genres[genre] = genres.get(genre, 0) + 1

    return genres

def actor_filmography(movies):
    actors = {}
    for n in movies:
        for actor in n["actors"]:
            if actor not in actors:
                actors[actor] = []
            actors[actor].append(n["title"])

    return actors

above_average = {
    n["title"]: n["rating"]
    for n in movies
    if n["rating"] > average_rating(movies)
}
