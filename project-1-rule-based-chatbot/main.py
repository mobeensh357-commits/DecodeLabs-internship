"""
Project 1: Rule-Based AI Chatbot — DecodeLabs Industrial Training (Batch 2026)

A rule-based decision bot that evaluates loan/credit applications using
explicit if-else logic (no machine learning). Supports two modes:

  1. Manual single-application input  ->  apply age=30 income=50000 credit=700 employment=employed loans=0
  2. Batch processing of a CSV file   ->  process sample_applications.csv

Runs in a continuous input loop until the user types 'exit', 'bye', or 'quit'.
"""

import re
import csv

# ---------- RULE ENGINE ----------
def evaluate_application(age, income, credit, employment, loans):
    """Apply explicit if-else business rules to decide Approved/Rejected."""
    if not (18 <= age <= 60):
        return "Rejected", "Age must be between 18 and 60."
    if income <= 30000:
        return "Rejected", "Annual income must be above 30,000."
    if credit < 650:
        return "Rejected", "Credit score must be 650 or higher."
    if employment.lower() not in ["employed", "self-employed"]:
        return "Rejected", "Must be employed or self-employed."
    if loans > 1:
        return "Rejected", "Cannot have more than 1 existing loan."
    return "Approved", "All criteria met."

# ---------- PARSE SINGLE APPLICATION (for manual input) ----------
def parse_application(text):
    """Extract key=value pairs from a command like 'apply age=30 income=50000'."""
    pattern = r'(\w+)=([\w.]+)'
    matches = re.findall(pattern, text)
    return {key: value for key, value in matches}

# ---------- BATCH PROCESS CSV ----------
def process_csv(filename):
    """Read an applications CSV, evaluate every row, and write the results
    (plus Decision/Reason columns) to processed_<filename>."""
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ['Decision', 'Reason']  # Add new columns
            rows = []
            approved = 0
            rejected = 0

            for row in reader:
                # Convert types (adjust column names to match YOUR CSV)
                try:
                    age = int(row.get('age', 0))
                    income = float(row.get('income', 0))
                    credit = int(row.get('credit', 0))
                    employment = row.get('employment', '')
                    loans = int(row.get('loans', 0))

                    status, reason = evaluate_application(age, income, credit, employment, loans)
                except Exception as e:
                    status, reason = "Error", f"Parsing failed: {e}"

                row['Decision'] = status
                row['Reason'] = reason
                rows.append(row)

                if status == "Approved":
                    approved += 1
                elif status == "Rejected":
                    rejected += 1

        # Write output CSV
        output_file = f"processed_{filename}"
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Bot: Batch processing complete!")
        print(f"     Approved: {approved}")
        print(f"     Rejected: {rejected}")
        print(f"     Results saved to: {output_file}")

    except FileNotFoundError:
        print(f"Bot: Error - File '{filename}' not found. Please check the name.")
    except Exception as e:
        print(f"Bot: Unexpected error - {e}")

# ---------- MAIN CHATBOT LOOP ----------
if __name__ == "__main__":
    print("Decision Bot with CSV Batch Support")
    print("Commands:")
    print("  - apply age=XX income=XX credit=XX employment=XX loans=X")
    print("  - process filename.csv   (batch process your dataset)")
    print("  - help")
    print("  - exit / bye\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "bye", "quit"]:
            print("Bot: Goodbye!")
            break

        if user_input == "help":
            print("Bot: Send an application manually, or use 'process data.csv'.")
            continue

        if user_input.startswith("process "):
            filename = user_input[8:].strip()  # Extract filename after 'process '
            process_csv(filename)
            continue

        if user_input.startswith("apply"):
            data = parse_application(user_input)
            try:
                age = int(data.get("age", 0))
                income = float(data.get("income", 0))
                credit = int(data.get("credit", 0))
                employment = data.get("employment", "")
                loans = int(data.get("loans", 0))

                status, reason = evaluate_application(age, income, credit, employment, loans)
                print(f"Bot: Decision = {status}.")
                print(f"     Reason: {reason}")
            except ValueError:
                print("Bot: Invalid number format. Use integers for age, credit, loans, and float for income.")
        else:
            print("Bot: I didn't understand. Type 'help'.")
