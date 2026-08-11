---
title: "rPocketBase"
tagline: "A PocketBase-shaped backend-as-a-service, reimplemented in Rust — embedded SQLite, REST API, realtime SSE, and an admin UI, all in a single self-hosted binary."
description: "rPocketBase is a clean-room, Rust implementation of a PocketBase-style backend: collections, auth, files, realtime, and an admin dashboard you host yourself."
platforms: ["Web", "Linux"]
tech: ["Rust", "SQLite", "REST API", "Realtime SSE", "JWT", "Docker"]
featured: true
weight: 4
year: "2026"
timeline: "Ongoing"
client: "Rinse Repeat Labs"
image: "/images/rpocketbase.png"
openSource: true
license: "MIT"
# githubUrl: "https://github.com/RinseRepeatLabs/rPocketBase"  # uncomment when the repo is made public
---

## Overview

rPocketBase is a clean-room reimplementation of a PocketBase-style backend-as-a-service, written in Rust. It ships as a single self-hosted binary with an embedded SQLite database, a REST API, password auth with JWT, file storage, realtime updates over SSE, and an admin dashboard at `/_/`.

It's an honest MVP: the goal is *PocketBase-shaped* HTTP so familiar patterns feel at home (`/api/collections/.../records`, auth-with-password, `expand`, filters) — not 1:1 SDK, OAuth, or batch parity. rPocketBase is independent of PocketBase, developed clean-room, and is not affiliated with or endorsed by the PocketBase authors.

## Why We Built It

We wanted a PocketBase-*like* API in a memory-safe Rust binary — no GC runtime, easy to ship as a LAN or appliance-style deployment — with a few capabilities treated as first-class from day one rather than bolted on later:

- **Sealed secret fields** instead of "store the API token in a text column."
- **TTL / expiry behaviors** at the collection level, not just app-side filtering.
- **Machine API keys** that are explicitly *not* superusers.
- An **ops-oriented admin** with backups, storage inventory, and schema export/import.

The result is a smaller, readable surface that's easy to fork, embed, or run as an internal tool.

## Key Features

**Collections & Rules**
Base, auth, and view collections with PocketBase-style rule semantics — `null` for superuser-only, `""` for any authenticated user, or a full expression — plus `@request.*` macros, filters, and nested relation `expand`.

**Secret Fields**
A first-class `secret` field type backed by AES-GCM envelopes and a reveal API, so sensitive values are never sitting in plain text.

**Behavior Packs**
Collection-level TTL / expiry, unique-key, and ordered behaviors, alongside autodate and multi-select fields.

**Machine API Keys**
Non-superuser keys scoped to collection allowlists and then evaluated against your normal CRUD rules — safe access for services and automations.

**Files & Realtime**
Multipart uploads served from `/api/files/...`, relation `expand`, and realtime change events over SSE at `/api/realtime`, with a live badge in the admin UI.

**Ops-Ready Admin**
A dashboard at `/_/` for the schema editor, guided rules, export/import, storage inventory, a metrics checklist, and full `pb_data` zip backups — plus a CLI and a first-run superuser installer that keeps the API locked until setup.

## Getting Started

1. Build the release binary (`cargo build --release`) or run the published Docker image.
2. Start the server with `rpocketbase serve` — the admin UI comes up at `http://127.0.0.1:8090/_/`.
3. Create your superuser on first run; the API stays locked until setup is complete.
4. Define collections, fields, and rules in the dashboard — or import a schema JSON.
5. Point your app at the REST API and subscribe to realtime SSE.

## Open Source

rPocketBase is **Rinse Repeat Labs' first open-source project** — released under the **MIT** license, clean-room, and independent of PocketBase. We're finishing a security and documentation pass before opening the repository, after which the source will live at `github.com/RinseRepeatLabs/rPocketBase`.

**Public release coming soon** — it'll be free to self-host, fork, and build on.
