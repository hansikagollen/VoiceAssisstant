import csv
import json
import os

SCHEME_FILE = "data/schemes.json"

def check_eligibility(state):
    with open(SCHEME_FILE, encoding="utf-8") as f:
        schemes = json.load(f)

    for s in schemes:
        if state["age"] >= s["min_age"] and state["income"] <= s["max_income"]:
            return s["name"]
    return None

def save_application(state, scheme):
    file_exists = os.path.exists("applications.csv")
    with open("applications.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["name", "age", "income", "scheme"])
        writer.writerow([
            state.get("name", "Anonymous"),
            state.get("age"),
            state.get("income"),
            scheme
        ])
