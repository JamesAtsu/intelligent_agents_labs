"""
LAB 1 & 2 Combined Demo Script

This script demonstrates both laboratories in sequence:
1. XMPP setup verification
2. Basic agent initialization
3. Disaster environment simulation with SensorAgent
"""

import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from lab1.xmpp_setup import verify_xmpp_setup
from lab2.demo import demonstrate_environment

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_complete_demo():
    """Run complete demonstration of both labs."""
    
    logger.info("\n\n")
    logger.info("╔" + "=" * 68 + "╗")
    logger.info("║" + " " * 68 + "║")
    logger.info("║" + "INTELLIGENT AGENTS LABS - COMPLETE DEMONSTRATION".center(68) + "║")
    logger.info("║" + " " * 68 + "║")
    logger.info("╚" + "=" * 68 + "╝")
    
    # Lab 1: Verify XMPP Setup
    logger.info("\n\n--- PHASE 1: XMPP ENVIRONMENT VERIFICATION ---\n")
    verify_xmpp_setup()
    
    # Lab 2: Disaster Environment Demonstration
    logger.info("\n\n--- PHASE 2: DISASTER ENVIRONMENT PERCEPTION ---\n")
    demonstrate_environment()
    
    # Summary
    logger.info("\n\n")
    logger.info("╔" + "=" * 68 + "╗")
    logger.info("║" + " " * 68 + "║")
    logger.info("║" + "DEMONSTRATION COMPLETE - ALL LABS OPERATIONAL".center(68) + "║")
    logger.info("║" + " " * 68 + "║")
    logger.info("╚" + "=" * 68 + "╝")
    
    logger.info("\nNext Steps:")
    logger.info("  1. Review event logs in lab2_event_logs.json")
    logger.info("  2. Analyze environment data in reports/SETUP_REPORT.md")
    logger.info("  3. Extend agents with inter-agent communication")
    logger.info("  4. Implement decision-making behaviors")


if __name__ == "__main__":
    run_complete_demo()
