"""
User profile management module.
"""

from typing import Dict
from ..data.models import UserProfile
from ..utils.constants import DEFAULT_PROFILE


class ProfileManager:
    """Manage user profiles"""
    
    def __init__(self):
        self.profiles: Dict[str, UserProfile] = {}
        self._initialize_default()
    
    def _initialize_default(self):
        """Create default profile"""
        self.profiles['Default'] = UserProfile(
            name='Default',
            **DEFAULT_PROFILE
        )
    
    def save_profile(self, name: str, profile_data: Dict):
        """Save a profile"""
        self.profiles[name] = UserProfile.from_dict(name, profile_data)
    
    def load_profile(self, name: str) -> UserProfile:
        """Load a profile"""
        return self.profiles.get(name, self.profiles['Default'])
    
    def delete_profile(self, name: str):
        """Delete a profile (except Default)"""
        if name != 'Default' and name in self.profiles:
            del self.profiles[name]
    
    def list_profiles(self) -> list:
        """Get all profile names"""
        return list(self.profiles.keys())
