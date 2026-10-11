# Cloud attack-path labs

The archived pentesting inventory identified credential access, IAM privilege escalation, cross-account movement, and storage exfiltration as intended AWS lab areas. The corresponding technique directories contained placeholders rather than executable labs.

This track will model those paths using disposable sandbox identities and synthetic data. Each lab must state:

- starting permissions;
- prohibited actions;
- expected CloudTrail events;
- guardrail or detection under evaluation;
- cleanup and credential revocation steps.

Production accounts, real data, persistence, and destructive actions are out of scope.
