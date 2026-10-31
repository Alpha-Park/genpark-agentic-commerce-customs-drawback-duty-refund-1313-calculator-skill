# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-customs-drawback-duty-refund-1313-calculator-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def calculate_customs_drawback_refund(import_entries, export_entries, drawback_type="1313_J_UNUSED_MERCHANDISE"):
    total_customs_duties_paid = sum(e.get("duties_paid", 0.0) for e in import_entries)
    total_mpf_paid = sum(e.get("mpf_paid", 0.0) for e in import_entries)
    total_hmf_paid = sum(e.get("hmf_paid", 0.0) for e in import_entries)
    
    total_eligible_base = total_customs_duties_paid + total_mpf_paid + total_hmf_paid
    
    # Statutory drawback rate is strictly 99% (CBP retains 1%)
    statutory_refund_rate = 0.99
    recoverable_refund = total_eligible_base * statutory_refund_rate
    cbp_retained_fee = total_eligible_base * 0.01
    
    # 5-year statutory filing window verification (from import date to drawback filing)
    all_within_window = all(e.get("elapsed_years_since_import", 1.0) <= 5.0 for e in import_entries)
    
    return {
        "drawback_statutory_basis": drawback_type,
        "total_customs_tariffs_paid_usd": round(total_customs_duties_paid, 2),
        "total_mpf_fees_paid_usd": round(total_mpf_paid, 2),
        "total_hmf_fees_paid_usd": round(total_hmf_paid, 2),
        "total_duty_drawback_eligible_base_usd": round(total_eligible_base, 2),
        "net_recoverable_refund_99pct_usd": round(recoverable_refund, 2),
        "cbp_retained_1pct_fee_usd": round(cbp_retained_fee, 2),
        "timely_5_year_filing_compliance": all_within_window,
        "action_required": "File CBP Form 7551 Drawback Entry with Automated Commercial Environment (ACE)."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "calculate_customs_drawback_refund",
                        "description": """Calculate US Customs duty drawback refunds under 19 U.S.C. § 1313 (Unused Merchandise § 1313(j) and Manufacturing Drawback § 1313(a)).
Authorizes a 99% refund of import duties, Merchandise Processing Fees (MPF), and Harbor Maintenance Fees (HMF) for imported merchandise subsequently exported within 5 years.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = calculate_customs_drawback_refund(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'import_entries': [{'entry_number': 'CBP-981-1', 'duties_paid': 45000.0, 'mpf_paid': 575.35, 'hmf_paid': 140.0, 'elapsed_years_since_import': 1.5}, {'entry_number': 'CBP-981-2', 'duties_paid': 28500.0, 'mpf_paid': 450.0, 'hmf_paid': 95.0, 'elapsed_years_since_import': 2.1}], 'export_entries': [{'export_bill_of_lading': 'MEDU918274', 'exported_value': 110000.0}], 'drawback_type': '1313_J_UNUSED_MERCHANDISE'}
        out = calculate_customs_drawback_refund(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
