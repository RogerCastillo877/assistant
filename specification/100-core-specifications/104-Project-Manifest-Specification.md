---
Document ID: OSEF-PMS-001
Title: Project Manifest Specification
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
  - OSEF-MAN-001
  - OSEF-CPR-001
  - OSEF-GOV-001
  - OSEF-ARC-001
  - OSEF-MTM-001
  - OSEF-ATM-001
---

# Project Manifest Specification

## 1. Purpose

The OSEF Project Manifest defines the canonical description of an OSEF project.

Every project compliant with the OSEF Specification shall contain exactly one Project Manifest.

The Project Manifest acts as the single entry point for engineering tools, validators, automation pipelines, and reference implementations.

It defines the engineering identity of a project independently of its implementation technology.

---

# 2. Objectives

The Project Manifest exists to:

- uniquely identify a project;
- declare compliance with a specific OSEF Specification version;
- define the engineering lifecycle adopted by the project;
- identify domains and missions;
- reference normative specifications;
- declare engineering assets;
- enable automated validation;
- support project bootstrapping.

---

# 3. Scope

The Project Manifest describes engineering metadata.

It does **not** describe implementation details such as:

- source code;
- business logic;
- algorithms;
- prompts;
- workflows.

Those artifacts are defined elsewhere.

---

# 4. File Name

The Project Manifest shall be stored at the project root using the following filename:

```text
osef.yaml
```

No alternative filenames are permitted.

---

# 5. File Format

The manifest shall use YAML 1.2 syntax.

UTF-8 encoding is mandatory.

Tabs are prohibited.

---

# 6. Required Sections

Every Project Manifest shall contain the following top-level sections.

```text
osef
project
organization
lifecycle
specifications
missions
domains
artifacts
knowledge
schemas
templates
quality
```

Additional sections may be introduced provided they do not conflict with this specification.

---

# 7. OSEF Section

The `osef` section identifies the specification implemented by the project.

Required fields:

- specification
- framework
- maturity

Optional fields:

- profile

Example:

```yaml
osef:
  specification: 1.0.0
  framework: Operating Systems Engineering Framework
  maturity: Foundation
  profile: default
```

---

# 8. Project Section

Defines the engineering identity of the project.

Required fields:

- id
- name
- version
- status
- type

Optional fields:

- description
- repository
- homepage

---

# 9. Organization Section

Identifies ownership.

Required:

- owner

Optional:

- organization
- contributors
- maintainers

---

# 10. Lifecycle Section

Declares the engineering lifecycle used by the project.

Typical fields:

- sdlc
- governance
- architecture

These values shall reference normative OSEF documents.

---

# 11. Specifications Section

Lists the normative documents adopted by the project.

Example:

```yaml
specifications:
  manifesto: OSEF-MAN-001
  vision: OSEF-VIS-001
  principles: OSEF-CPR-001
  governance: OSEF-GOV-001
```

---

# 12. Domains

Lists all domains implemented by the project.

Example:

```yaml
domains:
  - learning
  - finance
  - career
```

---

# 13. Missions

Lists the high-level missions supported by the project.

Every mission shall have a unique identifier.

---

# 14. Artifact Locations

Defines where engineering artifacts are stored.

Typical locations include:

- specifications
- ADR
- RFC
- decisions
- releases

---

# 15. Knowledge Locations

Defines where engineering knowledge is maintained.

Typical locations include:

- engineering memory
- lessons learned
- reusable patterns
- knowledge base

---

# 16. Quality Requirements

The manifest shall declare engineering quality policies.

Typical fields:

- semantic versioning
- traceability
- documentation required
- architecture review

---

# 17. Validation Rules

A valid Project Manifest shall satisfy the following conditions:

- required sections exist;
- required fields are present;
- identifiers are unique;
- referenced specifications exist;
- versions are valid;
- YAML syntax is valid;
- document references are resolvable.

---

# 18. Versioning

The Project Manifest follows Semantic Versioning.

Breaking changes require a MAJOR version increment.

---

# 19. Conformance

A project is considered OSEF compliant only if:

- it contains a valid Project Manifest;
- the manifest conforms to this specification;
- referenced specifications are available;
- mandatory engineering artifacts exist.

---

# 20. Future Evolution

Additional sections may be introduced by future versions of the OSEF Specification.

New sections shall preserve backward compatibility whenever practical.

---

# Informative Appendix A — Engineering Role

The Project Manifest is not a deployment descriptor.

It is an engineering descriptor.

Its primary purpose is to describe the engineering identity of a project, enabling governance, validation, automation, and traceability across the entire software lifecycle.