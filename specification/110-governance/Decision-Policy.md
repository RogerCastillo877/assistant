---
Document ID: OSEF-GOV-002
Title: Normative Decision Policy
Version: 0.1.0
Status: Draft
Authority: Normative
Owner: OSEF Architecture Board
Classification: Public
Created: 2026-07-27
Last Updated: 2026-07-27
Related Documents:
  - OSEF-SPE-101
  - OSEF-GOV-001
  - OSEF-CPR-001
---

# Normative Decision Policy

## 1. Purpose

This document establishes the default policy for resolving conflicts between OSEF principles and for determining when an implementation is considered compliant.

## 2. Priority of Principles

When principles conflict, the following order shall apply:

1. Safety, security, and legal obligations.
2. Human accountability and explainability.
3. Specification and conformance requirements.
4. Architecture and traceability.
5. Reuse, maintainability, and sustainability.

## 3. Compliance Expectations

A project shall be considered OSEF-compliant only when it:

- maintains a valid Project Manifest;
- preserves traceability between requirements, specifications, implementations, and validation evidence;
- follows the documented governance process;
- and passes the applicable runtime validators.

## 4. Exceptions

Exceptions to this policy shall be rare and shall be approved through the governance process.

Every exception shall:

- be recorded in an ADR or equivalent governance evidence file;
- state the rationale;
- define the scope and duration;
- and include a plan for remediation.

## 5. Normative Guidance

The runtime schemas, templates, validators, and project manifest shall be treated as the authoritative implementation contract for OSEF.
