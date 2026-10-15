"""
WinTrust weighted pipeline calculation.

Training exercise:
Use GitHub Copilot to review this function for correctness,
edge cases, and test coverage.

Expected input:
    opportunities = [
        {"opportunity_id": "OPP-001", "revenue": 100000, "probability": 0.25},
        {"opportunity_id": "OPP-002", "revenue": 200000, "probability": 0.75},
    ]

Probability is intended to represent a percentage as a decimal.
For example:
    0.25 = 25%
    0.75 = 75%
"""


def calculate_weighted_pipeline(opportunities):
    """
    Calculate the total weighted sales pipeline.

    Weighted value = revenue * probability
    """
    total = 0

    for opportunity in opportunities:
        revenue = opportunity["revenue"]
        probability = opportunity["probability"]

        total += revenue * probability

    return round(total, 2)


if __name__ == "__main__":
    sample_opportunities = [
        {
            "opportunity_id": "OPP-001",
            "revenue": 100000,
            "probability": 0.25,
        },
        {
            "opportunity_id": "OPP-002",
            "revenue": 200000,
            "probability": 0.75,
        },
        {
            "opportunity_id": "OPP-003",
            "revenue": 50000,
            "probability": 0.50,
        },
    ]

    result = calculate_weighted_pipeline(sample_opportunities)

    print(f"Weighted pipeline: {result:,.2f}")
    