# TikTok AI Ad Campaign Creation Agent

## Overview
This project implements a **conversational, production-style AI agent** that guides users through the end-to-end creation and submission of TikTok advertising campaigns using a step-by-step Command Line Interface (CLI).

The intent of this project is **not** UI development or model training. Instead, it focuses on designing a **reliable AI workflow** that mirrors how real-world advertising platforms behave under business constraints and API failures.

Core areas demonstrated:
- Prompt and conversation flow design
- Deterministic business rule enforcement
- Reasoning over external API responses
- Graceful error handling and safe exits
- Structured request and response generation

The agent is designed to behave like a **production-ready system**, not a demo chatbot.

---

## Key Capabilities
- Interactive CLI-based conversation
- Strict validation of business rules before API calls
- Mocked OAuth authentication and permission checks
- Mocked TikTok Ads API with realistic failure scenarios
- Human-readable error explanations
- Structured and validated ad payload generation
- Predictable and deterministic execution flow

---

## High-Level Architecture

The system is intentionally modular, with each component responsible for a single concern.

app/
├── conversation.py    # Manages conversational flow and user input
├── validator.py       # Enforces deterministic business rules
├── tiktok_oauth.py    # Simulates OAuth authentication and permissions
├── tiktok_ads.py      # Simulates TikTok Ads API behavior
├── errors.py          # Maps raw API errors to user-friendly messages
└── main.py            # Application entry point

This separation improves testability, debuggability, and production realism.

---

## Component Responsibilities

### Conversation Layer
Responsible for:
- Asking questions step-by-step
- Maintaining conversation state
- Collecting structured inputs from the user

No business logic or validation is performed here.

---

### Validation Layer
Responsible for:
- Enforcing all business rules deterministically
- Blocking invalid configurations before API calls
- Preventing reliance on LLM judgment

Validation failures immediately stop execution with a clear explanation.

---

### OAuth Layer
Responsible for:
- Simulating authentication
- Validating access tokens
- Checking required permission scopes
- Simulating geo-based access restrictions

This layer ensures secure and realistic authentication behavior.

---

### API Layer
Responsible for:
- Simulating TikTok Ads API requests
- Returning realistic success and failure responses
- Mimicking unreliable external services

All API calls are treated as potentially unreliable.

---

### Error Reasoning Layer
Responsible for:
- Translating raw API errors into human-readable messages
- Categorizing errors (auth, permission, input, system)
- Advising whether retry or correction is possible

This layer significantly improves user experience.

---

## Business Rules

All business rules are enforced strictly in code:

- Campaign name must be at least 3 characters long
- Campaign objective must be either:
  - Traffic
  - Conversions
- Ad text must not exceed 100 characters
- Call-To-Action (CTA) is mandatory
- Music rules:
  - Music is mandatory for Conversions campaigns
  - Music is optional for Traffic campaigns
  - Invalid combinations are blocked before submission

---

## Music Configuration Handling

The agent supports three music configurations:

1. Existing Music ID  
   - User provides a music ID  
   - ID is validated via the API  
   - Invalid IDs are rejected with explanation  

2. Custom / Uploaded Music  
   - Music upload is simulated  
   - A mock music ID is generated  
   - Generated ID is validated before submission  

3. No Music  
   - Allowed only for Traffic campaigns  
   - Explicitly blocked for Conversions campaigns  

---

## OAuth Failure Handling

The agent safely handles common OAuth failure scenarios:

- Expired or invalid access token (401)
- Missing Ads permission scope (403)
- Geo-restriction or region-based access denial (403)

Instead of exposing raw error codes, the agent:
- Explains the issue clearly
- Suggests corrective action
- Exits safely without crashing

---

## API Failure Reasoning

All external API calls are assumed to be unreliable.

Failures are:
- Categorized into authentication, permission, validation, or system errors
- Translated into user-friendly explanations
- Used to determine retry eligibility

This mirrors real-world production API behavior.

---

## Tech Stack
- Language: Python 3.10
- Interface: Command Line Interface (CLI)
- APIs: Mocked TikTok Ads API and OAuth
- Environment: Python Virtual Environment (venv)

---

## How to Run

python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate       # Windows
python app/main.py

---

## Example Scenarios Tested

- Conversions campaign without music  
  Blocked before API submission with a clear validation error.

- Invalid music ID  
  Music validation API rejects the ID with an explained error.

- OAuth authentication failure  
  Agent explains token expiry or missing permissions.

- Geo-restriction error  
  Agent reports region-based restriction clearly.

- Successful ad submission  
  Agent returns a mock ad ID after successful submission.

---

## Prompt Design Philosophy

The agent follows a strict and safe prompt design philosophy:

- The LLM is responsible only for formatting structured output
- All decision-making is enforced deterministically in code
- The agent never relies on the model to decide what is allowed

This prevents hallucinations and ensures predictable behavior.

---

## Limitations
- External APIs are mocked
- CLI-based interface only
- No persistent storage across sessions

---

## Future Enhancements
- Retry logic for recoverable API failures
- Persistent conversation state
- Integration with real TikTok Ads API
- Unit tests for validation and API layers
- Minimal web-based UI

---

## Final Notes

This project demonstrates how to design a **robust AI-driven workflow** that reasons about:
- Business constraints
- External API failures
- Structured request/response handling

The emphasis is on **engineering correctness, clarity, and production realism**, making this project suitable for interviews, system design discussions, and real-world inspiration. 

## 🎥 Demo Video
A 5-minute walkthrough covering architecture, rule enforcement, API error handling, and a successful demo flow:

👉 https://drive.google.com/file/d/14-mAyUOy-ErJokPUbIFp9Deg7r1tnkyv/view?usp=drive_link

