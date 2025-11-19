from flask import Flask, render_template, request
import json
from rules import get_recommendations

app = Flask(__name__)

# -----------------------------
# Load Scholarships (NO deadline)
# -----------------------------
with open("scholarships.json", "r") as f:
    SCHOLARSHIPS = json.load(f)

# Convert id to int for safety
for s in SCHOLARSHIPS:
    s["id"] = int(s["id"])


@app.route("/")
def home():
    return render_template("index.html", scholarships=SCHOLARSHIPS)


@app.route("/recommend", methods=["POST"])
def recommend():
    user_data = {
        "percentage": float(request.form["percentage"]),
        "income": float(request.form["income"]),
        "category": request.form["category"].lower(),
        "gender": request.form["gender"].lower()
    }

    recommended = get_recommendations(user_data)

    return render_template("recommend.html", rec=recommended)


@app.route("/apply/<int:sch_id>", methods=["GET", "POST"])
def apply(sch_id):

    scholarship = next((s for s in SCHOLARSHIPS if s["id"] == sch_id), None)

    if scholarship is None:
        return "Scholarship not found", 404

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return render_template("success.html", name=name, scholarship=scholarship)

    return render_template("apply.html", scholarship=scholarship)


if __name__ == "__main__":
    app.run(debug=True)
