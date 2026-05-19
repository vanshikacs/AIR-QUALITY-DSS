# AirFlow Decision Support System

**Professional air quality exposure risk assessment and timing optimization tool**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)

---

## Overview

AirFlow DSS is a professional decision-support system that transforms raw environmental monitoring data into actionable insights for exposure risk management. Built with clean architecture principles, it demonstrates production-ready software engineering, applied analytics, and user-centered design.

### What It Does

- **Personalized Risk Assessment:** Calculates exposure scores combining environmental conditions with individual activity patterns
- **Trend Analysis:** Detects patterns and changes in air quality across searches using statistical methods
- **Time Optimization:** Identifies lower-risk time windows for outdoor activities
- **Data Quality Assessment:** Evaluates and communicates reliability of source data

### What It's Not

- Not a simple visualization dashboard
- Not an awareness/activism tool
- Not using black-box ML models
- Not making medical diagnoses

---

## System Architecture

```
┌─────────────────────────────────────────────┐
│         UI Layer (Streamlit)                │
│  - Page routing and rendering               │
│  - User interactions                        │
│  - Visualization components                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         Analysis Layer                      │
│  - ExposureAnalyzer                         │
│  - TrendAnalyzer                            │
│  - TimeWindowOptimizer                      │
│  - ProfileManager                           │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         Data Layer                          │
│  - AQIAPIClient                             │
│  - DataQualityAssessor                      │
│  - Data models (AQIData, UserProfile)       │
└─────────────────────────────────────────────┘
```

**Design Principles:**
- Separation of concerns across layers
- Single responsibility per module
- Type-safe data models
- Centralized state management
- Defensive error handling

---

## Project Structure

```
airflow-dss/
├── app.py                      # Clean entry point
├── requirements.txt            # Dependencies
├── .streamlit/config.toml     # Configuration
│
├── src/                        # Source code
│   ├── data/                   # DATA LAYER
│   │   ├── api_client.py      # API integration
│   │   ├── quality.py         # Quality assessment
│   │   └── models.py          # Data models
│   │
│   ├── analysis/               # ANALYSIS LAYER
│   │   ├── exposure.py        # Risk scoring
│   │   ├── trends.py          # Trend analysis
│   │   ├── optimization.py    # Time windows
│   │   └── profiles.py        # Profile management
│   │
│   ├── ui/                     # UI LAYER
│   │   ├── pages/             # Page modules
│   │   ├── components.py      # Reusable components
│   │   └── visualizations.py  # Charts/graphs
│   │
│   ├── utils/                  # UTILITIES
│   │   ├── constants.py       # Configuration
│   │   └── helpers.py         # Helper functions
│   │
│   └── state.py               # State management
│
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md
│   └── API.md
│
└── tests/                      # Unit tests
    ├── test_exposure.py
    └── test_trends.py
```

---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/airflow-dss.git
cd airflow-dss

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Configuration

Edit `.streamlit/config.toml` for theme customization.

---

## Usage

### Basic Flow

1. **Search Location:** Enter city name
2. **View AQI:** See current air quality and data quality assessment
3. **Analyze Exposure:** Calculate personalized risk score based on your profile
4. **Optimize Timing:** Identify lower-risk time windows
5. **Track Trends:** After 3+ searches, view statistical insights

### Profile Configuration

Profiles allow personalization based on:
- **Outdoor Hours:** Time spent outside daily (0-12 hours)
- **Activity Level:** Intensity of physical activity (low/moderate/high)
- **Sensitivity:** Vulnerability to pollution (normal/sensitive/respiratory)

Create multiple profiles for different scenarios (e.g., "Commuter", "Athlete", "Sensitive").

---

## Methodology

### Exposure Scoring

**Formula:**
```
Score = (AQI/100) × Hours × Activity_Mult × Sensitivity_Mult
Normalized to 0-100 scale
```

**Components:**
- **AQI Factor:** Environmental pollution level (capped at 5.0)
- **Hours:** Time spent outdoors
- **Activity Multiplier:** 1.0 (low), 1.3 (moderate), 1.6 (high)
- **Sensitivity Multiplier:** 1.0 (normal), 1.4 (sensitive), 1.7 (respiratory)

**Risk Levels:**
- 0-20: Low Risk
- 20-40: Moderate Risk
- 40-60: Elevated Risk
- 60-100: High Risk

### Trend Analysis

Uses lightweight statistical methods:
- **Direction Analysis:** Compares recent vs. historical averages (±20% threshold)
- **Volatility Measurement:** Standard deviation calculation
- **Extremes Detection:** Identifies peak and minimum values
- **Moving Averages:** 3-point smoothing for visualization

### Time Window Optimization

Pattern-based estimation using typical urban pollution cycles:
- **Early Morning (5-7 AM):** ~70% of current AQI
- **Post Rush-Hour (9-11 AM):** ~85% of current AQI
- **Late Evening (10 PM-12 AM):** ~80% of current AQI

**Note:** Based on typical patterns, not location-specific forecasts.

---

## Assumptions & Limitations

### Assumptions
- Linear relationship between AQI and health risk
- Activity level correlates with respiration rate
- Sensitivity factors based on epidemiological guidelines
- Continuous outdoor exposure during specified hours

### Limitations
- Does not account for individual medical history
- Indoor air quality not separately modeled
- Mask usage not factored into calculations
- Time windows based on patterns, not real-time forecasts
- Limited to available API data coverage

### Not a Substitute For
- Official environmental monitoring agencies
- Medical advice from healthcare professionals
- Emergency health services
- Local health authority guidelines

---

## Technical Details

### Technology Stack
- **Framework:** Streamlit 1.28+
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly
- **Mapping:** Folium
- **API:** WAQI (World Air Quality Index)
- **Language:** Python 3.8+

### Code Quality
- Type hints throughout
- Comprehensive docstrings
- Modular, testable design
- Defensive error handling
- Clean separation of concerns

### Data Sources
- **Provider:** World Air Quality Index (WAQI) Project
- **Coverage:** 12,000+ monitoring stations in 1,000+ cities
- **Update Frequency:** Varies by location (typically 1-6 hours)
- **Attribution:** Data © WAQI Project, EPA, local agencies

---

## Development

### Running Tests
```bash
pytest tests/
```

### Adding New Features

1. **Data Layer:** Add to `src/data/` if fetching/processing data
2. **Analysis Layer:** Add to `src/analysis/` for calculations
3. **UI Layer:** Add to `src/ui/pages/` for new pages
4. **Update:** Modify `app.py` routing if adding pages

### Code Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions focused (single responsibility)

---

## Why This Structure?

### For Internships & Portfolios

**Software Engineering:**
- Clean architecture (layered design)
- Proper module organization
- Type-safe data models
- Testable components

**Applied Analytics:**
- Transparent calculations
- Statistical methods
- Data quality awareness
- Practical utility

**Product Thinking:**
- User-centered design
- Decision-focused features
- Clear communication
- Handles real-world complexity

---

## License

MIT License - See LICENSE file

---

## Author

[Your Name]  
[Your Email]  
[GitHub](https://github.com/yourusername)  
[LinkedIn](https://linkedin.com/in/yourprofile)

---

## Acknowledgments

- WAQI Project for air quality data API
- Streamlit for the framework
- Open source community

---

**Built to demonstrate professional software engineering and applied analytics**

*Last updated: December 2024*