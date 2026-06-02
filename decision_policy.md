# Decision Policy

## Purpose

This policy defines how the Hybrid AI Complaint Escalation System converts model predictions into business actions. The policy ensures that automated decisions remain explainable, consistent, and subject to appropriate human oversight.

---

## Risk Thresholds

### Low Risk

```text
final_score < 0.45
```

Characteristics:

* Minor customer issues
* Low likelihood of escalation
* No significant product or support concerns

Examples:

* Delivery slightly delayed
* Invoice request
* General information request

### Medium Risk

```text
0.45 <= final_score < 0.75
```

Characteristics:

* Customer dissatisfaction is present
* Potential escalation indicators exist
* Human review may be beneficial

Examples:

* Wrong item received
* Refund request
* Repeated customer complaints

### High Risk

```text
final_score >= 0.75
```

Characteristics:

* Strong escalation indicators
* Product damage or service failure
* Immediate attention required

Examples:

* Broken product received
* Multiple unanswered support requests
* Repeated unresolved complaints

---

## Actions

### Low Risk

Action:

```text
auto_reply
```

Policy:

* Automated response is permitted.
* No mandatory human review.
* Case remains monitored for future escalation.

### Medium Risk

Action:

```text
manual_review
```

Policy:

* Route complaint to support staff.
* Human review required before final action.
* Customer interaction should be monitored.

### High Risk

Action:

```text
escalate_immediately
```

Policy:

* Immediate escalation to senior support team.
* Human intervention required.
* Priority handling recommended.

---

## Human Review Rules

Human review is required when:

* Risk level is medium or high.
* Model scores disagree significantly.
* Complaint text is unclear or ambiguous.
* Image quality is poor or unreadable.
* Customer history appears inconsistent.
* LLM returns `human_review_required = true`.
* The final recommendation could significantly impact customer experience.

Examples of model disagreement:

```text
Classical ML Score = 0.90
CNN Score = 0.20
RNN Score = 0.80
```

Such cases require manual verification before action.

---

## Model Disagreement Policy

Model disagreement is considered significant when:

```text
max(model_scores) - min(model_scores) >= 0.50
```

When significant disagreement is detected:

* Human review becomes mandatory.
* Automatic escalation decisions should be reviewed.
* Additional evidence may be requested.

---

## LLM Restrictions

The LLM acts only as an explanation and decision-support component.

The LLM may:

* Summarize customer complaints.
* Explain model outputs.
* Recommend a policy-approved action.
* Flag cases requiring human review.
* Generate risk notes.

The LLM may not:

* Override model scores.
* Change risk levels.
* Approve refunds.
* Reject customer claims.
* Make legal decisions.
* Make financial decisions.
* Make hiring decisions.
* Make medical decisions.
* Make final customer service decisions.

---

## Governance and Accountability

The Hybrid AI system is designed to support human decision-making rather than replace it.

Final responsibility for customer-facing actions remains with authorized support personnel.

All medium-risk and high-risk cases must remain auditable through:

* Model outputs
* Hybrid scores
* LLM explanations
* Human review decisions

This ensures transparency, explainability, and responsible AI usage.
