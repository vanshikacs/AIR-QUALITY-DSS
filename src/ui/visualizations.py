"""
Chart and visualization generation.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import List, Dict
from ..data.models import SearchHistoryEntry, ExposureResult


def create_exposure_gauge(result: ExposureResult) -> go.Figure:
    """Create exposure risk gauge"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result.score,
        title={'text': "Exposure Score", 'font': {'size': 20}},
        number={'font': {'size': 48, 'color': result.risk_color}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': result.risk_color},
            'steps': [
                {'range': [0, 20], 'color': 'rgba(139, 172, 133, 0.2)'},
                {'range': [20, 40], 'color': 'rgba(245, 215, 110, 0.2)'},
                {'range': [40, 60], 'color': 'rgba(242, 158, 76, 0.2)'},
                {'range': [60, 100], 'color': 'rgba(217, 83, 79, 0.2)'}
            ]
        }
    ))
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor='white')
    return fig


def create_trend_chart(history: List[SearchHistoryEntry]) -> go.Figure:
    """Create trend visualization"""
    df = pd.DataFrame([{
        'timestamp': e.timestamp,
        'aqi': e.aqi,
        'city': e.city
    } for e in history]).sort_values('timestamp')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['timestamp'], y=df['aqi'],
        mode='markers+lines', name='Actual AQI',
        line=dict(color='#6b8e65', width=2)
    ))
    
    if len(df) >= 3:
        df['ma'] = df['aqi'].rolling(3, min_periods=1).mean()
        fig.add_trace(go.Scatter(
            x=df['timestamp'], y=df['ma'],
            mode='lines', name='Moving Avg',
            line=dict(color='#f29e4c', width=2, dash='dash')
        ))
    
    fig.update_layout(
        title="AQI Trend Analysis",
        xaxis_title="Time", yaxis_title="AQI",
        template='plotly_white', height=400
    )
    return fig


def create_time_window_chart(windows: List[Dict], current_aqi: float) -> go.Figure:
    """Create time window comparison chart"""
    df = pd.DataFrame(windows)
    
    fig = px.bar(df, x='time', y='est_aqi',
                 title="Estimated AQI by Time Window",
                 color='est_aqi',
                 color_continuous_scale=['#8bac85', '#f5d76e', '#f29e4c', '#d9534f'],
                 text='est_aqi')
    
    fig.add_hline(y=current_aqi, line_dash="dash", line_color="red",
                  annotation_text=f"Current: {current_aqi}")
    
    fig.update_layout(template='plotly_white', height=350, showlegend=False)
    fig.update_traces(textposition='outside')
    return fig

