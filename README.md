# genpark-agentic-commerce-customs-drawback-duty-refund-1313-calculator-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

US 19 U.S.C. 1313 unused merchandise and manufacturing duty drawback 99% refund recovery engine.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `calculate_customs_drawback_refund`
- **Category**: `agentic_commerce`

### Method Documentation
Calculate US Customs duty drawback refunds under 19 U.S.C. § 1313 (Unused Merchandise § 1313(j) and Manufacturing Drawback § 1313(a)).
Authorizes a 99% refund of import duties, Merchandise Processing Fees (MPF), and Harbor Maintenance Fees (HMF) for imported merchandise subsequently exported within 5 years.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "calculate_customs_drawback_refund",
    "arguments": {
    "import_entries": [
        {
            "entry_number": "CBP-981-1",
            "duties_paid": 45000.0,
            "mpf_paid": 575.35,
            "hmf_paid": 140.0,
            "elapsed_years_since_import": 1.5
        },
        {
            "entry_number": "CBP-981-2",
            "duties_paid": 28500.0,
            "mpf_paid": 450.0,
            "hmf_paid": 95.0,
            "elapsed_years_since_import": 2.1
        }
    ],
    "export_entries": [
        {
            "export_bill_of_lading": "MEDU918274",
            "exported_value": 110000.0
        }
    ],
    "drawback_type": "1313_J_UNUSED_MERCHANDISE"
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
