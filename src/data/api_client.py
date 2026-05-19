"""
API client for fetching air quality data.
"""

import requests
from typing import Optional
from ..utils.constants import API_BASE_URL, API_TOKEN, API_TIMEOUT
from ..utils.helpers import clean_location
from .models import AQIData


class AQIAPIClient:
    """Client for WAQI API"""
    
    def __init__(self, token: str = API_TOKEN):
        self.token = token
        self.base_url = API_BASE_URL
        self.timeout = API_TIMEOUT
    
    def fetch_aqi(self, location: str) -> Optional[AQIData]:
        """
        Fetch AQI data for a location.
        
        Args:
            location: City name or coordinates
            
        Returns:
            AQIData object or None if failed
        """
        location = clean_location(location)
        url = f"{self.base_url}/{location}/?token={self.token}"
        
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "ok":
                return AQIData.from_api_response(data["data"])
            return None
            
        except requests.Timeout:
            raise Exception("API request timed out")
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Failed to process API response: {str(e)}")


