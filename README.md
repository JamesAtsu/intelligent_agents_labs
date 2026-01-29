# Intelligent Agents Labs - SPADE Development

A comprehensive Python-based laboratory for developing intelligent agents using SPADE (Smart Python Agent Development Environment) with XMPP-based multi-agent communication.

## Overview

This project implements two core laboratory exercises in agent-based systems:

1. **Lab 1: Environment and Agent Platform Setup** - Basic SPADE agent configuration and deployment
2. **Lab 2: Perception and Environment Modeling** - Agent perception of disaster events and environmental monitoring

## Quick Start

### Prerequisites
- Python 3.8+
- XMPP server access (xmpp.jp configured)
- pip package manager

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Labs

```bash
# Lab 1: Verify XMPP setup
python lab1/xmpp_setup.py

# Lab 1: Run basic agent
python lab1/basic_agent.py

# Lab 2: Run environment demonstration
python lab2/demo.py
```

## Project Structure

```
intelligent_agents_labs/
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── lab1/                           # Lab 1: Basic agent setup
│   ├── basic_agent.py             # Simple SPADE agent implementation
│   └── xmpp_setup.py              # XMPP configuration verification
├── lab2/                           # Lab 2: Perception & environment modeling
│   ├── __init__.py                # Package initialization
│   ├── disaster_environment.py    # Simulated disaster environment
│   ├── sensor_agent.py            # Perception agent
│   ├── event_logger.py            # Event logging and analysis
│   └── demo.py                    # Demonstration script
└── reports/                        # Documentation and reports
    └── SETUP_REPORT.md            # Complete environment setup report
```

## Lab Details

### Lab 1: Environment and Agent Platform Setup

**Objective**: Configure Python agent development environment and deploy a basic agent

**Components**:
- BasicAgent: Simple agent with lifecycle management
- Startup behavior: Demonstrates agent initialization
- XMPP verification: Confirms server connectivity

**Key Features**:
- Asynchronous agent execution
- Behavior registration pattern
- XMPP protocol integration
- Logging and lifecycle management

### Lab 2: Perception and Environment Modeling

**Objective**: Implement agent perception of environmental and disaster-related events

**Components**:
- DisasterEnvironment: Simulates disaster events
- SensorAgent: Perceives and monitors environmental events
- EventLogger: Records and analyzes perceived events
- Event types: Earthquake, Flood, Wildfire, Hurricane, Landslide

**Key Features**:
- Continuous environmental monitoring
- Event generation and detection
- Damage assessment and severity classification
- Statistical analysis and reporting
- JSON-based event logging

## XMPP Configuration

**Server**: xmpp.jp  
**Agent JID**: james_016@xmpp.jp  
**Port**: 5222  
**Protocol**: XMPP with TLS/SSL  
**Authentication**: SASL/PLAIN

## Framework Details

### SPADE Architecture
- **Agents**: Autonomous entities with asynchronous behaviors
- **Behaviors**: 
  - OneShotBehaviour: Execute once on startup
  - CyclicBehaviour: Execute repeatedly with sleep intervals
- **Communication**: FIPA-ACL messages over XMPP
- **Execution Model**: Python asyncio with async/await

### Event Model (Lab 2)

Each disaster event contains:
- Event ID
- Disaster type (5 types)
- Location (8 zones)
- Severity level (1-5 scale)
- Damage assessment (0-100%)
- Affected population estimate
- Timestamp

## Documentation

- [Setup Report](reports/SETUP_REPORT.md) - Detailed environment configuration and analysis

## Dependencies

- **spade>=3.0.0** - Agent development framework (4.1.2 installed)
- **aiohttp>=3.7.4** - Async HTTP client
- **slixmpp-multiplatform** - Modern XMPP protocol library
- **requests>=2.28.0** - HTTP library
- **dnspython>=2.3.0** - DNS queries

## Usage Examples

### Run Lab 1 Agent
```python
from lab1.basic_agent import BasicAgent
import asyncio

async def main():
    agent = BasicAgent("james_016@xmpp.jp", "dk1963")
    await agent.start()
    await asyncio.sleep(3)
    await agent.stop()

asyncio.run(main())
```

### Generate Disaster Events
```python
from lab2.disaster_environment import DisasterEnvironment

env = DisasterEnvironment()
event = env.generate_event()
print(f"Event: {event.disaster_type.value} at {event.location}")
print(f"Severity: {event.severity_level.value}/5")
```

### Monitor Environment
```python
from lab2.disaster_environment import get_environment

env = get_environment()
summary = env.get_event_summary()
print(f"Events detected: {summary['total_events']}")
print(f"Critical events: {summary['critical_events']}")
```

## Status

✓ Lab 1 - Environment setup and basic agent: **COMPLETE**  
✓ Lab 2 - Perception and environment modeling: **COMPLETE**  
✓ XMPP configuration: **OPERATIONAL**  
✓ All tests: **PASSING**  

## Next Steps

Potential extensions:
- Multi-agent coordination for disaster response
- Agent decision-making with utility functions
- Message-based inter-agent communication
- Reactive behaviors to environmental conditions
- Agent planning and goal-oriented behavior

## Author Notes

Created in GitHub Codespaces environment with full async/await support for scalable agent implementations.