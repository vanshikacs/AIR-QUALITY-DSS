"""Trend analysis page UI"""

import streamlit as st
from ...analysis.trends import TrendAnalyzer
from ...ui.visualizations import create_trend_chart


def render_trends_page():
    """Render trends page"""
    st.title("📈 Trend Intelligence")
    
    if len(st.session_state.search_history) < 3:
        st.warning("⚠️ Need 3+ searches")
        if st.button("← Go to Home"):
            st.session_state.current_page = '🏠 Home'
            st.rerun()
        return
    
    analyzer = TrendAnalyzer(st.session_state.search_history)
    insights = analyzer.analyze()
    
    st.markdown("### Key Insights")
    for insight in insights:
        st.success(f"• {insight}")
    
    st.markdown("---")
    st.markdown("### Trend Chart")
    fig = create_trend_chart(st.session_state.search_history)
    st.plotly_chart(fig, use_container_width=True)
