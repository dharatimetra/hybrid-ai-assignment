# Problem Framing

## Business scenario

An e-commerce company receives customer complaints through multiple channels such as website forms, email, and customer support chat. Complaints may include customer profile information, complaint text, product images, and previous complaint history.

The company wants to build a Hybrid AI system that can automatically analyze complaints and predict the escalation risk level of each complaint as Low, Medium, or High. The system should also recommend the appropriate action for the support team.

The objective is to improve customer support efficiency, reduce unresolved escalations, prioritize critical complaints faster, and improve customer satisfaction.

---

## Prediction target

The prediction target is the complaint escalation risk level:

* Low
* Medium
* High

The system also recommends one of the following business actions:

* Auto-reply
* Manual review
* Escalate immediately

---

## Who will use the output

The output will primarily be used by:

* Customer support agents
* Customer escalation teams
* Operations managers
* Quality assurance teams

The predictions help support teams prioritize complaints and respond more efficiently.

---

## Business action

Based on the predicted risk level, the system performs the following actions:

| Risk Level | Recommended Action                                        |
| ---------- | --------------------------------------------------------- |
| Low        | Auto-reply using predefined response                      |
| Medium     | Send for manual review by support agent                   |
| High       | Escalate immediately to senior support or escalation team |

The system may also generate a short AI-based complaint summary to help agents quickly understand the issue.

---

## False positive impact

A false positive occurs when the system predicts a complaint as High risk even though it is actually Low or Medium risk.

Impact:

* Unnecessary escalations
* Increased workload for senior support staff
* Higher operational costs
* Slower handling of genuinely critical complaints

Example:
A minor delivery delay may incorrectly get escalated as a critical complaint.

---

## False negative impact

A false negative occurs when the system predicts a complaint as Low or Medium risk even though it is actually High risk.

Impact:

* Serious customer dissatisfaction
* Missed urgent complaints
* Negative social media or public reviews
* Potential customer churn and revenue loss
* Brand reputation damage

Example:
A damaged product complaint with repeated failed support attempts may not receive urgent attention.

False negatives are considered more harmful in this business scenario.

---

## Human review required when

Human review is required when:

* The predicted risk level is High
* The complaint text contains strong negative sentiment or legal threats
* The uploaded product image shows severe damage
* The customer has multiple previous complaints
* Model confidence is low
* Different AI models produce conflicting predictions

Human oversight is important to ensure fairness, accuracy, and responsible business decisions.

## Optional Components Status

### FastAPI API

Implemented.

File:

```text
app.py
```

The Hybrid AI system is exposed through a local FastAPI service with the following endpoints:

* `GET /` – Health Check
* `POST /predict` – Hybrid AI prediction endpoint

The API was successfully tested locally using Uvicorn and Swagger UI.

---

### Docker Containerization

Implemented.

Files:

```text
Dockerfile
requirements-docker.txt
```

The application was successfully containerized using Docker and tested locally.

Docker validation completed:

* Docker image built successfully
* Container started successfully
* FastAPI endpoints accessible through Docker
* Swagger UI available at:

```text
http://localhost:8000/docs
```

---

### AWS Hosting

Not completed as part of the final submission.

Current Status:

```text
Work In Progress (WIP)
```

Progress completed:

* FastAPI application developed
* Docker containerization completed
* GitHub repository created and configured

Planned deployment target:

```text
AWS Lambda (Container-based deployment)
```

Future work includes:

* Deploying the Dockerized application to AWS
* Configuring environment variables securely
* Exposing a public API endpoint
* Performance and latency testing in the cloud

---

### Environment Variables

Sensitive credentials are not hard-coded in the source code.

The following environment variable is required:

```text
GEMINI_API_KEY
```

This key must be provided through environment configuration during local execution or cloud deployment.
