# 🎬 100 Movies to Watch Web Scraper

This is a mini Python project that scrapes the **"100 Best Movies"** list from [Empire Online](https://www.empireonline.com/movies/features/best-movies-2/) (via the [Wayback Machine snapshot](https://web.archive.org/)), extracts all movie titles, and saves them into a text file.

---

## 📂 Project Structure
- ├── main.py # Main scraping script
- ├── movies.txt # Output file with the top 100 movies
- └── README.md # Project documentation
---



---

## 🛠️ Technology Stack
- **Python 3** → Core programming language  
- **Requests** → Fetching webpage content  
- **BeautifulSoup4** → Parsing and extracting HTML data  
- **File Handling (I/O)** → Writing cleaned movie titles into a `.txt` file  

---

## 🚀 Features
- Scrapes **100 movie titles** from an archived webpage.
- Cleans movie titles (removes numbering like `100)`).
- Reverses the order so the **#1 movie appears at the top**.
- Saves the results into a UTF-8 encoded `movies.txt` file.

---

## 📦 Requirements
Make sure you have Python installed, then install dependencies:

```bash
pip install requests beautifulsoup4


