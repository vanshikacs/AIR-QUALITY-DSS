
"""Home page UI"""

import streamlit as st
import folium
from streamlit_folium import folium_static
from ...data.quality import DataQualityAssessor
from ...ui.components import render_aqi_card, get_aqi_category


def render_home_page(handle_search_fn):
    """Render home page"""
    st.title("🌿 AirFlow Decision Support System")
    st.markdown("Transform environmental data into actionable insights")
    st.markdown("---")
    
    # Search
    col1, col2 = st.columns([4, 1])
    with col1:
        search_input = st.text_input("Location", placeholder="Enter city name", 
                                      key="search_input", label_visibility="collapsed")
    with col2:
        search_clicked = st.button("🔍 Search", use_container_width=True, type="primary")
    
    if search_clicked or (search_input and st.session_state.get('last_search_input') != search_input):
        if handle_search_fn(search_input):
            st.session_state.last_search_input = search_input
            st.rerun()
    
    st.markdown("---")
    
    # Display results
    if st.session_state.aqi_data:
        data = st.session_state.aqi_data
        
        col1, col2 = st.columns([2, 1])
        with col1:
            render_aqi_card(data)
        with col2:
            st.markdown("#### Data Quality")
            assessor = DataQualityAssessor(data)
            st.info(assessor.get_summary())
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("### Quick Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Analyze Exposure", use_container_width=True, type="primary"):
                st.session_state.current_page = '📊 Exposure Analysis'
                st.rerun()
        
        with col2:
            if st.button("⏰ Find Times", use_container_width=True, type="primary"):
                st.session_state.current_page = '⏰ Time Optimization'
                st.rerun()
        
        with col3:
            if len(st.session_state.search_history) >= 3:
                if st.button("📈 View Trends", use_container_width=True, type="primary"):
                    st.session_state.current_page = '📈 Trend Intelligence'
                    st.rerun()
            else:
                st.button("📈 Trends", disabled=True, help="Search 3+ locations")
        
        st.markdown("---")
        
        # Map
        st.markdown("### Location Map")
        m = folium.Map(location=[data.latitude, data.longitude], zoom_start=12)
        cat = get_aqi_category(data.aqi)
        folium.Marker(
            [data.latitude, data.longitude],
            popup=f"<b>{data.city_name}</b><br>AQI: {data.aqi}",
            icon=folium.Icon(color="green" if data.aqi<=100 else "orange" if data.aqi<=200 else "red")
        ).add_to(m)
        folium_static(m, width=1200, height=450)
    else:
        st.info("👋 Enter a location to begin analysis")

