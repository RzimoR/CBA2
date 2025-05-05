
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import numpy_financial as npf

app = Flask(__name__)

@app.route("/cba", methods=["POST"])
def cba():
    data = request.json
    rate = 0.015
    years = 10
    results = []

    for name, alt in data.items():
        df = pd.DataFrame({
            "Year": list(range(0, years + 1)),
            "CAPEX": alt["CAPEX"],
            "OPEX": alt["OPEX"],
            "BENEFITS": alt["BENEFITS"]
        })
        df["Net_Cash_Flow"] = df["BENEFITS"] - (df["CAPEX"] + df["OPEX"])
        df["Discount_Factor"] = 1 / (1 + rate) ** df["Year"]
        df["Discounted_CAPEX"] = df["CAPEX"] * df["Discount_Factor"]
        df["Discounted_OPEX"] = df["OPEX"] * df["Discount_Factor"]
        df["Discounted_Benefits"] = df["BENEFITS"] * df["Discount_Factor"]
        df["Discounted_Cost"] = df["Discounted_CAPEX"] + df["Discounted_OPEX"]
        df["NPV_Year"] = df["Discounted_Benefits"] - df["Discounted_Cost"]

        total_discounted_costs = df["Discounted_Cost"].sum()
        total_discounted_benefits = df["Discounted_Benefits"].sum()
        CB_ratio = total_discounted_benefits / total_discounted_costs if total_discounted_costs else None
        irr = npf.irr(df["Net_Cash_Flow"].values)
        total_npv = df["NPV_Year"].sum()

        results.append({
            "alternative": name,
            "NPV": round(total_npv, 2),
            "IRR": round(irr, 4),
            "Discounted Costs": round(total_discounted_costs, 2),
            "Discounted Benefits": round(total_discounted_benefits, 2),
            "BCR": round(CB_ratio, 4)
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
