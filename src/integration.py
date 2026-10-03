from dataclasses import dataclass
from time import sleep
from typing import Any, Dict


class IntegrationError(Exception):
    pass


class RetryableIntegrationError(IntegrationError):
    pass


@dataclass
class IntegrationResult:
    ok: bool
    provider_id: str | None
    data: Dict[str, Any]
    attempts: int


class DemoProvider:
    """Synthetic provider adapter. Replace with a real HTTP client in production."""

    def send(self, payload: Dict[str, Any], idempotency_key: str) -> Dict[str, Any]:
        if not idempotency_key:
            raise IntegrationError("idempotency_key is required")
        if payload.get("simulate") == "rate_limit":
            raise RetryableIntegrationError("provider rate limited request")
        if "customer_id" not in payload:
            raise IntegrationError("customer_id is required")
        return {"id": f"EXT-{payload['customer_id']}", "status": "accepted"}


def execute(provider: DemoProvider, payload: Dict[str, Any], key: str, max_attempts: int = 3) -> IntegrationResult:
    for attempt in range(1, max_attempts + 1):
        try:
            response = provider.send(payload, key)
            print({"event": "integration_success", "attempt": attempt, "provider_id": response["id"]})
            return IntegrationResult(True, response["id"], response, attempt)
        except RetryableIntegrationError as exc:
            print({"event": "integration_retry", "attempt": attempt, "error": str(exc)})
            if attempt == max_attempts:
                raise
            sleep(0.1 * attempt)
        except IntegrationError:
            raise

    raise RuntimeError("unreachable")


if __name__ == "__main__":
    result = execute(
        DemoProvider(),
        {"customer_id": "C-204", "operation": "sync"},
        key="sync-C-204-v1",
    )
    print(result)
