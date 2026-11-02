"""
Somatosensory Temporal Discrimination Threshold (STDT) & Gating Engine.
Provides deterministic, zero-dependency psychophysiological calculation of tactile temporal resolution,
ascending/descending inter-stimulus intervals (ISI), and basal ganglia-cortical inhibitory gating.
"""

from typing import Dict, Any, List, Optional


class SomatosensoryTemporalDiscriminationClient:
    """
    Deterministic client for calculating Somatosensory Temporal Discrimination Threshold (STDT) in milliseconds.
    Pure Python standard library implementation based on Lacruz et al. and Conte et al. sensorimotor standards.
    """

    def __init__(self):
        pass

    def evaluate_stdt_staircase(
        self,
        ascending_isi_trials_ms: List[float],
        descending_isi_trials_ms: List[float],
        reference_age_years: float = 35.0
    ) -> Dict[str, Any]:
        """
        Evaluates STDT staircase trials:
        - ascending_isi_trials_ms: Inter-stimulus intervals (ms) where paired pulses were first recognized as 2 distinct stimuli.
        - descending_isi_trials_ms: Inter-stimulus intervals (ms) where paired pulses fused into 1 stimulus.
        - reference_age_years: Subject age to adjust normative physiological expectations.
        """
        if not ascending_isi_trials_ms or not descending_isi_trials_ms:
            return {"error": "Both ascending and descending ISI trial lists must be non-empty"}

        mean_asc = sum(ascending_isi_trials_ms) / len(ascending_isi_trials_ms)
        mean_desc = sum(descending_isi_trials_ms) / len(descending_isi_trials_ms)

        stdt_threshold_ms = round((mean_asc + mean_desc) / 2.0, 1)
        hysteresis_ms = round(abs(mean_desc - mean_asc), 1)

        # Age-adjusted predicted normal threshold (Conte et al.):
        # Young adults ~ 35 - 55 ms; expands ~ 0.5 - 0.7 ms per year above age 20
        age = max(18.0, min(95.0, reference_age_years))
        predicted_norm_ms = round(42.0 + (age - 20.0) * 0.55, 1)

        ratio_to_norm = round(stdt_threshold_ms / predicted_norm_ms, 2)

        # Cortical Somatosensory Gating Index (CSGI, 0 - 100):
        # Ratio <= 1.0 -> 85-95. Ratio 1.0 - 1.4 -> 60-84. Ratio > 1.8 -> < 40 (Impaired Gating).
        if ratio_to_norm <= 1.0:
            csgi = min(100.0, 85.0 + (1.0 - ratio_to_norm) * 25.0)
        elif ratio_to_norm <= 1.40:
            csgi = 60.0 + ((1.40 - ratio_to_norm) / 0.40) * 24.0
        elif ratio_to_norm <= 1.80:
            csgi = 35.0 + ((1.80 - ratio_to_norm) / 0.40) * 24.0
        else:
            csgi = max(5.0, 35.0 - (ratio_to_norm - 1.80) * 20.0)

        csgi_score = round(min(100.0, max(5.0, csgi)), 1)

        if csgi_score >= 80.0:
            tier = "SHARP_INTRACORTICAL_INHIBITORY_GATING"
            interpretation = f"Intact somatosensory temporal resolution ({stdt_threshold_ms} ms vs predicted {predicted_norm_ms} ms); robust GABAergic cortical inhibition."
            guidance = "Fine sensorimotor differentiation is optimal. Full capacity for high-speed manual motor tasks."
        elif csgi_score >= 60.0:
            tier = "NORMAL_PHYSIOLOGICAL_TEMPORAL_DISCRIMINATION"
            interpretation = f"Normal tactile temporal threshold ({stdt_threshold_ms} ms); age-appropriate central somatosensory gating."
            guidance = "Routine tactile acuity preserved. Maintain regular manual dexterity activities."
        elif csgi_score >= 35.0:
            tier = "MILD_SOMATOSENSORY_GATING_DEFICIT"
            interpretation = f"Expanded temporal discrimination window ({stdt_threshold_ms} ms, {ratio_to_norm}x predicted); mild cortical sensory blurring."
            guidance = "Central fatigue or local repetitive strain detected. Schedule 15 minutes of manual rest and gentle sensory finger exercises."
        else:
            tier = "MARKED_SENSORIMOTOR_INHIBITORY_DYSFUNCTION"
            interpretation = f"Severely elevated STDT ({stdt_threshold_ms} ms); significant deficit in basal ganglia-thalamocortical temporal gating."
            guidance = "Substantial loss of temporal discrimination. Recommend neurological movement disorder review."

        return {
            "mean_ascending_isi_ms": round(mean_asc, 1),
            "mean_descending_isi_ms": round(mean_desc, 1),
            "composite_stdt_ms": stdt_threshold_ms,
            "hysteresis_ms": hysteresis_ms,
            "predicted_age_norm_ms": predicted_norm_ms,
            "threshold_ratio_to_norm": ratio_to_norm,
            "somatosensory_gating_index": csgi_score,
            "clinical_tier": tier,
            "physiological_interpretation": interpretation,
            "actionable_guidance": guidance
        }
