# Red Team Lab Engineering

> **Special practice of the [Cloud Operations Engineering](https://github.com/CloudSec-Jay/cloud-ops-engineering) system.** Each project lives in its own repository and links back to the hub. [Portfolio site](https://cloudsec-jay.github.io/cloud-ops-engineering/) · [Project site](https://cloudsec-jay.github.io/red-team-lab-engineering/)

An authorized adversary-validation workspace for web applications, APIs, cloud identity, and transport security.

This repository consolidates useful material from the archived `cloud-security-engineer/appsec/` and `cloud-security-engineer/pentesting/` trees into a lab-first operating model. It does not claim production testing, completed exploitation, or validated detections without evidence.

## Operating model

Every lab moves through the same gated loop:

1. Define an owned target, authorization boundary, and stop conditions.
2. State the attack hypothesis and required telemetry.
3. Execute only inside the isolated lab boundary.
4. Preserve requests, responses, logs, and timestamps.
5. Record the finding, mitigation, and detection handoff.

Detection engineering remains in [`k8s-secops-platform`](https://github.com/CloudSec-Jay/k8s-secops-platform). This repository owns adversary emulation, evidence, and gap reports.

## Lab tracks

| Track | Source material | Current state |
|---|---|---|
| Web authentication | Existing Burp Suite authentication notes | Source notes; evidence not migrated |
| Web input handling | Existing DVWA/Juice Shop mission design | Scaffolded |
| API authorization | Archived REST, GraphQL, OAuth, and JWT inventory | Scaffolded; original API notes were empty |
| Cloud attack paths | Archived credential, IAM, lateral-movement, and exfiltration inventory | Scaffolded; original technique folders were empty |
| Transport trust | Existing isolated OpenSSL TLS/mTLS lab | Source lab; execution evidence pending |
| Purple-team handoff | Existing mission template and lab guide | Scaffolded and normalized |

See [`labs/catalog.json`](labs/catalog.json) for machine-readable status and [`methodology/engagement-standard.md`](methodology/engagement-standard.md) for the safety boundary.

## Repository map

```text
labs/                 Lab briefs grouped by attack surface
methodology/          Authorization and execution standard
templates/            Reusable lab, finding, and evidence templates
evidence/             Sanitized evidence contract (no secrets)
tools/                Catalog validation
docs/                 GitHub Pages case study
```

## Validate

```bash
python3 tools/validate_catalog.py
python3 -m unittest discover -s tools/tests -v
```

## Safety

Use only systems you own or are explicitly authorized to test. The scaffolds intentionally exclude live credentials, public targets, stealth instructions, persistence, and destructive actions.

## Source provenance

The archived source remains unchanged. [`SOURCE_MAP.md`](SOURCE_MAP.md) records what informed each track and where the source was incomplete or inconsistent.
