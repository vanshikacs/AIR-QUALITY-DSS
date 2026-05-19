"""
Application constants and configuration.
"""

# API Configuration
import streamlit as st
import os

API_TOKEN = st.secrets.get("WAQI_API_TOKEN", os.getenv("WAQI_API_TOKEN", ""))
API_BASE_URL = "https://api.waqi.info/feed"
API_TIMEOUT = 10

# Exposure Scoring Weights
EXPOSURE_WEIGHTS = {
    'activity_multipliers': {
        'low': 1.0,      # Walking, sedentary
        'moderate': 1.3, # Cycling, jogging
        'high': 1.6      # Running, intense exercise
    },
    'sensitivity_multipliers': {
        'normal': 1.0,
        'sensitive': 1.4,    # Children, elderly
        'respiratory': 1.7   # Asthma, COPD, heart conditions
    }
}

# AQI Category Thresholds
AQI_THRESHOLDS = {
    'good': (0, 50),
    'satisfactory': (51, 100),
    'moderate': (101, 200),
    'poor': (201, 300),
    'very_poor': (301, 400),
    'severe': (401, 500)
}

# AQI Category Metadata
AQI_CATEGORIES = {
    'good': {"label": "Good", "emoji": "😃", "color": "#8bac85"},
    'satisfactory': {"label": "Satisfactory", "emoji": "🙂", "color": "#a8c9a2"},
    'moderate': {"label": "Moderate", "emoji": "😐", "color": "#f5d76e"},
    'poor': {"label": "Poor", "emoji": "😷", "color": "#f29e4c"},
    'very_poor': {"label": "Very Poor", "emoji": "🤢", "color": "#d9534f"},
    'severe': {"label": "Severe", "emoji": "🛑", "color": "#8b0000"}
}

# Session Configuration
MAX_SEARCH_HISTORY = 20
DEFAULT_PROFILE = {
    'outdoor_hours': 2.0,
    'activity_level': 'moderate',
    'sensitivity': 'normal'
}

# Time Window Patterns (typical urban pollution cycles)
TIME_WINDOW_PATTERNS = {
    'high_pollution': {
        'threshold': 150,
        'windows': [
            {'time': '5-7 AM', 'factor': 0.7, 'reason': 'Pre-traffic hours'},
            {'time': '10 PM-12 AM', 'factor': 0.8, 'reason': 'Reduced activity'}
        ]
    },
    'moderate_pollution': {
        'threshold': 100,
        'windows': [
            {'time': '9-11 AM', 'factor': 0.85, 'reason': 'Post rush-hour'},
            {'time': '3-5 PM', 'factor': 0.9, 'reason': 'Afternoon period'}
        ]
    },
    'low_pollution': {
        'threshold': 0,
        'windows': [
            {'time': 'Any time', 'factor': 1.0, 'reason': 'Air quality acceptable'}
        ]
    }
}
