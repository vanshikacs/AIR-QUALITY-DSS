"""Small reusable helper utilities for AirFlow."""

from datetime import datetime
from typing import Any, Dict


def clean_location(location: str) -> str:
    """Normalize city/location input before sending it to the API."""
    return " ".join((location or "").strip().split())


def format_timestamp(value: str) -> str:
    """Return a readable timestamp while safely handling unknown formats."""
    if not value:
        return "Unknown"
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).strftime("%d %b %Y, %I:%M %p")
    except Exception:
        return value


def safe_pollutants(raw_iaqi: Dict[str, Any]) -> Dict[str, int]:
    """Convert WAQI pollutant payload into a clean integer dictionary."""
    pollutants: Dict[str, int] = {}
    for key, value in (raw_iaqi or {}).items():
        try:
            pollutants[key] = int(float(value.get("v", 0)))
        except Exception:
            pollutants[key] = 0
    return pollutants
