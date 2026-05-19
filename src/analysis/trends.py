"""
Trend analysis module.
"""

import numpy as np
from typing import List
from ..data.models import SearchHistoryEntry


class TrendAnalyzer:
    """Analyze AQI trends from search history"""
    
    def __init__(self, history: List[SearchHistoryEntry]):
        self.history = sorted(history, key=lambda x: x.timestamp)
    
    def analyze(self) -> List[str]:
        """Generate actionable insights"""
        if len(self.history) < 3:
            return ["Insufficient data. Search more locations to enable trend analysis."]
        
        insights = []
        aqi_values = [e.aqi for e in self.history]
        
        # Direction analysis
        recent_avg = np.mean(aqi_values[-3:])
        older_avg = np.mean(aqi_values[:3])
        change_pct = ((recent_avg - older_avg) / older_avg) * 100
        
        if change_pct > 20:
            insights.append(f"Deteriorating: AQI increased {change_pct:.1f}% in recent searches")
        elif change_pct < -20:
            insights.append(f"Improving: AQI decreased {abs(change_pct):.1f}% in recent searches")
        else:
            insights.append(f"Stable: AQI consistent (±{abs(change_pct):.1f}%)")
        
        # Volatility
        if len(aqi_values) >= 5:
            std = np.std(aqi_values)
            if std > 50:
                insights.append(f"High variability detected (σ={std:.1f})")
            else:
                insights.append(f"Low variability (σ={std:.1f})")
        
        # Extremes
        max_aqi = max(aqi_values)
        min_aqi = min(aqi_values)
        max_city = self.history[aqi_values.index(max_aqi)].city
        min_city = self.history[aqi_values.index(min_aqi)].city
        
        insights.append(f"Peak: {max_aqi} in {max_city}")
        insights.append(f"Best: {min_aqi} in {min_city}")
        
        return insights