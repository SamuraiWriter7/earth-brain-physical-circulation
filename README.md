# Earth Brain Physical Circulation

**Wind Circulation and Physical Infrastructure Architecture for Earth Brain OS**

This repository defines the physical circulation layer for **Earth Brain OS**.

It describes how local AI nodes can operate as sustainable physical organs by coordinating:

* compute load
* thermal flow
* airflow
* acoustic quietness
* cooling method
* power routing
* local memory
* network connection
* rest and recovery cycles

The goal is not simply to maximize computation.

The goal is to allow AI infrastructure to breathe.

---

## Concept

Earth Brain OS is not only an informational architecture.

To operate in the real world, it requires a physical body.

This repository treats hardware not as isolated devices, but as organs inside a civilizational operating system.

```text
Compute node
= breathing organ

Cooling system
= pressure regulation organ

Case / enclosure
= circulation chamber

Power path
= metabolic route

Network path
= nervous connection
```

In short:

> Earth Brain OS needs not only memory and events, but also breath, nerves, and circulation.

---

## Position in Earth Brain OS

This repository focuses on the lower physical infrastructure layers of Earth Brain OS.

```text
Human / Community Intent Layer
        ↓
Question / Resonance Layer
        ↓
Memory / Trace Layer
        ↓
Optical Nervous Layer
        ↓
Wind Circulation Layer
        ↓
Physical Compute Substrate
```

The current `v0.1.0-candidate` focuses mainly on the **Wind Circulation Layer**.

---

## Wind Circulation Layer

The **Wind Circulation Layer** regulates the physical breath of local AI nodes.

It coordinates:

* computation
* heat
* airflow
* sound
* vibration
* cooling
* power
* local stability
* rest

Its core principle is:

> quiet flow over forced output.

A wind-aware system does not only ask:

```text
Can this node compute?
```

It also asks:

```text
Can this node compute without damaging its own circulation?
```

---

## Organ Model

The Wind Circulation Layer describes physical infrastructure using an organ-based model.

| Organ                  | Meaning                                            |
| ---------------------- | -------------------------------------------------- |
| Compute Lung           | Local AI node that performs inference or reasoning |
| Cognitive Muscle       | High-intensity compute component                   |
| Silent Pressure Organ  | Quiet cooling or pressure regulation component     |
| Circulation Chamber    | Enclosure or internal airflow path                 |
| Power Meridian         | Energy delivery and stabilization path             |
| Stable Peripheral Cell | Low-power or battery-backed edge node              |

This model allows physical AI infrastructure to be described as a living circulation system rather than a collection of disconnected devices.

---

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── physical-circulation-overview.md
│   └── wind-circulation-layer.md
├── schemas/
│   └── wind-node.schema.json
├── examples/
│   └── wind-node.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate-examples.yml
```

---

## Key Documents

### `docs/physical-circulation-overview.md`

Overview of the Physical Circulation Layer.

It defines the relationship between:

* Wind Circulation Layer
* Optical Nervous Layer
* Physical Compute Substrate
* local AI nodes
* power, thermal, acoustic, and network circulation

### `docs/wind-circulation-layer.md`

Detailed specification of the Wind Circulation Layer.

It defines:

* wind-aware node behavior
* thermal regulation
* airflow coordination
* acoustic regulation
* compute rhythm
* power-compute synchronization
* rest and recovery
* Wind Node lifecycle states

---

## Schema

### `schemas/wind-node.schema.json`

JSON Schema for describing a **Wind Node**.

A Wind Node is a physical AI node described by:

* node identity
* compute class
* circulation role
* thermal profile
* airflow profile
* acoustic profile
* cooling method
* power path
* local memory link
* network link
* lifecycle state
* circulation policy

---

## Example

### `examples/wind-node.example.yaml`

Example Wind Node record.

It represents a local AI compute node that prefers:

* quiet operation
* local execution
* thermal stability
* acoustic awareness
* burst execution with cooldown
* escalation when strained

---

## Validation

This repository includes a Python validation script.

### Install dependencies

```bash
pip install jsonschema pyyaml
```

### Run validation

```bash
python scripts/validate_examples.py
```

Expected result:

```text
[result] All examples are valid
```

---

## GitHub Actions

The repository includes a validation workflow:

```text
.github/workflows/validate-examples.yml
```

It runs on:

* push to `main`
* pull request to `main`
* manual workflow dispatch

The workflow checks:

* Python syntax
* example YAML validation against JSON Schema

---

## Current Version

```text
v0.1.0-candidate
Physical Circulation Layer for Earth Brain OS
```

This version introduces:

* Physical Circulation overview
* Wind Circulation Layer documentation
* Wind Node JSON Schema
* Wind Node YAML example
* validation script
* GitHub Actions workflow

---

## Design Principles

### 1. Breath Before Maximum Output

The system should not maximize computation at the expense of circulation.

### 2. Quietness Is Structural Health

Noise is treated as a structural signal.

### 3. Heat Is a Governance Signal

Thermal load should influence routing, reasoning depth, and scheduling.

### 4. Power Is Metabolism

Power delivery is part of the system’s operating rhythm.

### 5. Rest Is a Valid State

A resting node is not a failed node.

It is a maintained node.

### 6. Locality Requires Circulation

Local AI is only sustainable if local nodes can physically breathe.

### 7. Airflow Is Architecture

The path of air belongs in the specification.

---

## Non-Goals

This repository does not define:

* a specific hardware product
* mandatory vendor implementations
* exact fan curves
* commercial cooling benchmarks
* complete mechanical engineering specifications
* a full data center HVAC standard
* a replacement for Earth Brain OS core schemas

Instead, it defines a structural vocabulary for describing physical circulation in AI civilization systems.

---

## Future Direction

Possible next versions may add:

* Optical Nervous Layer specification
* Optical Node schema
* Optical Node example
* Hybrid Wind/Optical Node model
* physical circulation outcome logs
* thermal-acoustic routing policies
* Earth Brain OS integration records

---

## Summary

Modern AI systems are often described by model size, token throughput, benchmark score, or cloud scale.

Physical Circulation Architecture adds another question:

> Can the system breathe?

A system that cannot breathe becomes hot, loud, expensive, centralized, and brittle.

A system that can breathe becomes quiet, local, modular, resilient, and sustainable.

Earth Brain OS is not only an intelligence architecture.

It is a body.

And every body needs circulation.

