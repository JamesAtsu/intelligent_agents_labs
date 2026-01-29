"""
LAB 1: ENVIRONMENT AND AGENT PLATFORM SETUP
Basic SPADE Agent Implementation

This module implements a simple SPADE agent that demonstrates
basic agent functionality and XMPP communication.
"""

import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasicAgent(Agent):
    """
    A basic SPADE agent that demonstrates fundamental agent capabilities.
    
    This agent:
    - Connects to the XMPP server
    - Executes a startup behavior
    - Logs agent lifecycle events
    """
    
    class StartupBehaviour(OneShotBehaviour):
        """One-time startup behavior executed when the agent starts."""
        
        async def run(self):
            logger.info(f"Agent {self.agent.jid} started successfully!")
            logger.info("This is a basic SPADE agent demonstrating:")
            logger.info("  - Agent initialization")
            logger.info("  - Behavior execution")
            logger.info("  - Asynchronous message handling")
    
    async def setup(self):
        """Called when the agent starts. Registers initial behaviors."""
        logger.info(f"Setting up agent: {self.jid}")
        startup_behavior = self.StartupBehaviour()
        self.add_behaviour(startup_behavior)
        logger.info("Startup behavior registered")


async def main():
    """
    Main function to create and run the basic agent.
    
    Configuration:
    - JID (Jabber ID): james_016@xmpp.jp
    - XMPP Server: xmpp.jp (standard port 5222)
    """
    
    # Agent credentials
    jid = "james_016@xmpp.jp"
    password = "dk1963"
    
    # Create and configure agent
    agent = BasicAgent(jid, password)
    
    try:
        # Start the agent
        logger.info("=" * 60)
        logger.info("LAB 1: Starting Basic SPADE Agent")
        logger.info("=" * 60)
        
        await agent.start()
        
        # Allow agent to execute for a few seconds
        logger.info("Agent is running... (Press Ctrl+C to stop)")
        await asyncio.sleep(3)
        
        # Stop the agent gracefully
        await agent.stop()
        logger.info("Agent stopped successfully")
        
    except Exception as e:
        logger.error(f"Error running agent: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
