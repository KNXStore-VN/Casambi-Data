# Casambi-Data

A structured knowledge base for KNXStore's Casambi smart lighting ecosystem — built to power RAG-based chatbot responses, product lookups, and integration guidance.

---

## Overview

This repository contains markdown-formatted documentation for Casambi-compatible products, drivers, and ecosystem integrations. Each file is optimized for retrieval-augmented generation (RAG) with YAML frontmatter metadata for semantic filtering.

The knowledge base covers:
- Product specs, use cases, and pricing for 30+ Casambi-compatible devices
- Driver and controller documentation (Sunricher, Tridonic, and more)
- Integration guides between Casambi and other protocols (KNX, DALI, Modbus, Matter, BACnet)

---

## Repository Structure

```
Casambi-Data/
├── CASAMBI - Lighting Control/   # Product docs for Casambi-compatible lights, sensors, controllers
├── CASAMBI DRIVER/               # Driver and controller product documentation
├── productTemplate.md            # Template for new product files
└── integrationTemplate.md        # Template for ecosystem integration docs
```

---

## File Format

All product and integration files use YAML frontmatter for structured metadata:

```yaml
---
sku: "SR-XXXX"
ecosystem: ["Casambi", "DALI"]
protocols: ["BLE", "0-10V"]
use_cases: ["dimming", "tunable white"]
project_scale: ["residential", "commercial"]
---
```

Body content is written in Markdown, in both Vietnamese and English, following the templates in `productTemplate.md` and `integrationTemplate.md`.

---

## Supported Protocols & Ecosystems

- **Wireless**: Casambi (BLE-based mesh)
- **Wired control buses**: KNX, DALI, Modbus, 0-10V, PWM
- **IoT standards**: Matter, BACnet
- **Integration methods**: Gateway, IP Bridge, Scene Triggers, Native API

---

## Brands Covered

Sunricher, Tridonic, Olfer, Rayrun, Siqitech, Salvador, Vadsbo, and others.

---

## Usage

This data is consumed by KNXStore's chatbot for:
- Answering product specification questions
- Evaluating integration feasibility between ecosystems
- Recommending appropriate gateways and controllers for project deployments

---

## Maintainer

KNXStore Vietnam — [vu.ta@knxstore.vn](mailto:vu.ta@knxstore.vn)
