---
Document ID: OSEF-VER-001
Title: Versioning Specification
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
  - OSEF-DID-001
  - OSEF-GOV-001
---
# Versioning Specification

## 1. Purpose

This specification defines the official versioning model used throughout the Operating Systems Engineering Framework (OSEF).

Its purpose is to ensure consistent identification, evolution, compatibility, and lifecycle management of every engineering artifact produced within the framework.

Versioning is considered an engineering activity rather than an administrative task.

---

# 2. Scope

This specification applies to:

- Framework releases
- Specifications
- Documents
- Schemas
- Templates
- Reference implementations
- Runtime components
- Tooling
- Configuration files

Every versioned artifact shall comply with the rules defined in this document.

---

# 3. Versioned Artifacts

OSEF distinguishes multiple categories of versioned artifacts.

| Artifact | Example |
|----------|----------|
| Framework | OSEF |
| Specification | Architecture Specification |
| Document | Architecture.md |
| Schema | project.schema.json |
| Template | capability-template.md |
| Runtime | osef CLI |
| Reference Implementation | Personal OS |
| Extension | Plugin |

Each category evolves independently.

---

# 4. Semantic Versioning

OSEF adopts Semantic Versioning (SemVer):

```
MAJOR.MINOR.PATCH
```

Example:

```
2.4.1
```

---

## 4.1 Major Version

Incremented when introducing incompatible changes.

Examples:

- Breaking architectural changes
- Removal of public specifications
- Incompatible schema modifications

Example:

```
1.0.0 → 2.0.0
```

---

## 4.2 Minor Version

Incremented when introducing backward-compatible capabilities.

Examples:

- New engineering specifications
- Additional artifact types
- New governance mechanisms
- New lifecycle phases

Example:

```
1.2.0 → 1.3.0
```

---

## 4.3 Patch Version

Incremented for compatible corrections.

Examples:

- Editorial improvements
- Typographical corrections
- Clarifications
- Reference updates

Example:

```
1.3.2 → 1.3.3
```

---

# 5. Specification Version vs Document Revision

OSEF distinguishes between engineering evolution and editorial evolution.

Every specification should define two independent identifiers.

Example:

```
Specification Version: 1.2.0
Document Revision: 7
```

## Specification Version

Represents the engineering version of the specification.

It changes only when the normative content changes.

Examples:

- New requirements
- Modified behavior
- New engineering rules
- Compatibility changes

---

## Document Revision

Represents the editorial history of the document.

It increases whenever any modification is made, including:

- Grammar corrections
- Formatting improvements
- Updated references
- Improved explanations
- Editorial restructuring

Example:

```
Specification Version: 1.2.0

Revision 1
Revision 2
Revision 3
Revision 4
```

The specification remains version 1.2.0 while the revision number continues to evolve.

---

# 6. Framework Version

The OSEF Framework has its own version independent from individual documents.

Example:

```
OSEF Framework

Version 1.0.0
```

Framework releases represent coherent sets of compatible specifications.

---

# 7. Document Version

Every document evolves independently.

Example:

```
Architecture

1.0.0

↓

1.1.0

↓

1.2.0

↓

2.0.0
```

Not every document changes in every framework release.

---

# 8. Runtime Version

Executable components maintain independent versions.

Examples:

- osef CLI
- Validator
- Documentation Generator
- Project Bootstrap

---

# 9. Reference Implementation Version

Projects built with OSEF define their own versions.

Examples:

```
Personal OS

2.1.0
```

```
Marketing OS

0.8.4
```

Reference implementations are versioned independently from the framework.

---

# 10. Compatibility

Compatibility is evaluated at the specification level.

Example:

| OSEF Version | Compatible Specification Version |
|--------------|----------------------------------|
| 1.x | 1.x |
| 2.x | 2.x |

Backward compatibility should be preserved whenever practical.

Breaking compatibility requires a Major Version increment.

---

# 11. Lifecycle Status

Version numbers are complemented by lifecycle status.

| Status | Meaning |
|---------|---------|
| Draft | Under active development |
| Review | Pending approval |
| Approved | Accepted |
| Stable | Recommended for production |
| Deprecated | Scheduled for removal |
| Archived | No longer maintained |

Version and status are independent.

---

# 12. Change Classification

Changes are classified according to their engineering impact.

| Change | Version Increment |
|---------|-------------------|
| Editorial correction | PATCH |
| Clarification | PATCH |
| New informative appendix | PATCH |
| New section | MINOR |
| New engineering rule | MINOR |
| New specification | MINOR |
| Breaking architectural change | MAJOR |
| Removed specification | MAJOR |

---

# 13. Release Process

Every official release follows the governance process.

```
Proposal
      ↓
RFC
      ↓
Review
      ↓
Approval
      ↓
Release Candidate
      ↓
Stable Release
```

No version may be released without completing the governance workflow.

---

# 14. Version Matrix

OSEF components evolve independently while maintaining compatibility.

| Component | Example Version |
|-----------|-----------------|
| OSEF Framework | 1.0.0 |
| Architecture Specification | 1.1.0 |
| Governance Specification | 1.0.0 |
| Artifact Model | 1.2.0 |
| CLI | 0.6.0 |
| Validator | 0.4.0 |
| Project Manifest Schema | 1.0.0 |

---

# 15. Engineering Principles

Versioning within OSEF follows the following principles.

- Every engineering artifact shall be versioned.
- Version numbers shall be meaningful.
- Compatibility shall be explicit.
- Breaking changes shall be documented.
- Every release shall be traceable.
- Editorial changes shall be distinguishable from normative changes.
- Version history shall never be lost.

---

# 16. Conformance

Any implementation claiming compliance with OSEF shall follow the versioning rules defined in this specification.

Alternative versioning strategies may be used internally, provided that externally exposed artifacts remain compliant with this specification.