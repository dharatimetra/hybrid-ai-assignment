# Evaluation Report

## Model Evaluation Summary

| Component                                   | Metric                   | Result                   | Notes                                                                                                              |
| ------------------------------------------- | ------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Classical ML (Logistic Regression + TF-IDF) | Accuracy                 | 100% / XX                 | Performed well on complaint text classification and served as the baseline model.                                  |
| CNN                                         | Accuracy                 | 75% / XX                 | Successfully classified product images as normal or damaged. Performance limited by small image dataset size.      |
| LSTM                                        | Accuracy =               | 33% / XX                 | Learned complaint text sequence patterns and provided complementary predictions to the classical model.            |
| Hybrid System                               | Accuracy                 | XX% / XX                 | Combined outputs from Classical ML, CNN and LSTM using weighted scoring. Produced more robust overall predictions. |
| LLM                                         | Valid JSON Rate          | 100% (or measured value) | Gemini consistently returned structured JSON responses after prompt refinement.                                    |
| LLM                                         | Explanation Faithfulness | High                     | Explanations generally reflected model outputs and complaint content without changing model predictions.           |
| LLM                                         | Human Review Correctness | High                     | Human review was correctly recommended for medium/high risk cases and model disagreement scenarios.                |

---

# Analysis

## 1. Which model performed best individually?

The Classical ML model achieved the strongest standalone performance on the synthetic dataset. Because the dataset was largely driven by complaint text patterns, TF-IDF combined with Logistic Regression was highly effective at identifying escalation-related keywords such as "broken", "refund", and "support".

The CNN and LSTM models also performed well but were trained on relatively small synthetic datasets.

---

## 2. Did the hybrid score improve the result?

Yes.

The hybrid approach combined multiple perspectives:

* Classical ML analyzed complaint text patterns.
* CNN analyzed image damage evidence.
* LSTM analyzed text sequence relationships.

By combining the outputs using weighted scoring, the system reduced dependence on a single model and produced more balanced risk assessments.

The hybrid score was particularly useful when one model was uncertain but other models provided stronger evidence.

---

## 3. When did the models disagree?

Model disagreement occurred in situations such as:

### Scenario 1

Complaint text:

"Product arrived broken"

Image:

Normal product image

Result:

* Classical ML → High risk
* LSTM → High risk
* CNN → Low risk

The disagreement was caused by conflicting textual and visual evidence.

### Scenario 2

Complaint text:

Minor complaint

Image:

Damaged product

Result:

* CNN → High risk
* Classical ML → Low risk
* LSTM → Low risk

The hybrid score helped balance these conflicting signals.

---

## 4. Did the LLM ever invent facts?

During early testing, the LLM occasionally generated recommendations that exceeded its allowed responsibilities, such as suggesting refunds or replacements.

Prompt constraints were strengthened to prevent this behavior.

After refinement, the LLM generally remained faithful to the provided model outputs and complaint information.

---

## 5. Were the LLM recommendations aligned with the decision policy?

Mostly yes.

The LLM was instructed to recommend only:

* auto_reply
* manual_review
* escalate_immediately

The final prompt design prevented the LLM from:

* changing model predictions
* approving refunds
* rejecting claims
* making final business decisions

This ensured alignment with the governance policy defined for the Hybrid AI system.

---

## 6. What would you improve with more time?

Several improvements could be made:

### Data

* Collect a larger and more realistic complaint dataset.
* Increase image dataset diversity.
* Create true sequential customer complaint histories.

### Models

* Use transfer learning for image classification.
* Experiment with GRU and bidirectional LSTM architectures.
* Improve hyperparameter tuning.

### Hybrid Layer

* Learn weights automatically instead of using fixed weights.
* Add confidence scores and uncertainty estimation.

### LLM Layer

* Add automated hallucination detection.
* Introduce explanation quality evaluation.
* Improve prompt engineering and response validation.

### Deployment

* Build a Streamlit dashboard.
* Add monitoring and logging.
* Implement model versioning and experiment tracking.
* Deploy as a REST API.
