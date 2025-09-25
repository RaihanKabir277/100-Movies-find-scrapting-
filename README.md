# 🎬 100 Movies to Watch Web Scraper

This is a mini Python project that scrapes the **"100 Best Movies"** list from [Empire Online](https://www.empireonline.com/movies/features/best-movies-2/) (via the [Wayback Machine snapshot](https://web.archive.org/)), extracts all movie titles, and saves them into a text file.

---

## 📂 Project Structure
- ├── main.py # Main scraping script
- ├── movies.txt # Output file with the top 100 movies
- └── README.md # Project documentation
---


---

## 🚀 Features
- Uses **BeautifulSoup** and **Requests** to scrape data.
- Extracts all **100 movie titles** from the archived webpage.
- Cleans the titles (removes numbering like `100)`).
- Reverses the list so the #1 movie appears at the top.
- Saves the final list into a `movies.txt` file (UTF-8 encoded).

---

## 🛠️ Requirements
Make sure you have Python installed, then install dependencies:

```bash
pip install requests beautifulsoup4

