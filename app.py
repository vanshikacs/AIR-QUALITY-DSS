"""Main Streamlit launcher for AirFlow DSS.

This file connects the complete project architecture:
- src/utils/constants.py for API/config values
- src/data/api_client.py for WAQI fetching
- src/data/models.py for typed AQI/profile/history objects
- src/data/quality.py for data quality scoring
- src/analysis/* for exposure, timing, trends, and profiles
- src/ui/pages/* for all Streamlit pages
- src/ui/visualizations.py for Plotly charts
- index.html as an optional standalone showcase page
"""

from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html

from src.analysis.profiles import ProfileManager
from src.data.api_client import AQIAPIClient
from src.data.models import UserProfile
from src.state import SessionState
from src.ui.components import render_status_card
from src.ui.pages.exposure import render_exposure_page
from src.ui.pages.home import render_home_page
from src.ui.pages.optimization import render_optimization_page
from src.ui.pages.system_info import render_system_info_page
from src.ui.pages.trends import render_trends_page
from src.utils.constants import API_TOKEN

st.set_page_config(
    page_title="AirFlow DSS",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------- APP BOOT ----------
SessionState.initialize()

PAGES = [
    "🏠 Home",
    "📊 Exposure Analysis",
    "⏰ Time Optimization",
    "📈 Trend Intelligence",
    "✨ HTML Showcase",
    "🔬 System Information",
]


# ---------- DATA SEARCH ----------
def handle_search(location: str) -> bool:
    """Fetch AQI data through src/data/api_client.py and store it in session state."""
    location = (location or "").strip()

    if not location:
        st.warning("Please enter a city/location first.")
        return False

    try:
        client = AQIAPIClient(token=API_TOKEN)
        data = client.fetch_aqi(location)

        if data is None:
            st.error("City not found, API token invalid, or WAQI has no station for this location.")
            return False

        SessionState.set_aqi_data(data)
        SessionState.add_to_history(data.city_name, data.aqi)
        return True

    except Exception as exc:
        st.error(f"Could not fetch AQI data: {exc}")
        return False


# ---------- SIDEBAR ----------
st.sidebar.title("🌿 AirFlow")
st.sidebar.caption("Decision Support System")

current_page = st.sidebar.radio(
    "Navigate",
    PAGES,
    index=PAGES.index(st.session_state.current_page)
    if st.session_state.current_page in PAGES
    else 0,
)
st.session_state.current_page = current_page

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Exposure Profile")

outdoor_hours = st.sidebar.slider(
    "Outdoor hours/day",
    min_value=0.0,
    max_value=12.0,
    value=float(SessionState.get_current_profile().outdoor_hours),
    step=0.5,
)
activity_level = st.sidebar.selectbox(
    "Activity level",
    ["low", "moderate", "high"],
    index=["low", "moderate", "high"].index(SessionState.get_current_profile().activity_level),
    help="Low = walking/sedentary, moderate = cycling/jogging, high = intense exercise",
)
sensitivity = st.sidebar.selectbox(
    "Sensitivity",
    ["normal", "sensitive", "respiratory"],
    index=["normal", "sensitive", "respiratory"].index(SessionState.get_current_profile().sensitivity),
    help="Sensitive = children/elderly; respiratory = asthma/COPD/heart conditions",
)

# Keep profile system connected to UI controls.
profile_manager: ProfileManager = st.session_state.profile_manager
profile_manager.profiles["Current"] = UserProfile(
    name="Current",
    outdoor_hours=outdoor_hours,
    activity_level=activity_level,
    sensitivity=sensitivity,
)
st.session_state.current_profile_name = "Current"

st.sidebar.markdown("---")

if st.session_state.aqi_data:
    render_status_card(st.session_state.aqi_data)
else:
    st.sidebar.info("Search a city on Home to unlock analysis pages.")

st.sidebar.markdown("---")
st.sidebar.caption("Search 3+ cities/locations to unlock trend intelligence.")


# ---------- PAGE ROUTING ----------
if st.session_state.current_page == "🏠 Home":
    render_home_page(handle_search)

elif st.session_state.current_page == "📊 Exposure Analysis":
    render_exposure_page()

elif st.session_state.current_page == "⏰ Time Optimization":
    render_optimization_page()

elif st.session_state.current_page == "📈 Trend Intelligence":
    render_trends_page()

elif st.session_state.current_page == "✨ HTML Showcase":
    st.title("✨ AirFlow HTML Showcase")
    st.caption("This renders your original index.html design inside Streamlit.")

    index_path = Path(__file__).parent / "index.html"
    if index_path.exists():
        ui_html = index_path.read_text(encoding="utf-8")
        html(ui_html, height=900, scrolling=True)
    else:
        st.error("index.html was not found in the project root.")

elif st.session_state.current_page == "🔬 System Information":
    render_system_info_page()
