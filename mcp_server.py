"""
MCP Server for Somatosensory Temporal Discrimination Threshold (STDT) & Gating.
Exposes JSON-RPC endpoints for computing STDT thresholds and cortical sensory gating indices.
"""

import json
import sys
from client import SomatosensoryTemporalDiscriminationClient

client = SomatosensoryTemporalDiscriminationClient()


def handle_request(request: dict) -> dict:
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_stdt_staircase",
                        "description": "Calculates Somatosensory Temporal Discrimination Threshold (STDT in ms), age-adjusted ratio, and Cortical Somatosensory Gating Index from tactile inter-stimulus interval trials.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "ascending_isi_trials_ms": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Ascending staircase intervals in ms where 1 pulse transitioned to 2 distinct pulses"
                                },
                                "descending_isi_trials_ms": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Descending staircase intervals in ms where 2 pulses fused into 1 pulse"
                                },
                                "reference_age_years": {
                                    "type": "number",
                                    "default": 35.0,
                                    "description": "Subject age in years for normative adjustment"
                                }
                            },
                            "required": ["ascending_isi_trials_ms", "descending_isi_trials_ms"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "evaluate_stdt_staircase":
            res = client.evaluate_stdt_staircase(
                ascending_isi_trials_ms=args.get("ascending_isi_trials_ms", []),
                descending_isi_trials_ms=args.get("descending_isi_trials_ms", []),
                reference_age_years=args.get("reference_age_years", 35.0)
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32600, "message": "Invalid Request"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
