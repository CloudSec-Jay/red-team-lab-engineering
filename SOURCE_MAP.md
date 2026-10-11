# Source map

This project extracts structure and facts from the archived `cloud-security-engineer` repository without presenting empty folders or planning notes as completed work.

| New location | Archived source | Treatment |
|---|---|---|
| `labs/web/` | `appsec/README.md`, `appsec/burp-suite/server-side/authentication.md` | Authentication notes retained as source context; other empty Burp notes become candidate lab classes only |
| `labs/api/` | `appsec/README.md`, `appsec/api-security/` | REST, GraphQL, OAuth, JWT, and API-key themes retained; `notes.md` and implementation folders were empty, so all API labs remain planned |
| `labs/cloud/` | `pentesting/README.md`, `pentesting/cloud-attack/` | Technique inventory retained; original technique folders contained placeholders only |
| `labs/transport/` | `appsec/tls-mtls/openssl-lab/openssl.md` | Isolated three-host topology and trust-validation intent retained; evidence still required |
| `templates/` | `pentesting/purple-team/missions/MISSION_TEMPLATE.md` | Normalized around authorization, evidence, and detection handoff |
| `methodology/` | `pentesting/purple-team/README.md`, `docs/LAB_GUIDE.md` | Attack-to-detection loop retained without carrying forward conflicting example rule IDs |

## Deliberate exclusions

- Empty technique files are not copied.
- Example payloads are not treated as proof of execution.
- Conflicting Wazuh rule identifiers in the archived planning documents are not repeated.
- Detection rules are not duplicated; SecOps remains their owner.
- No credentials, scans, packet captures, or target-specific evidence are migrated.
