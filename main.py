#  ------ mini projects starts here --------
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
# print(soup.title)
# print(soup.prettify())

#  ------ find 100 movie title --------
movie_titles = soup.find_all(name="h3", class_ = "title")

# for title in movie_titles:
#     title_text.append(title.get_text())
# ------------ list comprehension -----------
title_text = [title.get_text() for title in movie_titles]
title_text.reverse()
# print(title_text)

# ---------- add them into a txt file ----------
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in title_text:
        # file.write(f"{movie.split()}\n")
        clean_name = " ".join(movie.split()[1:])
        file.write(f"{clean_name}\n")



