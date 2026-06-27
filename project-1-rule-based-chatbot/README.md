# Project 1: Rule-Based AI Chatbot (Application Decision Bot)

Industrial Training Kit submission for DecodeLabs (Batch 2026).

## Overview

A rule-based decision bot that evaluates loan/credit applications using
explicit if-else logic — no machine learning involved. It demonstrates
control flow, decision-making logic, and a continuous interaction loop,
extended into a small practical tool with two modes:

1. **Manual mode** — evaluate one application typed in directly.
2. **Batch mode** — evaluate every row in a CSV file and write the
   results (with `Decision` and `Reason` columns added) to a new file.

> **Note on scope vs. the original brief:** the assignment brief
> describes a chatbot that "handles greetings and exit commands."
> This implementation focuses entirely on the application-evaluation
> logic and exit commands; it does not include greeting responses
> (e.g. "hello" / "hi"). The core required skills — if-else control
> flow, decision-making logic, and a continuous loop — are all present
> and demonstrated through the application-decision use case instead.

## Rules Applied

| Rule | Condition for Rejection |
|---|---|
| Age | Must be between 18 and 60 |
| Income | Must be above 30,000 |
| Credit score | Must be 650 or higher |
| Employment | Must be "employed" or "self-employed" |
| Existing loans | Must not exceed 1 |

## Files

| File | Purpose |
|---|---|
| `main.py` | The chatbot/decision-bot script |
| `sample_applications.csv` | Example input data for batch mode |
| `processed_sample_applications.csv` | Example output after running batch mode on the sample data |

## How to Run

```bash
python main.py
```

Then, at the `You:` prompt, try:

```
apply age=30 income=50000 credit=700 employment=employed loans=0
process sample_applications.csv
help
exit
```

No external dependencies — uses only the Python standard library
(`re`, `csv`).

## Skills Demonstrated

Control flow, decision-making logic, basic AI concepts (rule-based
reasoning), CSV file I/O, and a continuous input loop.
