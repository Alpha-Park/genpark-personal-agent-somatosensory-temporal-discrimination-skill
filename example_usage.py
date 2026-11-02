"""
Example usage for Somatosensory Temporal Discrimination Threshold (STDT) Skill.
Demonstrates analyzing cutaneous inter-stimulus interval (ISI) staircase trials.
"""

from client import SomatosensoryTemporalDiscriminationClient


def main():
    client = SomatosensoryTemporalDiscriminationClient()

    print("=== 1. Evaluating STDT Staircase Test (Age 32, Healthy Adult) ===")
    asc_isi = [45.0, 50.0, 48.0]
    desc_isi = [52.0, 48.0, 50.0]

    res = client.evaluate_stdt_staircase(
        ascending_isi_trials_ms=asc_isi,
        descending_isi_trials_ms=desc_isi,
        reference_age_years=32.0
    )

    print(f"Mean Ascending ISI: {res['mean_ascending_isi_ms']} ms | Mean Descending ISI: {res['mean_descending_isi_ms']} ms")
    print(f"Composite STDT: {res['composite_stdt_ms']} ms (Predicted Age Norm: {res['predicted_age_norm_ms']} ms)")
    print(f"Ratio to Norm: {res['threshold_ratio_to_norm']}x")
    print(f"Somatosensory Gating Index: {res['somatosensory_gating_index']} / 100")
    print(f"Clinical Tier: {res['clinical_tier']}")
    print(f"Interpretation: {res['physiological_interpretation']}")
    print(f"Guidance: {res['actionable_guidance']}")


if __name__ == "__main__":
    main()
