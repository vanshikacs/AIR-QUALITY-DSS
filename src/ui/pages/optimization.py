"""Time optimization page UI"""

import streamlit as st
from ...analysis.optimization import TimeWindowOptimizer
from ...ui.visualizations import create_time_window_chart


def render_optimization_page():
    """Render optimization page"""
    st.title("⏰ Time Window Optimization")
    
    if not st.session_state.aqi_data:
        st.warning("⚠️ No data available")
        if st.button("← Go to Home"):
            st.session_state.current_page = '🏠 Home'
            st.rerun()
        return
    
    data = st.session_state.aqi_data
    optimizer = TimeWindowOptimizer(data.aqi, data.city_name)
    windows = optimizer.identify_windows()
    best = optimizer.get_best_window()
    
    if best:
        st.success(f"""
        **Best Window:** {best['time']}  
        **Est. AQI:** ~{best['est_aqi']}  
        **Reason:** {best['reason']}
        """)
    
    st.markdown("---")
    fig = create_time_window_chart(windows, data.aqi)
    st.plotly_chart(fig, use_container_width=True)

