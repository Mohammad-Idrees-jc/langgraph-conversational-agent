# LangGraph Conversational Agent

A stateful conversational AI agent built on **LangGraph**, developed in
incremental, production-oriented stages — from a minimal terminal chatbot to a
persistent, tool-augmented, observable agent with human-in-the-loop control.

Each stage is a separate, reviewable commit, so the repository doubles as a
reference implementation for LangGraph's core primitives.

---

## Why this project

Most chatbot examples are single-file scripts with no state model, no
persistence, and no failure handling. This project treats a chatbot as what it
actually is in production: a **graph of nodes operating over typed, checkpointed
state**.

---

## Architecture

The agent is a directed graph. Version 1 is intentionally minimal: