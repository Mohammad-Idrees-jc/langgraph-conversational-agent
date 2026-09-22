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

START ──▶ chat_node ──▶ END


Conversation state is a `TypedDict` whose `messages` field uses an
`Annotated` reducer, so each turn appends to history rather than overwriting it.
A **checkpointer** persists that state per `thread_id`, which is what gives the
agent memory across turns — and, later, across process restarts.

| Concept | Implementation |
|---|---|
| State | `TypedDict` with annotated message reducer |
| Execution | `StateGraph` compiled to a runnable |
| Memory | Checkpointer keyed by `thread_id` |
| Model | HuggingFace Inference Endpoint via `ChatHuggingFace` |

---

## Roadmap

| Stage | Capability                                           | Status |
|---|------------------------------------------------------|---|
| 1 | Terminal chat with in-memory checkpointing           | ✅ Complete |
| 2 | Durable persistence (SQLite / Postgres checkpointer) | ✅ Complete |
| 3 | Streamlit UI                                         | ✅ Complete |
| 4 | Token streaming                                      | ✅ Complete |
| 5 | Resume prior conversation threads                    | 🔜 Planned |
| 6 | Tool calling                                         | 🔜 Planned |
| 7 | RAG over a document corpus                           | 🔜 Planned |
| 8 | LangSmith tracing and evaluation                     | 🔜 Planned |
| 9 | Human-in-the-loop interrupts and approval            | 🔜 Planned |
| 10 | Fault tolerance and retry policies                   | 🔜 Planned |

---

## Getting started

### Prerequisites
- Python 3.10+
- A HuggingFace access token

### Installation

```bash
git clone https://github.com/Mohammad-Idrees-jc/langgraph-conversational-agent.git
cd langgraph-conversational-agent

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

### Run

```bash
for UI use the following
- streamlit_frontend.py → basic UI (no streaming)
- streamlit_frontend_streaming.py → UI with streaming responses (latest)
- chat_bot.py → old terminal-only version, kept for reference
```

Type `exit` to end the session.

---

## Project structure

langgraph-conversational-agent/
├── chatbot.py # Graph definition and terminal loop
├── langgraph_backend.py # Graph definition, state, checkpointer
├── streamlit_frontend.py # streamlit friendly UI for the chatbot
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


---

## Tech stack

LangGraph · LangChain Core · HuggingFace Inference Endpoints · Python

---

## Author

**Mohammad Idrees Khan** — BS Computer Science, University of Swat
[GitHub](https://github.com/Mohammad-Idrees-jc) · Mohammadidreesjc@gmail.com

---

## License

MIT
