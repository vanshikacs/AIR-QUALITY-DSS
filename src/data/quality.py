
"""
Data quality assessment module.
"""

from datetime import datetime
from typing import Dict
from .models import AQIData


class DataQualityAssessor:
    """Assess data quality metrics"""
    
    def __init__(self, data: AQIData):
        self.data = data
    
    def assess_completeness(self) -> float:
        """Calculate data completeness score (0-1)"""
        required_fields = ['aqi', 'city_name', 'latitude', 'longitude', 'timestamp']
        available = sum(1 for field in required_fields if getattr(self.data, field))
        return available / len(required_fields)
    
    def assess_recency(self) -> str:
        """Assess how recent the data is"""
        try:
            update_time = datetime.fromisoformat(self.data.timestamp.replace('Z', '+00:00'))
            age = datetime.now(update_time.tzinfo) - update_time
            hours = age.total_seconds() / 3600
            
            if hours < 1: return "Excellent (<1h)"
            elif hours < 3: return "Good (<3h)"
            elif hours < 6: return "Fair (<6h)"
            else: return "Stale (>6h)"
        except:
            return "Unknown"
    
    def assess_reliability(self) -> str:
        """Overall reliability assessment"""
        completeness = self.assess_completeness()
        recency = self.assess_recency()
        
        if completeness >= 0.9 and recency == "Excellent (<1h)":
            return "High"
        elif completeness >= 0.7:
            return "Moderate"
        return "Low"
    
    def get_summary(self) -> str:
        """Generate quality summary"""
        completeness = self.assess_completeness()
        recency = self.assess_recency()
        reliability = self.assess_reliability()
        
        return f"Completeness: {completeness*100:.0f}% | Recency: {recency} | Reliability: {reliability}"
