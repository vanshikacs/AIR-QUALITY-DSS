"""Exposure analysis page UI"""

import streamlit as st
from ...analysis.exposure import ExposureAnalyzer
from ...ui.visualizations import create_exposure_gauge
from ...state import SessionState


def render_exposure_page():
    """Render exposure analysis page"""
    st.title("📊 Exposure Risk Assessment")
    
    if not st.session_state.aqi_data:
        st.warning("⚠️ No data available")
        if st.button("← Go to Home"):
            st.session_state.current_page = '🏠 Home'
            st.rerun()
        return
    
    data = st.session_state.aqi_data
    profile = SessionState.get_current_profile()
    
    # Calculate
    analyzer = ExposureAnalyzer(data.aqi, profile)
    result = analyzer.calculate()
    st.session_state.exposure_score = result
    
    st.markdown(f"**Location:** {data.city_name} | **AQI:** {data.aqi} | **Profile:** {st.session_state.current_profile_name}")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = create_exposure_gauge(result)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div style='background: {result.risk_color}15; padding: 25px; border-radius: 12px; border-left: 5px solid {result.risk_color};'>
            <div style='font-size: 1.8rem; font-weight: 700; color: {result.risk_color};'>
                {result.risk_emoji} {result.risk_level} Risk
            </div>
            <div style='margin-top: 15px;'>{result.recommendation}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Calculation Breakdown")
        comp = result.components
        st.markdown(f"""
        - **AQI Factor:** {comp['aqi_factor']:.2f}
        - **Hours:** {comp['hours']:.1f}
        - **Activity:** {comp['activity_mult']:.1f}x
        - **Sensitivity:** {comp['sensitivity_mult']:.1f}x
        
        **Score:** {result.score:.1f}/100
        """)