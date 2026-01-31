# Demo Script – TikTok AI Ad Campaign Creation Agent

## Demo Duration
Approximately **5 minutes**

---

## 1. Introduction (0:00 – 0:30)

Hi, this is Nitin.

In this demo, I’ll walk you through my **TikTok AI Ad Campaign Creation Agent**.  
I’ll explain the project architecture, how prompts are designed, how business rules are enforced, how API failures are handled, and finally I’ll show a short live demo.

The main focus of this project is **reliability and reasoning**, not UI.

---

## 2. Project Structure (0:30 – 1:10)

The project is structured with clear separation of concerns:

- The **agent** module handles conversation flow and validation.
- The **api** module simulates TikTok Ads APIs.
- The **oauth** module handles authentication logic.
- The **models** module defines structured schemas.

This structure makes the system easy to maintain, test, and reason about.

---

## 3. Prompt Design (1:10 – 1:50)

The prompt is designed in a strict way.

The model is **not responsible for business decisions**.  
Its role is limited to generating structured output only.

All business rules and validations are enforced deterministically in code.  
This avoids hallucination and ensures predictable behavior, which is critical for production systems.

---

## 4. Business Rule Enforcement (1:50 – 3:00)

Business rules are enforced in a dedicated validation layer before any API call is made.

Examples of enforced rules:
- Campaign name length validation
- Ad text length validation
- Mandatory CTA

The most important rule is the **music logic**:
- Music is mandatory for **Conversions** campaigns
- Music is optional for **Traffic** campaigns

If an invalid configuration is detected, the agent blocks the flow immediately and explains the issue.  
This ensures invalid ads are never submitted to the API.

---

## 5. API Error Handling & OAuth (3:00 – 3:40)

External APIs are treated as unreliable.

Instead of exposing raw API errors, errors are translated into clear, human-readable messages such as:
- Authentication failure
- Permission or geo-restriction issues
- Invalid input errors

OAuth failures like expired tokens or missing permissions are handled gracefully, and the agent explains what action the user should take.

---

## 6. Live Demo (3:40 – 4:40)

Now I’ll show a short live demo of the agent.

I’ll run the application and provide inputs step by step.

For demo purposes, I’ll use **Demo Mode**, which simulates:
- A valid OAuth token
- An approved music asset
- A successful submission flow

This allows us to clearly see the happy-path behavior.  
In production, real OAuth validation and API checks would be enforced.

The agent successfully submits the ad and returns a mock ad ID.

---

## 7. Improvements & Closing (4:40 – 5:00)

With more time, I would:
- Add retry logic for recoverable API failures
- Integrate the real TikTok Ads API
- Persist conversation state
- Add unit tests for validation and API layers

Thank you for watching the demo.
