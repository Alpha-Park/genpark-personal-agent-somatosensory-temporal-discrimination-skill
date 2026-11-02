# Somatosensory Temporal Discrimination Threshold (STDT) Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/alphaparkinc/genpark-personal-agent-somatosensory-temporal-discrimination-skill)
[![OpenClaw Ready](https://img.shields.io/badge/OpenClaw-Compatible-purple.svg)](https://github.com/alphaparkinc/genpark-personal-agent-somatosensory-temporal-discrimination-skill)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io/)

A sovereign personal agent capability for computational somatosensory psychophysics, evaluating tactile temporal discrimination thresholds (STDT in ms), age-adjusted ratios, and cortical sensory gating.

## Architecture

```mermaid
flowchart TD
    StaircaseData["Tactile Paired Pulses: Ascending & Descending Inter-Stimulus Intervals (ISI in ms)"] --> ThresholdEngine["Composite STDT = (Mean_Asc + Mean_Desc) / 2"]
    ThresholdEngine --> AgeModel["Age-Adjusted Normative Model: 42.0 + (Age - 20) * 0.55 ms"]
    AgeModel --> RatioCalc["Threshold Ratio to Norm = STDT / Predicted Norm"]
    RatioCalc --> CSGI["Cortical Somatosensory Gating Index (CSGI: 0 - 100)"]
    CSGI --> Prescriptions["OpenClaw / Hermes Sensorimotor Recovery & Manual Rest Directives"]
```

## Quickstart

```python
from client import SomatosensoryTemporalDiscriminationClient

client = SomatosensoryTemporalDiscriminationClient()

# Evaluate STDT staircase test (ms)
asc = [45.0, 50.0, 48.0]
desc = [52.0, 48.0, 50.0]

res = client.evaluate_stdt_staircase(asc, desc, reference_age_years=32.0)

print("Composite STDT:", res["composite_stdt_ms"], "ms")
print("Predicted Norm:", res["predicted_age_norm_ms"], "ms")
print("Gating Index:", res["somatosensory_gating_index"], "/ 100")
print("Clinical Tier:", res["clinical_tier"])
```

## MCP Server Integration

Add to your `claude_desktop_config.json` or OpenClaw tool registry:

```json
{
  "mcpServers": {
    "stdt-temporal-discrimination": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-somatosensory-temporal-discrimination-skill/mcp_server.py"]
    }
  }
}
```

## License
MIT License.
