"""
LAB 2: PERCEPTION AND ENVIRONMENT MODELING
SensorAgent Implementation

This module implements a SensorAgent that monitors the disaster environment,
perceives events, and logs observations.
"""

import asyncio
import logging
from datetime import datetime
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from .disaster_environment import DisasterEnvironment, get_environment

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - SensorAgent - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EnvironmentMonitorBehaviour(CyclicBehaviour):
    """
    Cyclic behavior that continuously monitors the environment for disaster events.
    
    This behavior:
    - Periodically checks for new events
    - Logs environmental conditions
    - Maintains sensor observations
    """
    
    async def run(self):
        """Execute the monitoring cycle."""
        environment = get_environment()
        
        # Generate a new disaster event
        event = environment.generate_event()
        
        # Log the perceived event
        logger.info("=" * 70)
        logger.info(f"SENSOR PERCEPTION - Event Detected: {event.event_id}")
        logger.info("=" * 70)
        logger.info(f"  Disaster Type      : {event.disaster_type.value.upper()}")
        logger.info(f"  Location           : {event.location}")
        logger.info(f"  Severity Level     : {event.severity_level.value}/5")
        logger.info(f"  Damage Assessment  : {event.damage_assessment}%")
        logger.info(f"  Affected Population: {event.affected_population} people")
        logger.info(f"  Timestamp          : {event.timestamp.isoformat()}")
        logger.info("=" * 70)
        
        # Log environmental summary
        summary = environment.get_event_summary()
        logger.info("ENVIRONMENTAL STATUS UPDATE:")
        logger.info(f"  Total Events Detected    : {summary['total_events']}")
        logger.info(f"  Average Severity Level   : {summary['average_severity']}/5")
        logger.info(f"  Total Affected Population: {summary['total_affected_population']} people")
        logger.info(f"  Critical Events          : {summary['critical_events']}")
        logger.info(f"  Environment Status       : {summary['environmental_status']}")
        
        # Wait before next sensor cycle
        await asyncio.sleep(2)


class InitializationBehaviour(OneShotBehaviour):
    """One-time initialization behavior executed when the SensorAgent starts."""
    
    async def run(self):
        """Initialize the sensor agent and its monitoring capabilities."""
        logger.info("=" * 70)
        logger.info(f"SensorAgent {self.agent.jid} Initializing")
        logger.info("=" * 70)
        logger.info("Sensor Configuration:")
        logger.info("  - Type: Environmental Disaster Monitor")
        logger.info("  - Monitoring Interval: 2 seconds")
        logger.info("  - Event Types: Earthquake, Flood, Wildfire, Hurricane, Landslide")
        logger.info("  - Perception Modality: Event Detection and Assessment")
        logger.info("  - Severity Levels: Critical (5), Severe (4), Moderate (3), Minor (2), Low (1)")
        logger.info("=" * 70)


class SensorAgent(Agent):
    """
    An intelligent agent that perceives the disaster environment.
    
    The SensorAgent:
    - Continuously monitors environmental conditions
    - Detects and logs disaster events
    - Assesses damage severity levels
    - Maintains environmental state information
    - Communicates observations to other agents (in extended versions)
    """
    
    async def setup(self):
        """
        Called when the agent starts. Registers all required behaviors.
        """
        logger.info(f"Setting up SensorAgent: {self.jid}")
        
        # Register initialization behavior
        init_behaviour = InitializationBehaviour()
        self.add_behaviour(init_behaviour)
        
        # Register continuous monitoring behavior
        monitor_behaviour = EnvironmentMonitorBehaviour()
        self.add_behaviour(monitor_behaviour)
        
        logger.info("All behaviors registered successfully")


async def run_sensor_agent(duration: int = 30):
    """
    Create and run the SensorAgent for a specified duration.
    
    Args:
        duration: How long the agent should run in seconds (default: 30)
    """
    jid = "james_016@xmpp.jp"
    password = "dk1963"
    
    agent = SensorAgent(jid, password)
    
    try:
        logger.info("=" * 70)
        logger.info("LAB 2: Starting SensorAgent - Disaster Environment Monitoring")
        logger.info("=" * 70)
        
        await agent.start()
        
        logger.info(f"Agent is monitoring environment for {duration} seconds...")
        await asyncio.sleep(duration)
        
        await agent.stop()
        logger.info("SensorAgent stopped")
        
    except Exception as e:
        logger.error(f"Error running SensorAgent: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(run_sensor_agent())