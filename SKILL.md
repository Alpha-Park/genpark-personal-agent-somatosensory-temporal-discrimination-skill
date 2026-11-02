---
name: genpark-personal-agent-somatosensory-temporal-discrimination-skill
description: Deterministic evaluation of Somatosensory Temporal Discrimination Threshold (STDT in ms), tactile temporal resolution, and basal ganglia sensory gating.
version: 1.0.0
author: GenPark Autonomous Agents Ecosystem
license: MIT
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
---

# Somatosensory Temporal Discrimination Threshold (STDT) Skill

## Overview
The `genpark-personal-agent-somatosensory-temporal-discrimination-skill` equips personal sovereign agents with central somatosensory neuro-analytics. The Somatosensory Temporal Discrimination Threshold (STDT) is the shortest time interval (in milliseconds) at which paired tactile stimuli are perceived as two distinct events rather than one fused sensation. Regulated by GABAergic intracortical inhibition and basal ganglia circuits, STDT provides a sensitive index of sensory gating, deteriorating under mental exhaustion, central motor drive fatigue, or subclinical movement disorders.

## Physiological Model & Mathematics
1. **Composite STDT Staircase Threshold**:
   $$STDT = \frac{\overline{ISI}_{\text{ascending}} + \overline{ISI}_{\text{descending}}}{2}$$
2. **Age-Adjusted Normative Prediction**:
   $$STDT_{\text{pred}} = 42.0 + (\text{Age} - 20) \times 0.55 \quad (\text{ms})$$
3. **Threshold Ratio to Norm**:
   $$\text{Ratio} = \frac{STDT}{STDT_{\text{pred}}}$$
   - **Optimal Sensory Gating**: $\text{Ratio} \le 1.0$.
   - **Normal Baseline**: $1.0 - 1.4$.
   - **Gating Blurring / Fatigue**: $> 1.8$.
4. **Cortical Somatosensory Gating Index ($CSGI$)**:
   Standardized 0 to 100 metric reflecting intracortical inhibitory precision.

## Tools & Endpoints
- `evaluate_stdt_staircase`: Computes composite STDT, age-adjusted ratio, hysteresis, and sensory gating index.
