---

Document ID: OSEF-SPE-113
Title: Skill Specification
Version: 0.1.0
Status: Draft
Authority: Normative
Owner: OSEF Architecture Board
Classification: Public
Created: 2026-07-27
Last Updated: 2026-07-27
Related Documents:

* OSEF-SPE-101
* OSEF-SPE-108
* OSEF-SPE-109
* OSEF-SPE-110
* OSEF-SPE-111
* OSEF-SPE-112
* OSEF-SPE-114
* OSEF-ARC-001
* OSEF-MTM-001

---

# Skill Specification

## 1. Purpose

This specification defines the concept, structure, lifecycle, and governance rules for Skills within OSEF.

A Skill represents the smallest independently reusable functional unit in the OSEF engineering model.

Skills are the atomic building blocks used by Capabilities, Workflows, and Agents to perform work.

---

## 2. Definition

A Skill is a narrowly defined function that performs one coherent task within a system.

A Skill defines:

* what it does;
* what input it requires;
* what output it produces;
* what constraints it must follow;
* what tools it may use.

A Skill does not coordinate other skills.

A Skill does not orchestrate workflows.

A Skill does not make strategic decisions.

It executes a focused responsibility.

---

## 3. Position Within OSEF

The relationship between execution layers is:

```text id="n3kq51"
Agent

↓

Workflow

↓

Capability

↓

Skill

↓

Tool

↓

Resource
```

Each layer has a distinct responsibility.

Skills are the smallest reusable execution unit before tool interaction.

---

## 4. Skill Characteristics

Every Skill must be:

### Single-purpose

A Skill must solve one clearly defined problem.

---

### Reusable

A Skill should be reusable across multiple Capabilities or Workflows whenever practical.

---

### Traceable

Every Skill must reference:

* originating Capability;
* requirements;
* expected behavior;
* validation criteria.

---

### Observable

Skill execution should produce measurable output or evidence.

---

### Independent

A Skill must remain independent from other Skills.

It may be composed into larger units, but it must not depend on hidden orchestration logic.

---

## 5. Skill Structure

Every Skill specification should contain:

```yaml id="x1q8rt"
skill:
  id:
  name:
  purpose:
  version:

  description:

  input:

  output:

  tools:

  constraints:

  validations:

  metrics:
```

---

## 6. Skill Components

### 6.1 Identity

Every Skill must have:

* unique identifier;
* name;
* version;
* owner;
* purpose.

---

### 6.2 Purpose

Defines why the Skill exists.

Example:

"Classify financial transactions into categories."

---

### 6.3 Input

Defines the information required to execute the Skill.

Examples:

* text;
* data rows;
* documents;
* context;
* configuration.

---

### 6.4 Output

Defines the result produced by the Skill.

Examples:

* classified data;
* summary;
* report fragment;
* recommendation;
* transformed content.

---

### 6.5 Tools

A Skill may use one or more Tools to perform its function.

Tool usage must remain explicit and constrained.

---

### 6.6 Constraints

Defines what the Skill may and may not do.

Examples:

* allowed scope;
* allowed data types;
* security restrictions;
* context limitations;
* output boundaries.

---

## 7. Skill Lifecycle

Skills follow this lifecycle:

```text id="v8j3nl"
Draft

↓

Designed

↓

Reviewed

↓

Approved

↓

Implemented

↓

Validated

↓

Released

↓

Improved
```

---

## 8. Skill Design Rules

### Rule 1 — Skills Must Be Atomic

A Skill should represent a single functional concern.

If a Skill becomes too broad, it should be decomposed.

---

### Rule 2 — Skills Must Be Reusable

A Skill should be designed for repeated use in more than one context when appropriate.

---

### Rule 3 — Skills Must Remain Independent

A Skill should not directly control other Skills.

Skills may be composed by Capabilities or Workflows, not by hidden internal coupling.

---

### Rule 4 — Skills Must Be Traceable

Every Skill must trace back to a Capability or a specific engineering need.

---

### Rule 5 — Skills Must Respect Boundaries

A Skill must not exceed its defined scope.

If it requires additional behavior, a new Skill should be created.

---

## 9. Skill Validation

Every Skill must define validation criteria.

### Functional Validation

Verify that the Skill performs its intended task.

---

### Quality Validation

Verify:

* correctness;
* consistency;
* reliability;
* expected output format.

---

### Security Validation

Verify:

* permitted inputs;
* prohibited actions;
* data handling rules;
* tool access boundaries.

---

### Performance Validation

Measure:

* execution time;
* resource usage;
* scalability.

---

## 10. Skill Metrics

Recommended metrics:

* success rate;
* execution time;
* error rate;
* reuse frequency;
* output quality score;
* human intervention frequency;
* cost per execution.

---

## 11. Skill and Knowledge

Every Skill execution may generate knowledge.

Examples:

* successful patterns;
* common failures;
* parameter tuning;
* output improvements;
* validation results.

This knowledge should contribute to Engineering Memory when relevant.

---

## 12. Skill Example

Example:

```text id="p2w7rz"
Capability:

Expense Analysis


Skill:

Categorize Transactions


Purpose:

Assign transactions to predefined categories.


Input:

- transaction description
- amount
- merchant
- context


Output:

- transaction category


Tools:

- classification model
- rules engine


Constraints:

- do not change transaction amounts;
- do not infer unsupported categories;
- do not access unrelated private data.
```

---

## 13. Governance

Changes to critical Skills require:

* specification update;
* review;
* validation;
* version increment.

Skill behavior must remain aligned with the OSEF Specification, Governance Specification, and Security Specification.

---

## 14. Quality Criteria

A Skill is considered compliant with OSEF when:

* its purpose is clearly defined;
* it performs a single coherent function;
* it has traceable requirements;
* it uses approved tools;
* it has validation criteria;
* it produces observable results;
* it follows governance rules.

---

## 15. Evolution

Skill Specification will evolve as OSEF introduces:

* richer capability libraries;
* reusable AI behaviors;
* optimized functional units;
* standardized skill catalogs;
* domain-specific skill packs.

The objective is to provide a stable foundation for increasingly modular and reusable intelligent systems.
