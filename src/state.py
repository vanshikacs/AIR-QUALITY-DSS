"""
Centralized session state management.
"""

import streamlit as st
from typing import Dict, List, Optional
from datetime import datetime
from .data.models import AQIData, UserProfile, SearchHistoryEntry
from .analysis.profiles import ProfileManager
from .utils.constants import DEFAULT_PROFILE


class SessionState:
    """
    Centralized session state manager.
    Provides clean interface to Streamlit session_state.
    """
    
    @staticmethod
    def initialize():
        """Initialize all session state variables"""
        defaults = {
            'initialized': True,
            'aqi_data': None,
            'location': None,
            'search_history': [],
            'current_page': '🏠 Home',
            'last_update': None,
            'exposure_score': None,
            'time_windows': None,
            'profile_manager': ProfileManager(),
            'current_profile_name': 'Default',
            'show_save_dialog': False,
            'last_search_input': ''
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    @staticmethod
    def get_aqi_data() -> Optional[AQIData]:
        """Get current AQI data"""
        return st.session_state.get('aqi_data')
    
    @staticmethod
    def set_aqi_data(data: AQIData):
        """Set current AQI data"""
        st.session_state.aqi_data = data
        st.session_state.last_update = datetime.now()
    
    @staticmethod
    def add_to_history(city: str, aqi: int):
        """Add search to history"""
        entry = SearchHistoryEntry(city=city, aqi=aqi, timestamp=datetime.now())
        st.session_state.search_history.append(entry)
        
        # Limit size
        from .utils.constants import MAX_SEARCH_HISTORY
        if len(st.session_state.search_history) > MAX_SEARCH_HISTORY:
            st.session_state.search_history.pop(0)
    
    @staticmethod
    def get_current_profile() -> UserProfile:
        """Get active profile"""
        manager: ProfileManager = st.session_state.profile_manager
        return manager.load_profile(st.session_state.current_profile_name)
    
    @staticmethod
    def navigate_to(page: str):
        """Navigate to page"""
        st.session_state.current_page = page
