import random
import os

# Placeholder: simple mock scoring function.
# Replace this block with LangChain + LLM calls to produce better scores.
def simple_score(name: str, email: str, product_interest: str | None) -> int:
    # deterministic-ish score for demo (hash-based) or random
    base = sum(ord(c) for c in (name or "")) % 50
    interest_bonus = 20 if product_interest else 0
    random_bonus = random.randint(0, 30)
    score = min(100, base + interest_bonus + random_bonus)
    return score

def generate_and_score_lead(name: str, email: str, product_interest: str | None = None):
    """
    Returns (score:int, status:str)
    - score: 0..100
    - status: 'qualified' if score > threshold else 'new'
    """
    score = simple_score(name, email, product_interest)
    status = "qualified" if score >= 60 else "new"
    return score, status
