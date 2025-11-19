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

        # Check percentage
        if s["minmarks"] != "" and percentage < int(s["minmarks"]):
            ok = False

        # Check income
        if "income" in s and s["income"] != "" and income > int(s["income"]):
            ok = False

        # Gender filter
        if s["eligibility"].lower().find("female") != -1 and gender != "female":
            ok = False

        if s["eligibility"].lower().find("male") != -1 and gender != "male":
            ok = False

        # Category filter
        if any(cat in s["eligibility"].lower() for cat in ["sc","st","obc"]):
            if category not in ["sc","st","obc"]:
                ok = False

        if ok:
            results.append(s)

    return results
