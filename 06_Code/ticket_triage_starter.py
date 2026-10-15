"""Starter for the GitHub Copilot scripting lab. No external services."""
from dataclasses import dataclass

@dataclass
class Ticket:
    ticket_id: str
    customer_criticality: str
    severity: str
    elapsed_minutes: int
    sla_minutes: int
    affected_transactions: int
    symptom: str

def classify_ticket(ticket: Ticket) -> dict:
    """Implement deterministic WinTrust triage rules with GitHub Copilot."""
    raise NotImplementedError
