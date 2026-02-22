---

```md
# Personal AI Employee — Bronze Tier (Hackathon 0)

## Overview

This project implements the **Bronze Tier** deliverable for **Hackathon 0: Personal AI Employee (Digital FTE)**.

The goal of the Bronze Tier is to demonstrate a **foundational autonomous AI loop** where:
- An external event is detected automatically
- A task is written into a local knowledge system (Obsidian vault)
- An AI agent (Claude Code) reasons over the task
- The AI writes results back to the vault
- The task is marked complete by moving it to a `/Done` folder

This project is **local-first**, privacy-preserving, and fully auditable.

---

## What This Project Demonstrates

✅ Local-first AI Employee architecture  
✅ Obsidian used as long-term memory + dashboard  
✅ Watcher-based perception (filesystem events)  
✅ Claude Code reading and writing files autonomously  
✅ File-based task lifecycle: `Inbox → Needs_Action → Done`  
✅ No manual prompting after task arrival  

This establishes the **foundation** for higher tiers (Silver, Gold, Platinum).

---

## Architecture (Bronze Tier)

```

External Trigger (File Drop)
↓
Filesystem Watcher (Python)
↓
/Needs_Action (Obsidian Vault)
↓
Claude Code (Reasoning Engine)
↓
Dashboard.md updated
↓
Task moved to /Done

```

---

## Folder Structure

```

ai-employee/
│
├── filesystem_watcher.py        # Python watcher (perception layer)
│
├── AI_Employee_Vault/           # Obsidian vault (memory + UI)
│   ├── Inbox/
│   ├── Needs_Action/
│   ├── Done/
│   ├── Logs/
│   ├── Dashboard.md
│   └── Company_Handbook.md
│
└── README.md

````

---

## Prerequisites

- Python **3.13+**
- Obsidian **v1.10.6+**
- Claude Code (installed globally)
- Git

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd ai-employee
````

---

### 2. (Optional but Recommended) Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install watchdog
```

---

### 4. Open Obsidian Vault

Open **Obsidian** and select the folder:

```
AI_Employee_Vault
```

---

### 5. Start Filesystem Watcher

From the project root:

```bash
python filesystem_watcher.py
```

You should see:

```
Filesystem Watcher running...
```

⚠️ Keep this terminal running.

---

## How to Trigger the AI Employee

1. Create a new Markdown file inside:

```
AI_Employee_Vault/Inbox/
```

Example: `task_test.md`

```md
---
type: test_task
priority: high
---

Summarize this task and mark it complete.
```

2. The watcher automatically moves it to `/Needs_Action`
3. Run Claude Code from the **vault directory**:

```bash
cd AI_Employee_Vault
claude
```

4. Use the Bronze processing prompt to let Claude:

   * Read the task
   * Update `Dashboard.md`
   * Move the task to `/Done`

---

## AI Rules & Safety

All AI behavior is constrained by **Company_Handbook.md**, which defines:

* Communication rules
* Completion criteria
* Safety constraints
* No external actions
* No deletions

This ensures **predictable, auditable behavior**.

---

## Bronze Tier Deliverables Checklist

✅ Obsidian vault with dashboard and handbook
✅ One working watcher (filesystem-based)
✅ Claude Code reads and writes vault files
✅ Task lifecycle folders implemented
✅ All AI logic implemented via agent behavior (no hardcoding)

---

## What Is NOT Included (By Design)

❌ No MCP servers
❌ No Gmail / WhatsApp automation
❌ No payments or social posting
❌ No cron scheduling
❌ No always-on cloud deployment

These belong to **Silver+ tiers**.

---

## Demo Instructions (For Judges)

1. Start `filesystem_watcher.py`
2. Drop a task file into `/Inbox`
3. Show file auto-moved to `/Needs_Action`
4. Run Claude Code to process tasks
5. Show `Dashboard.md` update
6. Show task moved to `/Done`

---

## Hackathon Metadata

* **Hackathon:** Personal AI Employee Hackathon 0
* **Tier:** Bronze
* **Reasoning Engine:** Claude Code
* **Memory System:** Obsidian (Local Markdown)
* **Automation Pattern:** Watcher → Reason → Write

---

## Next Steps

This Bronze Tier foundation is designed to be extended into:

* Silver Tier: Planning, MCP servers, HITL
* Gold Tier: Accounting, cross-domain autonomy
* Platinum Tier: Cloud + Local agent collaboration

---
