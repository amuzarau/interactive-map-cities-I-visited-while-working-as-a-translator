# Interactive Map — Cities I Visited While Working as a Translator

🌍 **Interactive world map** built with Python, Plotly & Streamlit  
This web app visualizes the cities I visited during my work as a translator. It combines an interactive geographical map and a clean, responsive table of visited cities.

✔ Highlights:
- Colored polygons for **visited countries**
- Interactive map with **city markers**
- Hover shows **city names**
- Mobile-friendly map layout
- Clean table with SVG country flags

---

## 📍 Live Demo

Visit the live interactive web app here:  
👉 https://interactive-map-cities-i-visited-while-working-as-a-translator.streamlit.app/

> 🔁 The app may take a few seconds to “wake up” if it has been idle.

---

## 🧠 What the App Shows

- A world map with highlighted countries where I have been  
- Black dots for visited cities  
- Hover labels with city name only  
- A responsive table listing all visited cities with flags

Example of table entries:

| # | City       | Country | Flag |
|---|------------|---------|------|
| 1 | Amsterdam  | Netherlands | 🇳🇱 |
| 2 | Prague     | Czech Republic | 🇨🇿 |
|…  | …          | …       | … |
|14 | Lodz       | Poland  | 🇵🇱 |
|15 | Kielce     | Poland  | 🇵🇱 |

---

## 🚀 How It Works

The project uses:

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Pandas** | Data handling |
| **Plotly** | Interactive map generation |
| **Streamlit** | UI & web deployment |
| **GeoJSON** | Country boundary data |

The map uses a GeoJSON world dataset and plots filled countries and city markers.  
The table displays cities and SVG flags for country representation.

---

## 🧩 Project Structure

interactive-map-cities-I-visited-while-working-as-a-translator/
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project overview (this file)
└── .gitignore # Git ignore rules

yaml
Копировать код

---

## 🔧 Setup & Installation

To run this project locally:

### 1. Clone the repository

```bash
git clone https://github.com/amuzarau/interactive-map-cities-I-visited-while-working-as-a-translator.git
cd interactive-map-cities-I-visited-while-working-as-a-translator
2. Create and activate a virtual environment
bash
Копировать код
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
Копировать код
pip install -r requirements.txt
4. Run the app
bash
Копировать код
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📦 Requirements
The main dependencies are:

text
Копировать код
streamlit
pandas
plotly
If you need to update dependencies, open requirements.txt.

📌 Notes
The map is designed to be mobile-friendly and responsive.

When deployed on Streamlit Community Cloud, the app may go to sleep when idle.

The app uses public GeoJSON data for country borders.

🧭 Contributing
Feel free to open issues or make pull requests.
Suggestions welcome for improvements like:

Adding filtering by country

Displaying routes between cities

Animation or timeline view of visits

📝 License
This project is open-source and available under the MIT License.

🙏 Acknowledgements
GeoJSON world data by Johan Sundström
https://github.com/johan/world.geo.json

Map rendering thanks to Plotly & Streamlit


