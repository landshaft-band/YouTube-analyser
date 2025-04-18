# YouTube Recommendation Data Analyzer

This project is designed to collect, cluster, and categorize YouTube recommendations from a user's homepage. It includes tools for scraping video data, vectorizing titles, and grouping videos by semantic similarity using OpenAI models.

---

## 📌 Features

- **Parser (Selenium-based)** — collects YouTube homepage video recommendations using a custom Chrome user profile.
- **Structured CSV Export** — stores metadata like video title, URL, channel name, thumbnail, and duration.
- **Clustering** — groups videos based on semantic similarity of titles.
- **Category Classification** — uses OpenAI GPT models to generate thematic categories for each video.

---

## 🗂️ Folder Structure


---

## 🧰 Prerequisites

- Python 3.9+
- Google Chrome installed
- ChromeDriver (auto-installed)
- OpenAI API key
- VPN (if required by your region)

---



options.add_argument(r"user-data-dir=C:\Users\<your_username>\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"profile-directory=Profile 11")


🚀 Usage
1. Run the Parser
This script will collect up to 500 videos from your homepage:

bash
Копировать
Редактировать
python parser.py
2. Analyze and Cluster (Notebook)
Open analyze_clusters.ipynb

Run all cells:

Clean data

Generate embeddings

Cluster similar titles

Use GPT for category labeling

3. Review Output
Final dataset will be saved as:

Копировать
Редактировать
youtube_data_with_categories.csv
📊 Example Output

Title	Channel	Duration	Category
How to Learn Python in 2024	Python Hub	12:34	Programming
The Rise of AI in Creativity	AI Today	08:21	Artificial Intel
🔐 Notes
Uses your real YouTube profile for accurate recommendations.

Ensure you're logged in before running the script.

VPN may be required for OpenAI access in restricted regions.
