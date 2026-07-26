---
Document ID: OSEF-DID-001
Title: Document ID Specification
Version: 1.0.0
Status: Draft
Authority: Normative
Owner: OSEF Architecture Board
Classification: Public
Created: 2026-07-26
Last Updated: 2026-07-26
Next Review: TBD

Related Documents:
  - OSEF-SPE-001
  - OSEF-PMS-001
  - OSEF-GOV-001
---

# Document ID Specification

## 1. Purpose

This specification defines the official identification system for all engineering artifacts within the Operating Systems Engineering Framework (OSEF).

Document identifiers provide a stable, unique, and machine-readable mechanism for referencing specifications, governance artifacts, schemas, templates, and other engineering assets.

The identifier remains permanent even if the document title, filename, or storage location changes.

---

# 2. Scope

This specification applies to every normative and informative artifact produced under OSEF.

This includes, but is not limited to:

- Specifications
- Governance documents
- RFCs
- ADRs
- Templates
- Schemas
- Reference implementations
- Validation reports
- Engineering guides

---

# 3. Objectives

The Document ID system is designed to:

- Ensure uniqueness.
- Enable traceability.
- Support automated tooling.
- Simplify cross-referencing.
- Preserve long-term stability.
- Decouple document identity from filenames.

---

# 4. Identifier Structure

Every document identifier shall follow the format:

```
OSEF-<TYPE>-<NUMBER>
```

Example:

```
OSEF-ARC-001
```

Where:

| Element | Description |
|----------|-------------|
| OSEF | Framework identifier |
| TYPE | Artifact type code |
| NUMBER | Sequential identifier |

---

# 5. Type Codes

The following type codes are reserved.

| Code | Document |
|------|-------------------------------|
| MAN | Manifesto |
| VIS | Vision |
| CPR | Core Principles |
| CHA | Project Charter |
| GOV | Governance |
| ARC | Architecture |
| SDL | Software Development Lifecycle |
| MTM | Meta Model |
| ATM | Artifact Model |
| BLU | Blueprint |
| GLS | Glossary |
| RDM | Roadmap |
| PMS | Project Manifest Specification |
| SPE | OSEF Specification |
| DID | Document ID Specification |
| VER | Versioning Specification |
| DIR | Directory Specification |
| RFC | RFC Specification |
| ADR | ADR Specification |
| SCH | Schema Specification |
| TMP | Template Specification |
| CLI | CLI Specification |

Additional codes may be introduced through the governance process.

---

# 6. Numbering Rules

Each document type maintains an independent sequence.

Examples:

```
OSEF-ARC-001
OSEF-ARC-002
OSEF-ARC-003

OSEF-RFC-001
OSEF-RFC-002

OSEF-ADR-001
OSEF-ADR-002
```

Numbers shall never be reused.

Deprecated identifiers remain permanently reserved.

---

# 7. Identifier Lifecycle

A Document ID progresses through the following lifecycle.

```
Reserved
      ↓
Assigned
      ↓
Published
      ↓
Deprecated
      ↓
Archived
```

Once assigned, an identifier shall never be reassigned to another artifact.

---

# 8. Filename Independence

Document identifiers are independent of filenames.

Example:

```
Filename:
Architecture.md

Document ID:
OSEF-ARC-001
```

Renaming or relocating a file shall not modify its identifier.

---

# 9. Cross-References

Documents shall reference other artifacts using their Document IDs.

Example:

```yaml
Related Documents:
  - OSEF-ARC-001
  - OSEF-GOV-001
  - OSEF-SDL-001
```

References should remain valid regardless of file organization.

---

# 10. Reserved Prefixes

The following prefixes are reserved exclusively for OSEF.

```
OSEF
```

Extensions should define their own namespace.

Example:

```
MOS-ARC-001
POS-CAP-004
```

This prevents collisions between the framework and projects built upon it.

---

# 11. Domain Extensions

Projects adopting OSEF should maintain their own identifier namespace.

Examples:

```
POS-REQ-001
POS-AGT-001
POS-WFL-003

MOS-REQ-001
MOS-CAP-005
MOS-SKL-012
```

The OSEF namespace remains reserved for framework-level artifacts.

---

# 12. Validation Rules

A valid Document ID shall satisfy the following constraints:

- Use uppercase letters.
- Begin with the framework namespace.
- Include a registered type code.
- End with a three-digit sequential number.
- Be globally unique within its namespace.

---

# 13. Examples

Framework documents

```
OSEF-MAN-001
OSEF-ARC-001
OSEF-SDL-001
OSEF-SPE-001
```

Project documents

```
POS-REQ-001
POS-CAP-004
MOS-WFL-002
```

---

# 14. Compatibility

Document IDs are immutable.

Changing the title, version, owner, status, or location of a document shall not change its identifier.

Only creating a new engineering artifact results in a new Document ID.

---

# 15. Governance

New document type codes shall only be introduced through the OSEF Governance process.

The Governance Specification defines the approval workflow for extending this registry.

---

# Informative Appendix A — Naming Examples

| Filename | Document ID |
|----------|-------------|
| Manifesto.md | OSEF-MAN-001 |
| Architecture.md | OSEF-ARC-001 |
| SDLC.md | OSEF-SDL-001 |
| Governance.md | OSEF-GOV-001 |
| OSEF Specification.md | OSEF-SPE-001 |

---

# Informative Appendix B — Design Principles

The Document ID system follows five principles:

- Stable over time.
- Human-readable.
- Machine-readable.
- Globally unique.
- Independent of implementation.

These principles ensure that engineering artifacts remain consistently identifiable throughout the lifecycle of the framework.