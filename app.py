import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import urllib.request

st.set_page_config(page_title="Visited Cities Map", layout="wide")

st.title("🌍 Cities I visited while working as a translator")


# ---------------------------
# CITY DATA
# ---------------------------
data = {
    "city": [
        "Amsterdam",
        "Prague",
        "Brno",
        "Vienna",
        "Milan",
        "Venice",
        "Verona",
        "Monza",
        "Sant'Agata Bolognese",
        "Trier",
        "Hannover",
        "Frankfurt am Main",
        "Warsaw",
        "Moscow",
        "Saint Petersburg",
        "Beijing",
        "Guangzhou",
    ],
    "country": [
        "Netherlands",
        "Czech Republic",
        "Czech Republic",
        "Austria",
        "Italy",
        "Italy",
        "Italy",
        "Italy",
        "Italy",
        "Germany",
        "Germany",
        "Germany",
        "Poland",
        "Russia",
        "Russia",
        "China",
        "China",
    ],
    "iso": [
        "nl",
        "cz",
        "cz",
        "at",
        "it",
        "it",
        "it",
        "it",
        "it",
        "de",
        "de",
        "de",
        "pl",
        "ru",
        "ru",
        "cn",
        "cn",
    ],
    "lat": [
        52.3676,
        50.0755,
        49.1951,
        48.2082,
        45.4642,
        45.4408,
        45.4384,
        45.5845,
        44.6643,
        49.7499,
        52.3759,
        50.1109,
        52.2297,
        55.7558,
        59.9311,
        39.9042,
        23.1291,
    ],
    "lon": [
        4.9041,
        14.4378,
        16.6068,
        16.3738,
        9.1900,
        12.3155,
        10.9930,
        9.2744,
        11.1920,
        6.6340,
        9.7320,
        8.6821,
        21.0122,
        37.6176,
        30.3609,
        116.4074,
        113.2644,
    ],
}

df = pd.DataFrame(data)
visited_countries = df["country"].unique().tolist()

# ---------------------------
# LOAD WORLD GEOJSON
# ---------------------------
url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
with urllib.request.urlopen(url) as response:
    world_geo = json.load(response)

# ---------------------------
# COLORS PER COUNTRY
# ---------------------------
color_map = {
    "Netherlands": "rgba(255,140,0,0.35)",
    "Czech Republic": "rgba(30,144,255,0.35)",
    "Austria": "rgba(255,99,132,0.35)",
    "Italy": "rgba(50,205,50,0.35)",
    "Germany": "rgba(138,43,226,0.35)",
    "Poland": "rgba(255,215,0,0.35)",
    "Russia": "rgba(70,130,180,0.25)",
    "China": "rgba(255,0,0,0.25)",
}

solid_color_map = {
    country: color_map[country].replace("0.35", "1").replace("0.25", "1")
    for country in visited_countries
}

# Emoji just for legend (clean)
flag_emoji = {
    "nl": "🇳🇱",
    "cz": "🇨🇿",
    "at": "🇦🇹",
    "it": "🇮🇹",
    "de": "🇩🇪",
    "pl": "🇵🇱",
    "ru": "🇷🇺",
    "cn": "🇨🇳",
}

df["emoji"] = df["iso"].map(flag_emoji)


# SVG flags for chart
def flag_svg(iso):
    return f'<img src="https://flagcdn.com/{iso}.svg" width="32">'


fig = go.Figure()

# ---------------------------
# DRAW VISITED COUNTRIES (NO TEXT)
# ---------------------------
for feature in world_geo["features"]:
    name = feature["properties"]["name"]

    if name in visited_countries:
        geom = feature["geometry"]

        if geom["type"] == "Polygon":
            lon, lat = zip(*geom["coordinates"][0])
            fig.add_trace(
                go.Scattergeo(
                    lon=lon,
                    lat=lat,
                    fill="toself",
                    fillcolor=color_map[name],
                    line=dict(color="black", width=1.2),
                    mode="lines",
                    name="",
                    showlegend=False,
                )
            )

        elif geom["type"] == "MultiPolygon":
            for poly in geom["coordinates"]:
                lon, lat = zip(*poly[0])
                fig.add_trace(
                    go.Scattergeo(
                        lon=lon,
                        lat=lat,
                        fill="toself",
                        fillcolor=color_map[name],
                        line=dict(color="black", width=1.2),
                        mode="lines",
                        name="",
                        showlegend=False,
                    )
                )

# ---------------------------
# CITY DOTS — ONLY CITY NAME ON HOVER
# ---------------------------
fig.add_trace(
    go.Scattergeo(
        lon=df["lon"],
        lat=df["lat"],
        mode="markers",
        marker=dict(size=6, color="black"),
        text=df["city"],
        hovertemplate="%{text}<extra></extra>",
        name="",
        showlegend=False,
    )
)

# ---------------------------
# LEGEND: COLOR CIRCLE + COUNTRY NAME ONLY
# ---------------------------
for country in visited_countries:
    iso = df[df["country"] == country]["iso"].iloc[0]
    fig.add_trace(
        go.Scattergeo(
            lon=[None],
            lat=[None],
            mode="markers",
            marker=dict(size=14, color=solid_color_map[country]),
            name=country,
        )
    )

# ---------------------------
# MAP SETTINGS (FULL WORLD ZOOM)
# ---------------------------
fig.update_layout(
    height=720,
    margin={"r": 0, "t": 20, "l": 0, "b": 0},
    geo=dict(
        projection_type="natural earth",
        showcountries=True,
        countrycolor="black",
        showland=True,
        landcolor="rgb(240,240,240)",
        # FULL WORLD VIEW ENABLED (no limits)
    ),
    legend_title_text="Visited Countries",
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# TABLE WITH SVG FLAGS
# ---------------------------
st.subheader("📌 List of visited cities")

df["flag"] = df["iso"].apply(flag_svg)

table = df[["city", "country", "flag"]].copy()
table.columns = ["City", "Country", "Flag"]
table.index = table.index + 1
table.index.name = "#"

html = table.to_html(escape=False)
st.markdown(html, unsafe_allow_html=True)
