import json

# Load the full scholarship dataset
with open("scholarships.json", "r") as f:
    SCHOLARSHIPS = json.load(f)

def get_recommendations(user):
    percentage = user["percentage"]
    income = user["income"]
    category = user["category"].lower()
    gender = user["gender"].lower()

    results = []

    for s in SCHOLARSHIPS:

        ok = True
        elig = s["eligibility"].lower()

        # --- Percentage filter ---
        if s["minmarks"] != "" and percentage < int(s["minmarks"]):
            ok = False

        # --- Income filter ---
        if "income" in s and s["income"] != "" and income > int(s["income"]):
            ok = False

        # --- Gender filter ---
        # Female-only
        if any(w in elig for w in ["female", "girl", "women", "woman"]):
            if gender != "female":
                ok = False

        # Male-only
        if any(w in elig for w in ["male", "boy", "man", "men"]):
            if gender != "male":
                ok = False

        # --- Category filter ---
        if any(cat in elig for cat in ["sc", "st", "obc"]):
            if category not in ["sc", "st", "obc"]:
                ok = False

        if ok:
            results.append(s)

    return results
