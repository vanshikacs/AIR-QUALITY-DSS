"""
Reusable UI components.
"""

import streamlit as st
from ..data.models import AQIData
from ..utils.constants import AQI_THRESHOLDS, AQI_CATEGORIES


def get_aqi_category(aqi: float) -> dict:
    """Get AQI category metadata"""
    for key, (min_val, max_val) in AQI_THRESHOLDS.items():
        if min_val <= aqi <= max_val:
            return AQI_CATEGORIES[key]
    return AQI_CATEGORIES['severe']


def render_aqi_card(data: AQIData):
    """Render AQI display card"""
    cat = get_aqi_category(data.aqi)
    
    st.markdown(f"""
    <div style='background: white; padding: 40px; border-radius: 12px; 
         box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-left: 6px solid {cat["color"]};'>
        <div style='font-size: 1rem; color: #666; margin-bottom: 10px;'>📍 {data.city_name}</div>
        <div style='font-size: 4.5rem; font-weight: 900; color: {cat["color"]}; line-height: 1;'>{data.aqi}</div>
        <div style='font-size: 1.5rem; font-weight: 600; color: {cat["color"]}; margin-top: 10px;'>
            {cat["emoji"]} {cat["label"]}
        </div>
        <div style='margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;'>
            <small style='color: #888;'>Dominant: <strong>{data.dominant_pollutant or 'N/A'}</strong></small>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_status_card(data: AQIData):
    """Render status card in sidebar"""
    cat = get_aqi_category(data.aqi)
    
    st.markdown(f"""
    <div style='background: {cat["color"]}20; padding: 15px; border-radius: 10px; 
         border-left: 4px solid {cat["color"]};'>
        <div style='font-size: 0.8rem; color: #666; font-weight: 600;'>CURRENT LOCATION</div>
        <div style='font-size: 1.2rem; font-weight: 700; color: {cat["color"]};'>{data.city_name}</div>
        <div style='font-size: 2rem; font-weight: 900; color: {cat["color"]};'>{data.aqi}</div>
        <div style='font-size: 0.9rem; color: {cat["color"]};'>{cat["emoji"]} {cat["label"]}</div>
    </div>
    """, unsafe_allow_html=True)
