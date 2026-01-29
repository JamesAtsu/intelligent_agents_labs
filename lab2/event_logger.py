"""
LAB 2: Event Logger and Analysis

This module provides logging utilities and analysis tools for disaster events
detected by the SensorAgent.
"""

import json
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Handle imports for both direct and package execution
try:
    from disaster_environment import DisasterEvent, get_environment
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from disaster_environment import DisasterEvent, get_environment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EventLogger:
    """
    Logs disaster events to file and memory for analysis.
    
    Maintains a persistent record of all perceived events for
    analysis and historical reference.
    """
    
    def __init__(self, log_file: str = "event_logs.json"):
        """
        Initialize the event logger.
        
        Args:
            log_file: Path to the file where events will be logged
        """
        self.log_file = log_file
        self.events_log: List[Dict] = []
        logger.info(f"EventLogger initialized with log file: {log_file}")
    
    def log_event(self, event: DisasterEvent) -> None:
        """
        Log a disaster event.
        
        Args:
            event: The DisasterEvent to log
        """
        event_dict = event.to_dict()
        self.events_log.append(event_dict)
        
        logger.info(f"Event logged: {event.event_id}")
    
    def save_logs(self) -> None:
        """Save all logged events to the log file."""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.events_log, f, indent=2)
            logger.info(f"Logs saved to {self.log_file}")
        except Exception as e:
            logger.error(f"Error saving logs: {e}")
    
    def generate_report(self) -> Dict:
        """
        Generate an analysis report of all logged events.
        
        Returns:
            Dictionary containing event statistics and analysis
        """
        if not self.events_log:
            return {"error": "No events logged"}
        
        severity_counts = {}
        disaster_counts = {}
        
        for event in self.events_log:
            severity = event['severity_level']
            disaster = event['disaster_type']
            
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            disaster_counts[disaster] = disaster_counts.get(disaster, 0) + 1
        
        report = {
            "total_events": len(self.events_log),
            "severity_distribution": severity_counts,
            "disaster_distribution": disaster_counts,
            "log_file": self.log_file,
            "report_generated": datetime.now().isoformat()
        }
        
        return report


def analyze_environment_state() -> Dict:
    """
    Analyze the current state of the disaster environment.
    
    Returns:
        Dictionary containing environmental analysis
    """
    environment = get_environment()
    summary = environment.get_event_summary()
    recent = environment.get_recent_events(3)
    
    analysis = {
        "environment_summary": summary,
        "recent_events": [e.to_dict() for e in recent],
        "analysis_timestamp": datetime.now().isoformat()
    }
    
    return analysis
