# Final Report: Network Traffic Analysis: Suspicious DNS Activity

## Executive Summary

A network analysis project using synthetic DNS and HTTP evidence to identify suspicious domain patterns, possible command-and-control behavior, and recommended detection improvements.

The main purpose of this project is to demonstrate practical cybersecurity judgment. The project uses synthetic data and a realistic small-business scenario to show how security work should be documented: scope, evidence, findings, impact, and recommendations.

## Scope

- Environment: Synthetic small-business environment
- Data classification: Public-safe simulated data
- Objective: Identify security risks and produce actionable recommendations
- Out of scope: Real client data, exploitation, malware execution, unauthorized scanning

## Methodology

1. Reviewed the scenario and defined the security objective.
2. Examined the provided synthetic data.
3. Identified findings and assigned practical severity.
4. Documented impact in plain business language.
5. Recommended remediation steps.
6. Summarized how the work maps to entry-level cybersecurity responsibilities.

## Findings

### Finding 1: High volume of DNS queries to random subdomains

- **Severity / Type:** High
- **Impact:** Possible domain generation algorithm or beaconing behavior.
- **Recommended Action:** Validate the issue, assign an owner, prioritize based on business impact, document remediation, and retest.

### Finding 2: Repeated HTTP connections to newly observed domain

- **Severity / Type:** High
- **Impact:** Potential command-and-control callback.
- **Recommended Action:** Validate the issue, assign an owner, prioritize based on business impact, document remediation, and retest.

### Finding 3: User workstation had outdated browser plugin

- **Severity / Type:** Medium
- **Impact:** Likely initial infection or unwanted software vector.
- **Recommended Action:** Validate the issue, assign an owner, prioritize based on business impact, document remediation, and retest.

### Finding 4: No DNS sinkhole or egress filtering in place

- **Severity / Type:** Medium
- **Impact:** Weak prevention and containment capability.
- **Recommended Action:** Validate the issue, assign an owner, prioritize based on business impact, document remediation, and retest.

### Finding 5: Asset owner field missing in inventory

- **Severity / Type:** Low
- **Impact:** Delayed user/device follow-up.
- **Recommended Action:** Validate the issue, assign an owner, prioritize based on business impact, document remediation, and retest.

## Recommendations

- Prioritize high-impact issues first.
- Assign each finding to a clear owner.
- Track remediation status.
- Retest after changes are made.
- Keep documentation concise enough for business stakeholders and detailed enough for technical follow-up.

## What This Demonstrates to Employers

This project shows that I can look at network behavior, not just individual alerts. I can explain why repeated DNS lookups and unusual domains matter and how defenders can reduce risk.

## Resume Bullet Option

Built a cybersecurity portfolio project simulating network traffic analysis: suspicious dns activity, documenting scope, evidence, findings, risk impact, and remediation recommendations using public-safe synthetic data.
