from fastapi import FastAPI

# from app import telemetry
from app import telemetry
from app.routes import health


def create_app():
    app = FastAPI()

    app.include_router(health.router)

    # Start Prometheus client
    telemetry.start(app)

    return app
