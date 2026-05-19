"""
Data models for type safety and validation.
"""

from typing import Dict, Optional, List
from datetime import datetime
from dataclasses import dataclass
from ..utils.helpers import safe_pollutants


@dataclass
class AQIData:
    """Air Quality Index data model"""
    aqi: int
    city_name: str
    latitude: float
    longitude: float
    dominant_pollutant: Optional[str]
    pollutants: Dict[str, int]
    timestamp: str
    raw_data: Dict
    
    @classmethod
    def from_api_response(cls, data: Dict) -> 'AQIData':
        """Create AQIData from API response"""
        return cls(
            aqi=int(float(data.get('aqi', 0))),
            city_name=data.get('city', {}).get('name', 'Unknown'),
            latitude=float(data.get('city', {}).get('geo', [0, 0])[0]),
            longitude=float(data.get('city', {}).get('geo', [0, 0])[1]),
            dominant_pollutant=data.get('dominentpol'),
            pollutants=safe_pollutants(data.get('iaqi', {})),
            timestamp=data.get('time', {}).get('s', 'Unknown'),
            raw_data=data
        )


@dataclass
class UserProfile:
    """User profile data model"""
    name: str
    outdoor_hours: float
    activity_level: str
    sensitivity: str
    
    def to_dict(self) -> Dict:
        return {
            'outdoor_hours': self.outdoor_hours,
            'activity_level': self.activity_level,
            'sensitivity': self.sensitivity
        }
    
    @classmethod
    def from_dict(cls, name: str, data: Dict) -> 'UserProfile':
        return cls(
            name=name,
            outdoor_hours=data['outdoor_hours'],
            activity_level=data['activity_level'],
            sensitivity=data['sensitivity']
        )


@dataclass
class SearchHistoryEntry:
    """Search history entry model"""
    city: str
    aqi: int
    timestamp: datetime


@dataclass
class ExposureResult:
    """Exposure analysis result model"""
    score: float
    risk_level: str
    risk_color: str
    risk_emoji: str
    components: Dict
    recommendation: str