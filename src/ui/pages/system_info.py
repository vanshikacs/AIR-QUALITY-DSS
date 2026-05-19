"""System info page UI"""

import streamlit as st


def render_system_info_page():
    """Render system info page"""
    st.title("🔬 System Information")
    
    st.markdown("""
    ## About
    
    Professional analytical tool for exposure risk assessment and timing optimization.
    
    ---
    
    ### Data Sources
    
    **Provider:** World Air Quality Index (WAQI) Project  
    **Coverage:** 12,000+ stations in 1,000+ cities  
    **Update Frequency:** 1-6 hours (varies by location)
    
    ---
    
    ### Methodology
    
    **Exposure Score Formula:**
    ```
    Score = (AQI/100) × Hours × Activity_Mult × Sensitivity_Mult
    Normalized to 0-100 scale
    ```
    
    **Assumptions:**
    - Linear AQI-risk relationship
    - Activity affects respiration rate
    - Sensitivity from epidemiological data
    
    **Limitations:**
    - Does not account for individual medical history
    - Indoor air quality not modeled
    - Time windows based on typical patterns, not forecasts
    
    ---
    
    ### Disclaimer
    
    This system is for informational purposes only. Not a substitute for medical advice.
    Consult healthcare professionals for health-critical decisions.
    """)
    
    st.caption("AirFlow DSS v1.0 | Data © WAQI Project")