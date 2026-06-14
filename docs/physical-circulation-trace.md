# Physical Circulation Trace

## Purpose

The **Physical Circulation Trace** defines how Earth Brain OS records the actual behavior of its physical circulation body.

Previous releases defined physical node models:

```text
Wind Node
= internal breathing and physical stability

Optical Node
= external connection and signal coordination

Hybrid Node
= integrated execution, circulation, routing, memory, fallback, and recovery
```

The Physical Circulation Trace records what happens when those nodes operate.

It captures:

* task execution
* thermal change
* acoustic change
* power change
* routing decisions
* memory access
* fallback behavior
* cloud escalation
* rest and recovery
* final outcome

In short:

> Physical Circulation Trace is the operational memory of the Earth Brain OS physical body.

---

## Definition

A **Physical Circulation Trace** is a structured record of a physical node event.

It describes how a Wind Node, Optical Node, or Hybrid Node changed state while handling a task, signal, route, memory request, fallback event, or recovery cycle.

It answers questions such as:

```text
What happened?
Which node was involved?
Was the node physically stable?
Was the route local or remote?
Was memory accessed nearby?
Was fallback used?
Was cloud escalation required?
Did the node need rest afterward?
What should the system learn from this event?
```

The trace does not replace the node schemas.

Instead, it records the behavior of nodes after they are used.

---

## Position in Physical Circulation Architecture

The Physical Circulation Trace sits between the physical node layers and the Memory / Trace Layer.

```text
Memory / Trace Layer
        ↑
Physical Circulation Trace
        ↑
Hybrid Wind/Optical Node
        ↑
Optical Nervous Layer
        ↑
Wind Circulation Layer
        ↑
Physical Compute Substrate
```

The node schemas define what a node is.

The trace schema defines what a node did.

---

## Core Principle

The core principle of the Physical Circulation Trace is:

> every physical decision leaves a recoverable trace.

A physical AI system should not only complete tasks.

It should remember how those tasks affected:

* heat
* airflow
* sound
* power
* routing
* memory
* fallback
* rest

This makes future execution more stable.

---

## Why Physical Traces Matter

A local AI system may appear successful if it completes a task.

But physical circulation asks deeper questions:

```text
Did the node overheat?
Did acoustic pressure rise?
Was local execution worth it?
Was cloud escalation avoidable?
Was memory too far away?
Did routing create congestion?
Was fallback used too late?
Should this node rest before the next task?
```

Without traces, Earth Brain OS cannot learn from physical operation.

With traces, the system can improve routing, workload depth, rest cycles, and local-first behavior.

---

## Trace Types

A Physical Circulation Trace may represent one of several trace types.

```text
wind_circulation_outcome
optical_routing_outcome
hybrid_execution_outcome
fallback_escalation
rest_recovery
```

---

## 1. Wind Circulation Outcome

A **Wind Circulation Outcome** records how a physical node responded internally to computation.

It may include:

* start lifecycle state
* end lifecycle state
* thermal change
* acoustic change
* power change
* airflow state
* cooling action
* rest requirement
* local execution result

Example questions:

```text
Did local execution increase heat?
Did the acoustic state remain quiet?
Was cooldown required?
Did power remain stable?
```

---

## 2. Optical Routing Outcome

An **Optical Routing Outcome** records how a task, signal, or memory request moved through the local nervous system.

It may include:

* source node
* destination node
* selected route
* alternative routes
* latency class
* bandwidth class
* memory path
* fallback path
* cloud escalation
* route outcome

Example questions:

```text
Was the nearest suitable route used?
Was data movement necessary?
Was memory accessed locally?
Was cloud escalation justified?
```

---

## 3. Hybrid Execution Outcome

A **Hybrid Execution Outcome** records a combined local execution and routing event.

It may include:

* local execution decision
* Wind state considered
* Optical route considered
* memory proximity
* fallback decision
* cloud escalation decision
* rest requirement
* final outcome

Example questions:

```text
Did the Hybrid Node execute locally?
Did it reroute because of circulation stress?
Did it reduce task depth?
Did it preserve local-first behavior?
```

---

## 4. Fallback Escalation

A **Fallback Escalation** trace records when the preferred route or node could not be used.

Fallback may occur because of:

* thermal strain
* acoustic pressure
* power instability
* network congestion
* memory unavailability
* local compute insufficiency
* governance boundary
* cloud-required operation

Example questions:

```text
Why was fallback used?
Was the fallback local, edge, remote, or human-reviewed?
Could the original route be improved later?
```

---

## 5. Rest Recovery

A **Rest Recovery** trace records when a node enters cooldown, resting, or degraded mode.

It may include:

* rest trigger
* previous workload
* recovery action
* expected availability
* future routing recommendation

Example questions:

```text
Why did the node rest?
Was rest caused by heat, sound, power, or routing load?
Should future tasks avoid this pattern?
```

---

## Trace Profile

A Physical Circulation Trace should be described using a structured profile.

Minimum fields may include:

```text
schema_version
trace_id
trace_type
source_node_id
target_node_id
task_id
start_state
end_state
wind_state
optical_route
memory_path
fallback_used
cloud_escalated
thermal_change
acoustic_change
power_change
rest_required
outcome
notes
```

These fields allow Earth Brain OS to treat physical operation as learnable experience.

---

## Example Physical Circulation Trace

```yaml
schema_version: "0.4.0"

trace_id: "pct-2026-001"
trace_type: "hybrid_execution_outcome"

source_node_id: "hybrid-ai-workstation-01"
target_node_id: "hybrid-ai-workstation-01"
task_id: "task-2026-physical-001"

start_state: "available"
end_state: "cooling"

wind_state:
  thermal_change: "moderate_increase"
  acoustic_change: "low"
  power_change: "stable"
  rest_required: true

optical_route:
  selected_route: "local_execution"
  fallback_used: false
  cloud_escalated: false

memory_path:
  memory_node_id: "nas-memory-01"
  memory_role: "coordination_memory"
  remote_memory_used: false

outcome: "local_execution_completed"

notes:
  - "Task was executed locally with nearby memory access."
  - "Cooldown recommended before another burst reasoning task."
```

---

## Physical Decision Learning

Physical Circulation Traces should support future decisions.

A trace may be used to learn:

* which nodes overheat under specific task types
* which routes remain stable
* which memory paths are efficient
* which fallback paths are useful
* when cloud escalation is justified
* when local-first execution is sustainable
* when rest prevents degradation

This allows Earth Brain OS to evolve from static node descriptions into adaptive physical operation.

---

## Relationship with Wind Node

Wind Node schemas define the physical properties of a node.

Physical Circulation Trace records how those properties changed during operation.

```text
Wind Node:
This node can perform local inference.

Physical Circulation Trace:
This node performed local inference and required cooldown afterward.
```

The trace turns node capacity into observed history.

---

## Relationship with Optical Node

Optical Node schemas define routing and nervous coordination capabilities.

Physical Circulation Trace records which routes were actually used.

```text
Optical Node:
This node prefers local-first routing.

Physical Circulation Trace:
This route was selected, fallback was not used, and cloud escalation was avoided.
```

The trace turns routing policy into routing memory.

---

## Relationship with Hybrid Node

Hybrid Node schemas define integrated execution and routing behavior.

Physical Circulation Trace records the combined outcome.

```text
Hybrid Node:
This node can execute locally and coordinate nearby nodes.

Physical Circulation Trace:
This node executed locally, used nearby memory, entered cooling, and did not escalate to cloud.
```

The trace turns hybrid capability into operational evidence.

---

## Relationship with Memory / Trace Layer

The Physical Circulation Trace should be stored in the Memory / Trace Layer.

This allows Earth Brain OS to remember:

* physical stress patterns
* routing patterns
* local-first success cases
* escalation reasons
* rest and recovery cycles
* node reliability
* circulation efficiency

This creates a feedback loop:

```text
Node operates
    ↓
Physical Circulation Trace is recorded
    ↓
Memory / Trace Layer stores the record
    ↓
Future routing and execution decisions improve
```

---

## Relationship with Earth Brain OS Core

Earth Brain OS Core may generate tasks, reasoning events, governance checks, memory requests, or agent actions.

The Physical Circulation Trace records how the physical body handled those events.

This allows the core system to ask:

```text
Which physical path was used?
Was local execution sustainable?
Was cloud escalation necessary?
Did the system need rest?
Should future tasks be routed differently?
```

The core remains abstract.

The trace records physical reality.

---

## Design Principles

### 1. Trace Physical Consequences

A successful task may still produce heat, noise, or power stress.

Those consequences should be recorded.

### 2. Make Escalation Visible

Cloud escalation, fallback routing, and human review should not be invisible.

They should leave traces.

### 3. Rest Is Evidence

Rest and cooldown are not failures.

They are useful physical signals.

### 4. Local-First Must Be Verified

A system should not only claim local-first behavior.

It should record when local-first execution actually happened.

### 5. Memory Path Matters

The location of memory affects cost, latency, privacy, and stability.

Memory paths should be traceable.

### 6. Physical State Should Inform Future Routing

Thermal, acoustic, power, and network outcomes should improve future decisions.

### 7. Every Body Learns Through History

A body without memory repeats stress.

A body with traces learns how to move.

---

## Non-Goals

The Physical Circulation Trace does not define:

* a complete observability platform
* hardware telemetry standards
* exact thermal metrics
* exact acoustic measurement protocols
* vendor-specific monitoring tools
* full distributed tracing infrastructure
* replacement for Earth Brain OS core trace schemas

Instead, it defines a structural vocabulary for recording physical circulation outcomes in Earth Brain OS.

---

## Minimal Implementation Scope

For `v0.4.0-candidate`, the Physical Circulation Trace model should include:

```text
docs/physical-circulation-trace.md
schemas/physical-circulation-trace.schema.json
examples/physical-circulation-trace.example.yaml
scripts/validate_examples.py update
README.md update
CHANGELOG.md update
```

The initial schema should validate a minimum Physical Circulation Trace profile.

The example should demonstrate a Hybrid Node execution outcome with Wind state, Optical route, memory path, fallback status, cloud escalation status, rest requirement, and final outcome.

---

## Summary

The Physical Circulation Trace makes Earth Brain OS physically reflective.

It asks not only:

```text
What did the node do?
```

but also:

```text
What happened to the body when the node did it?
```

This shift is essential.

Without Wind, intelligence overheats.

Without Optical nerves, intelligence fragments.

Without Hybrid Nodes, real local AI infrastructure cannot be modeled accurately.

Without Physical Circulation Trace, the body cannot learn from its own operation.

The Physical Circulation Trace is where Earth Brain OS begins to remember its physical experience.

It is the layer where the body gains a history.

---

## Version

Initial draft for:

```text
v0.4.0-candidate
Physical Circulation Trace Architecture
```
