# Earth Brain Physical Circulation

**Wind Circulation and Optical Nervous Architecture for Earth Brain OS**

This repository defines the physical circulation layer for **Earth Brain OS**.

It describes how local AI nodes can operate as sustainable physical organs by coordinating:

* compute load
* thermal flow
* airflow
* acoustic quietness
* cooling method
* power routing
* local memory
* local-first networking
* optical nervous coordination
* rest and recovery cycles

The goal is not simply to maximize computation.

The goal is to allow AI infrastructure to breathe, connect, and sustain itself as a physical body.

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

Memory node
= memory nucleus

AI router
= local nervous ganglion
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

The current `v0.2.0-candidate` defines two major physical layers:

* **Wind Circulation Layer**
* **Optical Nervous Layer**

Together, these layers describe how Earth Brain OS can become a physically sustainable, local-first, distributed AI body.

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

## Optical Nervous Layer

The **Optical Nervous Layer** regulates signal flow between local AI nodes, routers, memory nodes, edge devices, and cloud interfaces.

It coordinates:

* node-to-node communication
* local-first routing
* low-latency communication
* memory access
* edge coordination
* task routing
* signal prioritization
* fallback routing
* cloud escalation
* nervous trace logging

Its core principle is:

> shortest suitable path over maximum data movement.

An optical-aware system does not only ask:

```text
Can this network transfer data?
```

It also asks:

```text
Should this data move at all?
```

and:

```text
Where is the nearest suitable intelligence?
```

The Optical Nervous Layer prevents Earth Brain OS from becoming unnecessarily centralized, noisy, expensive, and brittle.

---

## Relationship Between Wind and Optical Layers

The two layers are distinct but interdependent.

```text
Wind Circulation Layer
= internal breathing and physical stability

Optical Nervous Layer
= external connection and signal coordination
```

Wind answers:

```text
Can this node breathe?
```

Optical answers:

```text
Should the signal go there?
```

Together, they form the first physical body model of Earth Brain OS.

```text
Wind
= breath, heat, airflow, sound, power

Optical
= signal, memory, connection, routing, coordination
```

Without wind, intelligence overheats.

Without optical nerves, intelligence fragments.

Without local-first routing, intelligence becomes centralized, expensive, and brittle.

---

## Organ Model

This repository describes physical infrastructure using an organ-based model.

### Wind Organs

| Organ                  | Meaning                                            |
| ---------------------- | -------------------------------------------------- |
| Compute Lung           | Local AI node that performs inference or reasoning |
| Cognitive Muscle       | High-intensity compute component                   |
| Silent Pressure Organ  | Quiet cooling or pressure regulation component     |
| Circulation Chamber    | Enclosure or internal airflow path                 |
| Power Meridian         | Energy delivery and stabilization path             |
| Stable Peripheral Cell | Low-power or battery-backed edge node              |

### Optical Organs

| Organ                        | Meaning                                              |
| ---------------------------- | ---------------------------------------------------- |
| Local Nervous Ganglion       | AI router or local coordination node                 |
| Optical Nerve Bundle         | High-speed communication path                        |
| Memory Nucleus               | NAS, trace store, model cache, or shared memory node |
| Peripheral Intelligence Node | Edge-side sensing or inference node                  |
| Execution Organ              | Local AI compute node selected for task execution    |
| Cloud Interface Organ        | Gateway to external cloud infrastructure             |

This model allows AI infrastructure to be described as a living circulation and nervous system rather than a collection of disconnected devices.

---

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── physical-circulation-overview.md
│   ├── wind-circulation-layer.md
│   └── optical-nervous-layer.md
├── schemas/
│   ├── wind-node.schema.json
│   └── optical-node.schema.json
├── examples/
│   ├── wind-node.example.yaml
│   └── optical-node.example.yaml
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
* power, thermal, acoustic, memory, and network circulation

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

### `docs/optical-nervous-layer.md`

Detailed specification of the Optical Nervous Layer.

It defines:

* local-first routing
* optical nervous coordination
* node discovery
* signal prioritization
* memory access coordination
* task routing
* fallback and escalation
* nervous trace logging
* Optical Node lifecycle states

---

## Schemas

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

### `schemas/optical-node.schema.json`

JSON Schema for describing an **Optical Node**.

An Optical Node is a routing, memory, or coordination node described by:

* node identity
* nervous role
* connection profile
* latency profile
* bandwidth profile
* routing policy
* memory access
* Wind Node links
* fallback paths
* lifecycle state
* nervous trace policy

---

## Examples

### `examples/wind-node.example.yaml`

Example Wind Node record.

It represents a local AI compute node that prefers:

* quiet operation
* local execution
* thermal stability
* acoustic awareness
* burst execution with cooldown
* escalation when strained

### `examples/optical-node.example.yaml`

Example Optical Node record.

It represents a local AI router that coordinates nearby Wind Nodes through:

* local-first routing
* memory-near-compute preference
* Wind Circulation state awareness
* fallback routing
* cloud escalation only when needed
* nervous trace logging

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
* Wind Node example validation against JSON Schema
* Optical Node example validation against JSON Schema

---

## Current Version

```text
v0.2.0-candidate
Optical Nervous Architecture
```

This version introduces:

* Optical Nervous Layer documentation
* Optical Node JSON Schema
* Optical Node YAML example
* validation support for both Wind Node and Optical Node examples

It builds on:

```text
v0.1.0-candidate
Physical Circulation Layer for Earth Brain OS
```

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

### 8. Shortest Suitable Path

The system should prefer the nearest appropriate route, not the largest route.

### 9. Local First, Not Local Only

Local nodes should be preferred when sustainable, but escalation remains possible.

### 10. Every Route Leaves a Trace

Routing decisions should be observable, traceable, and learnable.

---

## Non-Goals

This repository does not define:

* a specific hardware product
* mandatory vendor implementations
* exact fan curves
* commercial cooling benchmarks
* complete mechanical engineering specifications
* a full data center HVAC standard
* complete telecom standards
* a replacement for existing internet protocols
* a replacement for Earth Brain OS core schemas

Instead, it defines a structural vocabulary for describing physical circulation and optical nervous coordination in AI civilization systems.

---

## Future Direction

Possible next versions may add:

* Hybrid Wind/Optical Node model
* circulation outcome logs
* nervous routing outcome logs
* thermal-acoustic routing policies
* breathing reasoning node profiles
* Earth Brain OS integration records
* physical circulation event schemas

---

## Summary

Modern AI systems are often described by model size, token throughput, benchmark score, or cloud scale.

Physical Circulation Architecture adds another question:

> Can the system breathe?

Optical Nervous Architecture adds one more:

> Can the system coordinate without unnecessary centralization?

A system that cannot breathe becomes hot, loud, expensive, centralized, and brittle.

A system that can breathe and coordinate becomes quiet, local, modular, resilient, and sustainable.

Earth Brain OS is not only an intelligence architecture.

It is a body.

And every body needs circulation and nerves.
