# Authorized lab engagement standard

## Required before execution

- The target is locally owned or explicitly authorized.
- The target boundary, source host, test window, and operator are recorded.
- Required logs are enabled and their clocks are synchronized.
- Stop conditions and a recovery path are documented.
- Secrets and personal data are excluded from evidence.

## Lab lifecycle

### 1. Scope

Record the asset, test account, network boundary, allowed technique, exclusions, and teardown owner.

### 2. Hypothesis

Describe the control being tested and the observable behavior expected if it fails. Map the hypothesis to OWASP and MITRE only when the mapping is supported by the source material.

### 3. Execute

Use the minimum action necessary to validate the hypothesis. Stop when the success condition is reached, telemetry disappears, scope becomes uncertain, or the target behaves unexpectedly.

### 4. Observe

Capture sanitized request/response pairs, relevant application or cloud audit events, timestamps with timezone, and the operator's notes. Do not store tokens, cookies, private keys, or raw customer data.

### 5. Close

Record whether the control prevented, detected, or missed the behavior. Document remediation and send detection requirements or gaps to the SecOps repository.

## Status language

- `planned`: structured intent; no implementation or run is claimed.
- `source-notes`: substantive archived notes exist; evidence has not been migrated.
- `source-lab`: an archived lab design or scripts exist; current execution remains unverified.
- `executed`: a completed evidence manifest passes validation.
- `retired`: intentionally removed from the active lab program.
