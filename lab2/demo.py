"""
LAB 2: Test and Demonstration Script

This script demonstrates the disaster environment and sensor agent
capabilities for lab evaluation.
"""

import asyncio
import logging
import json
import sys
from pathlib import Path
from datetime import datetime

# Handle imports for both direct and package execution
try:
    from disaster_environment import get_environment, DisasterEnvironment
    from event_logger import EventLogger, analyze_environment_state
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from disaster_environment import get_environment, DisasterEnvironment
    from event_logger import EventLogger, analyze_environment_state

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - Lab2Demo - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demonstrate_environment():
    """Demonstrate the disaster environment and event generation."""
    
    logger.info("=" * 70)
    logger.info("LAB 2: PERCEPTION AND ENVIRONMENT MODELING DEMONSTRATION")
    logger.info("=" * 70)
    
    # Initialize environment
    environment = DisasterEnvironment()
    event_logger = EventLogger("lab2_event_logs.json")
    
    # Generate multiple disaster events
    logger.info("\n--- Generating Disaster Events ---")
    for i in range(5):
        event = environment.generate_event()
        event_logger.log_event(event)
        
        logger.info(f"\nEvent {i+1}: {event.event_id}")
        logger.info(f"  Type: {event.disaster_type.value}")
        logger.info(f"  Location: {event.location}")
        logger.info(f"  Severity: {event.severity_level.value}/5")
        logger.info(f"  Damage: {event.damage_assessment}%")
        logger.info(f"  Population Affected: {event.affected_population}")
    
    # Save logs
    logger.info("\n--- Saving Event Logs ---")
    event_logger.save_logs()
    
    # Generate and display analysis report
    logger.info("\n--- Environment Analysis Report ---")
    report = event_logger.generate_report()
    logger.info(json.dumps(report, indent=2))
    
    # Display environment state
    logger.info("\n--- Current Environment State ---")
    state = environment.get_event_summary()
    logger.info(json.dumps(state, indent=2))
    
    logger.info("\n" + "=" * 70)
    logger.info("DEMONSTRATION COMPLETE")
    logger.info("=" * 70)


if __name__ == "__main__":
    demonstrate_environment()
