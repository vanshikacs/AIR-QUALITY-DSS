
"""
Exposure risk analysis module.
"""

from typing import Dict
from ..utils.constants import EXPOSURE_WEIGHTS
from ..data.models import UserProfile, ExposureResult


class ExposureAnalyzer:
    """
    Calculate personalized exposure risk score.
    
    Formula: Score = (AQI/100) × Hours × Activity_Mult × Sensitivity_Mult
    Normalized to 0-100 scale
    """
    
    def __init__(self, aqi: float, profile: UserProfile):
        self.aqi = aqi
        self.profile = profile
    
    def calculate(self) -> ExposureResult:
        """Calculate exposure score with full breakdown"""
        # Calculate components
        aqi_factor = min(self.aqi / 100, 5.0)
        hours = self.profile.outdoor_hours
        activity_mult = EXPOSURE_WEIGHTS['activity_multipliers'][self.profile.activity_level]
        sensitivity_mult = EXPOSURE_WEIGHTS['sensitivity_multipliers'][self.profile.sensitivity]
        
        # Raw score
        raw_score = aqi_factor * hours * activity_mult * sensitivity_mult
        
        # Normalize to 0-100
        score = min((raw_score / 40) * 100, 100)
        
        # Determine risk level
        if score < 20:
            risk_level = 'Low'
            risk_color = '#8bac85'
            risk_emoji = '🟢'
            recommendation = "Normal outdoor activities are safe with current conditions."
        elif score < 40:
            risk_level = 'Moderate'
            risk_color = '#f5d76e'
            risk_emoji = '🟡'
            recommendation = "Consider limiting prolonged outdoor exposure. Sensitive individuals be cautious."
        elif score < 60:
            risk_level = 'Elevated'
            risk_color = '#f29e4c'
            risk_emoji = '🟠'
            recommendation = "Reduce outdoor time and use protective measures (N95 masks)."
        else:
            risk_level = 'High'
            risk_color = '#d9534f'
            risk_emoji = '🔴'
            recommendation = "Minimize outdoor exposure. Use N95 masks if unavoidable."
        
        # Package results
        components = {
            'aqi_factor': aqi_factor,
            'hours': hours,
            'activity_mult': activity_mult,
            'sensitivity_mult': sensitivity_mult,
            'raw_score': raw_score
        }
        
        return ExposureResult(
            score=score,
            risk_level=risk_level,
            risk_color=risk_color,
            risk_emoji=risk_emoji,
            components=components,
            recommendation=recommendation
        )
