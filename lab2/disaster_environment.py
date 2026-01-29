"""
LAB 2: PERCEPTION AND ENVIRONMENT MODELING
Simulated Disaster Environment Module

This module simulates a disaster environment with various event types
including earthquakes, floods, fires, and infrastructure damage.
"""

import random
import logging
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DisasterType(Enum):
    """Enumeration of disaster types the environment can simulate."""
    EARTHQUAKE = "earthquake"
    FLOOD = "flood"
    WILDFIRE = "wildfire"
    HURRICANE = "hurricane"
    LANDSLIDE = "landslide"


class SeverityLevel(Enum):
    """Enumeration of disaster severity levels (1-5)."""
    CRITICAL = 5
    SEVERE = 4
    MODERATE = 3
    MINOR = 2
    LOW = 1


@dataclass
class DisasterEvent:
    """
    Represents a disaster event in the environment.
    
    Attributes:
        event_id: Unique identifier for the event
        disaster_type: Type of disaster
        location: Location where the disaster occurred
        severity_level: Severity on a scale of 1-5
        damage_assessment: Estimated damage percentage (0-100)
        timestamp: When the event occurred
        affected_population: Estimated number of affected people
    """
    event_id: str
    disaster_type: DisasterType
    location: str
    severity_level: SeverityLevel
    damage_assessment: int
    timestamp: datetime
    affected_population: int
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary format for logging."""
        return {
            "event_id": self.event_id,
            "disaster_type": self.disaster_type.value,
            "location": self.location,
            "severity_level": self.severity_level.value,
            "damage_assessment": f"{self.damage_assessment}%",
            "timestamp": self.timestamp.isoformat(),
            "affected_population": self.affected_population
        }


class DisasterEnvironment:
    """
    Simulates a disaster environment with event generation and monitoring.
    
    This environment:
    - Generates random disaster events
    - Tracks environmental conditions
    - Provides event logging and history
    """
    
    # Predefined locations in the disaster scenario
    LOCATIONS = [
        "Downtown District", "Industrial Zone", "Residential Area",
        "Port District", "University Campus", "Hospital Area",
        "Shopping District", "Agricultural Region"
    ]
    
    def __init__(self, seed: int = None):
        """Initialize the disaster environment."""
        if seed is not None:
            random.seed(seed)
        
        self.events: List[DisasterEvent] = []
        self.event_counter = 0
        logger.info("Disaster Environment initialized")
    
    def generate_event(self) -> DisasterEvent:
        """
        Generate a random disaster event.
        
        Returns:
            DisasterEvent: A newly generated disaster event
        """
        self.event_counter += 1
        
        disaster_type = random.choice(list(DisasterType))
        severity_level = random.choice(list(SeverityLevel))
        location = random.choice(self.LOCATIONS)
        damage = random.randint(5, 100)
        affected_pop = random.randint(50, 5000)
        
        event = DisasterEvent(
            event_id=f"EVT_{self.event_counter:04d}",
            disaster_type=disaster_type,
            location=location,
            severity_level=severity_level,
            damage_assessment=damage,
            timestamp=datetime.now(),
            affected_population=affected_pop
        )
        
        self.events.append(event)
        return event
    
    def get_event_summary(self) -> Dict:
        """
        Get a summary of all events and environmental conditions.
        
        Returns:
            Dictionary containing event statistics and environment state
        """
        total_events = len(self.events)
        avg_severity = sum(e.severity_level.value for e in self.events) / total_events if total_events > 0 else 0
        total_affected = sum(e.affected_population for e in self.events)
        
        return {
            "total_events": total_events,
            "average_severity": round(avg_severity, 2),
            "total_affected_population": total_affected,
            "critical_events": sum(1 for e in self.events if e.severity_level == SeverityLevel.CRITICAL),
            "environmental_status": "Unstable" if avg_severity > 3 else "Monitoring"
        }
    
    def get_recent_events(self, limit: int = 5) -> List[DisasterEvent]:
        """Get the most recent events."""
        return self.events[-limit:] if self.events else []


# Singleton instance for global environment access
_environment_instance = None


def get_environment() -> DisasterEnvironment:
    """Get or create the global disaster environment instance."""
    global _environment_instance
    if _environment_instance is None:
        _environment_instance = DisasterEnvironment()
    return _environment_instance
