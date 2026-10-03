# API Integration Starter

A compact reference architecture for reliable business API integrations.

The interesting part of an integration is not the HTTP request. It is what happens when authentication expires, a provider throttles requests, data is malformed, a request is retried, or the downstream system is temporarily unavailable.

This starter separates those concerns so integrations can evolve without burying operational logic inside API calls.

## Architecture

```text
Operational System
       ↓
Input Validation
       ↓
Integration Service
       ↓
Provider Adapter → External API
       ↓                ↓
Normalized Result   Retry / Error
       ↓                ↓
Business Workflow ← Observability
```

## What it demonstrates

- provider-specific code behind an adapter
- normalized responses
- timeouts and bounded retries
- retryable vs non-retryable errors
- idempotency support
- structured operational events
- no credentials committed to source control

## Quick start

Requires Python 3.10+ and uses only the standard library.

```bash
python src/integration.py
```

The included provider is simulated so the repository runs without external credentials.

## Production principle

An API integration is an operational dependency. It should fail visibly, retry intentionally and return a predictable contract to the rest of the system.

## Related

- [Portfolio](https://mariacastano.co/)
- [Custom Web Apps](https://mariacastano.co/custom-web-apps/)
- [Internal Tools](https://mariacastano.co/internal-tools/)

Built by **María Isabel Castaño — AI Systems Developer | Web Apps, APIs & Automation**.
