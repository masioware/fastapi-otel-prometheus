from fastapi import FastAPI

from app.telemetry import prometheus
from app.telemetry.status_code_middleware import StatusCodeMeterMiddleware

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.metrics import get_meter_provider
from prometheus_client import make_asgi_app


# Add prometheus asgi middleware to route /metrics requests
def start(app: FastAPI):

    # Setup Promethues provider
    prometheus.setup_prometheus_provider()
    provider = get_meter_provider()

    # Instrumenting FastAPI endpoints
    app.add_middleware(StatusCodeMeterMiddleware)
    FastAPIInstrumentor.instrument_app(app, meter_provider=provider)

    # Creating ASGI enpoint for Prometheus
    metrics_app = make_asgi_app()
    app.mount("/metrics", metrics_app)
