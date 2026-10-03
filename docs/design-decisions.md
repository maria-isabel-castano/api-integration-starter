# Design decisions

## Adapter boundary
Provider-specific request/response shapes stay inside the adapter. The operational system receives a normalized contract.

## Idempotency
Repeated execution should not create duplicate downstream work. Real providers should receive an idempotency key where supported; otherwise persist one internally.

## Retries
Retry only transient failures such as timeouts, throttling and selected 5xx responses. Validation and authorization failures should surface immediately.

## Observability
Record attempts, latency, provider response category and correlation IDs. Never log secrets or unnecessary personal data.

## Secrets
Use environment variables or a secret manager. Credentials do not belong in source control.
