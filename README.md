# 🌿 Air Quality DSS

> A professional air-quality decision support system that transforms real-time AQI data into personalized exposure insights, safer outdoor timing recommendations, and trend intelligence.

<p align="center">
  <a href="https://airflowdss.streamlit.app/"><strong>🚀 Live Demo: airflowdss.streamlit.app</strong></a>
</p>

<p align="center">
  <a href="https://airflowdss.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live App">
  </a>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Visualization-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
</p>

---

## Overview

**Air Quality DSS** is a decision-support application for air-quality awareness, exposure risk assessment, and safer activity planning. Instead of only displaying raw AQI values, the system interprets environmental data through a user-centered lens by combining air quality, outdoor duration, activity intensity, and sensitivity profile.

The goal is to make air-quality information more practical, explainable, and actionable for everyday decisions.

---

## Key Features

### Personalized Exposure Risk Assessment
Calculates an exposure score by combining AQI level with user-specific factors such as outdoor hours, activity level, and pollution sensitivity.

### Time Window Optimization
Suggests lower-risk outdoor time windows based on typical urban pollution patterns and current AQI severity.

### Trend Intelligence
Tracks searched locations and identifies patterns such as rising, falling, stable, or volatile AQI behavior after multiple searches.

### Data Quality Assessment
Evaluates the reliability, freshness, and completeness of available AQI data so users understand how confident they should be in the result.

### Multi-Page Streamlit Interface
Includes dedicated pages for home search, exposure analysis, time optimization, trend intelligence, HTML showcase, and system information.

### Clean Modular Architecture
Built using a layered structure with separate data, analysis, UI, utility, and state-management modules.

---

## Live Application

The deployed version is available here:

**🔗 [https://airflowdss.streamlit.app/](https://airflowdss.streamlit.app/)**

---

## System Architecture

```text
┌─────────────────────────────────────────────┐
│              UI Layer                       │
│  Streamlit pages, reusable components,      │
│  visualizations, navigation, interactions   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Analysis Layer                    │
│  Exposure scoring, trend analysis,          │
│  timing optimization, profile logic         │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│              Data Layer                     │
│  WAQI API client, data models,              │
│  quality assessment, response handling      │
└─────────────────────────────────────────────┘
```

---

## Project Structure

```text
AIR-QUALITY-DSS/
├── app.py                         # Main Streamlit entry point and page router
├── index.html                     # HTML showcase interface
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Files excluded from GitHub
│
├── .streamlit/
│   └── config.toml                # Streamlit theme/configuration
│
├── src/
│   ├── data/
│   │   ├── api_client.py          # WAQI API integration
│   │   ├── models.py              # AQI and profile data models
│   │   └── quality.py             # Data quality assessment
│   │
│   ├── analysis/
│   │   ├── exposure.py            # Exposure risk scoring
│   │   ├── optimization.py        # Outdoor timing recommendations
│   │   ├── profiles.py            # User profile logic
│   │   └── trends.py              # Trend intelligence
│   │
│   ├── ui/
│   │   ├── pages/                 # Individual Streamlit pages
│   │   ├── components.py          # Reusable UI components
│   │   └── visualizations.py      # Plotly charts and graphs
│   │
│   ├── utils/
│   │   ├── constants.py           # Central configuration and thresholds
│   │   └── helpers.py             # Helper functions
│   │
│   └── state.py                   # Streamlit session-state management
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── API.md
│
└── tests/
    ├── test_exposure.py
    └── test_trends.py
```

---

## Technology Stack

| Area | Tools |
|---|---|
| Frontend/App Framework | Streamlit |
| Language | Python |
| Data Fetching | Requests |
| Data Processing | Pandas, NumPy |
| Visualizations | Plotly, Folium |
| API Source | World Air Quality Index API |
| Deployment | Streamlit Community Cloud |

---

## Installation and Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/vanshikacs/AIR-QUALITY-DSS.git
cd AIR-QUALITY-DSS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your WAQI API token locally

Create a file:

```text
.streamlit/secrets.toml
```

Add:

```toml
WAQI_API_TOKEN = "your_waqi_api_token_here"
```

> Do not commit `secrets.toml` to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local app at:

```text
http://localhost:8501
```

---

## Deployment

This project can be deployed on **Streamlit Community Cloud**.

### Streamlit Cloud settings

```text
Repository: vanshikacs/AIR-QUALITY-DSS
Branch: main
Main file path: app.py
```

### Add secrets in Streamlit Cloud

Go to:

```text
Manage app → Settings → Secrets
```

Paste:

```toml
WAQI_API_TOKEN = "your_waqi_api_token_here"
```

Save and reboot the app.

---

## Usage Flow

1. Open the live app or run it locally.
2. Go to the **Home** page.
3. Search for a city such as `delhi`, `lucknow`, `mumbai`, or `kanpur`.
4. Review current AQI and data quality.
5. Configure your exposure profile from the sidebar.
6. Open **Exposure Analysis** to view personalized risk.
7. Open **Time Optimization** to identify safer outdoor windows.
8. Search 3 or more locations to unlock **Trend Intelligence**.

---

## Methodology

### Exposure Score

```text
Exposure Score = (AQI / 100) × Outdoor Hours × Activity Multiplier × Sensitivity Multiplier
```

The final score is normalized to a 0–100 scale for easier interpretation.

### Activity Multipliers

| Activity Level | Multiplier |
|---|---:|
| Low | 1.0 |
| Moderate | 1.3 |
| High | 1.6 |

### Sensitivity Multipliers

| Sensitivity Type | Multiplier |
|---|---:|
| Normal | 1.0 |
| Sensitive | 1.4 |
| Respiratory | 1.7 |

### Risk Levels

| Score Range | Interpretation |
|---|---|
| 0–20 | Low Risk |
| 20–40 | Moderate Risk |
| 40–60 | Elevated Risk |
| 60–100 | High Risk |

---

## Data Quality Logic

The system considers:

- API response availability
- AQI value validity
- Pollutant data completeness
- Station metadata availability
- Data recency where available

This helps communicate whether an AQI result should be treated as highly reliable or interpreted with caution.

---

## Assumptions and Limitations

Air Quality DSS is designed as a decision-support and educational tool. It does not replace official environmental agencies, local public-health advisories, or medical advice.

Current limitations include:

- Indoor air quality is not modeled separately.
- Mask usage is not included in exposure calculations.
- Time-window suggestions are pattern-based, not real-time forecasts.
- API coverage depends on available WAQI monitoring stations.
- Individual medical history is not used in the model.

---

## Code Quality Highlights

- Layered architecture
- Modular and reusable components
- Type-safe data models
- Centralized constants and configuration
- Session-state management
- Defensive error handling
- Transparent calculations
- Portfolio-friendly documentation

---

## Why This Project Matters

Air quality affects health, productivity, mobility, and daily planning. Most dashboards show numbers, but users often need answers to practical questions:

- Is it safe to go outside right now?
- How risky is outdoor activity for me?
- What time would be better for a walk or commute?
- Is air quality improving or worsening?
- How reliable is this AQI reading?

Air Quality DSS focuses on turning environmental data into clear, explainable decisions.

---

## Future Improvements

- 24–72 hour AQI forecasting
- Satellite-based pollution layer integration
- Personalized health recommendation engine
- Historical city-wise AQI dashboard
- Push alerts for severe AQI conditions
- More granular station selection
- Mobile-first UI enhancements
- Exportable reports for analysis

---

## License

This project is released under the MIT License.

---

## Author

**Vanshika Saxena**  
B.Tech Computer Science Engineering  
GitHub: [@vanshikacs](https://github.com/vanshikacs)

---

## Acknowledgments

- World Air Quality Index Project for AQI data access
- Streamlit for rapid interactive app development
- Open-source Python ecosystem for analytics and visualization tools

---

<p align="center">
  <strong>Built with clean architecture, applied analytics, and user-centered environmental decision support.</strong>
</p>
