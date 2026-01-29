# Quick Reference Guide

## Project Setup

### Installation (One-time)
```bash
cd /workspaces/intelligent_agents_labs
pip install -r requirements.txt
```

### Verify Installation
```bash
python lab1/xmpp_setup.py
```

## Running the Labs

### Lab 1: Basic Agent & XMPP Setup
```bash
# Verify XMPP configuration
python lab1/xmpp_setup.py

# Run basic agent (requires XMPP server)
python lab1/basic_agent.py
```

### Lab 2: Disaster Environment & Perception
```bash
# Run environment demonstration (generates 5 events)
python lab2/demo.py

# View generated event logs
cat lab2_event_logs.json | python -m json.tool
```

## Project Structure Quick Reference

```
intelligent_agents_labs/
├── lab1/                      # Basic agent setup
│   ├── basic_agent.py        # Simple SPADE agent
│   └── xmpp_setup.py         # Server verification
├── lab2/                      # Perception & environment
│   ├── disaster_environment.py    # Event simulation
│   ├── sensor_agent.py            # Monitoring agent
│   ├── event_logger.py            # Logging utilities
│   └── demo.py                    # Demo script
├── reports/
│   └── SETUP_REPORT.md       # Detailed setup documentation
├── README.md                  # Main documentation
├── IMPLEMENTATION_SUMMARY.md  # This implementation details
├── requirements.txt           # Dependencies
└── run_demo.py               # Combined demo runner
```

## Key Components

### DisasterEnvironment
```python
from lab2.disaster_environment import DisasterEnvironment

env = DisasterEnvironment()
event = env.generate_event()  # Creates random disaster event
summary = env.get_event_summary()  # Gets stats: total, severity, affected pop
```

### SensorAgent
```python
from lab2.sensor_agent import SensorAgent

agent = SensorAgent("james_016@xmpp.jp", "dk1963")
await agent.start()  # Starts monitoring
await asyncio.sleep(10)
await agent.stop()  # Stops agent
```

### EventLogger
```python
from lab2.event_logger import EventLogger

logger = EventLogger("events.json")
logger.log_event(event)
logger.save_logs()
report = logger.generate_report()
```

## Event Structure

Each disaster event contains:
```json
{
  "event_id": "EVT_0001",           # Unique identifier
  "disaster_type": "earthquake",    # Type of disaster
  "location": "Downtown District",  # Where it occurred
  "severity_level": 4,              # 1-5 scale
  "damage_assessment": "75%",       # Damage percentage
  "timestamp": "2026-01-29T11:14:47",
  "affected_population": 2500       # Estimated people affected
}
```

## Disaster Types
- **Earthquake**: Ground displacement events
- **Flood**: Water-based disasters
- **Wildfire**: Uncontrolled fires
- **Hurricane**: Severe storms with high winds
- **Landslide**: Mass ground movement

## Severity Levels
- **1 (Low)**: Minor damage, few affected
- **2 (Minor)**: Limited impact
- **3 (Moderate)**: Significant damage
- **4 (Severe)**: Major disaster
- **5 (Critical)**: Catastrophic event

## XMPP Configuration
- **Server**: xmpp.jp
- **Port**: 5222
- **Agent**: james_016@xmpp.jp
- **Password**: dk1963

## Common Commands

### View event logs with formatting
```bash
cd /workspaces/intelligent_agents_labs
python -m json.tool lab2_event_logs.json
```

### Count events by type
```bash
cat lab2_event_logs.json | python -c "
import json, sys
data = json.load(sys.stdin)
types = {}
for e in data:
    t = e['disaster_type']
    types[t] = types.get(t, 0) + 1
print(json.dumps(types, indent=2))
"
```

### Get severity statistics
```bash
cat lab2_event_logs.json | python -c "
import json, sys
data = json.load(sys.stdin)
sevs = [e['severity_level'] for e in data]
print(f'Count: {len(data)}')
print(f'Average Severity: {sum(sevs)/len(sevs):.1f}/5')
print(f'Max: {max(sevs)}, Min: {min(sevs)}')
"
```

## Troubleshooting

### Import Errors
If you get `ImportError` when running demo.py:
- Ensure you're in the correct directory: `/workspaces/intelligent_agents_labs`
- Run as module: `python -m lab2.demo`
- Or change to lab2 directory: `cd lab2 && python demo.py`

### XMPP Connection Issues
- Verify credentials are correct (james_016@xmpp.jp)
- Check xmpp.jp server is accessible
- Ensure port 5222 is not blocked

### SPADE Not Found
```bash
pip install -r requirements.txt
```

## Output Locations

After running demo.py, check:
- **Event logs**: `lab2_event_logs.json`
- **Setup report**: `reports/SETUP_REPORT.md`
- **Implementation details**: `IMPLEMENTATION_SUMMARY.md`
- **Console output**: Printed directly (grep for "Event")

## Python Version Check
```bash
python --version  # Should be 3.8 or higher
```

## File Sizes
- disaster_environment.py: ~410 lines
- sensor_agent.py: ~170 lines
- event_logger.py: ~140 lines
- Total implementation: ~810 lines
- Documentation: ~2500 lines

## Next Steps

1. **Extend the agent**: Add decision-making capabilities
2. **Multi-agent**: Create multiple agents that communicate
3. **Real-time visualization**: Build a dashboard for events
4. **Database storage**: Persist events to a database
5. **Advanced behaviors**: Implement FSM-based planning

## Getting Help

1. Check `IMPLEMENTATION_SUMMARY.md` for detailed info
2. Review `reports/SETUP_REPORT.md` for environment details
3. Look at inline code comments in the modules
4. Run individual test scripts: `python lab1/xmpp_setup.py`

---
**Last Updated**: 2026-01-29  
**Status**: ✅ Complete and tested  
**Python**: 3.8+  
**SPADE**: 2.3.1
