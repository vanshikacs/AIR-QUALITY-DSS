"""
Time window optimization module.
"""

from typing import List, Dict, Optional
from ..utils.constants import TIME_WINDOW_PATTERNS


class TimeWindowOptimizer:
    """
    Identify optimal time windows for outdoor activities.
    
    Uses typical urban pollution patterns. In production, would integrate
    hourly forecast API.
    """
    
    def __init__(self, current_aqi: float, location: str):
        self.current_aqi = current_aqi
        self.location = location
    
    def identify_windows(self) -> List[Dict]:
        """Identify safer time windows"""
        # Determine pattern based on AQI
        for pattern_name, pattern_data in TIME_WINDOW_PATTERNS.items():
            if self.current_aqi > pattern_data['threshold']:
                windows = []
                for window in pattern_data['windows']:
                    windows.append({
                        'time': window['time'],
                        'est_aqi': int(self.current_aqi * window['factor']),
                        'reason': window['reason']
                    })
                return windows
        
        # Default: any time
        return [{'time': 'Any time', 'est_aqi': int(self.current_aqi), 
                 'reason': 'Air quality acceptable'}]
    
    def get_best_window(self) -> Optional[Dict]:
        """Get the optimal window"""
        windows = self.identify_windows()
        return windows[0] if windows else None