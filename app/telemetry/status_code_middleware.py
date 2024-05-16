from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from opentelemetry.metrics import get_meter

# Define http status code meter
meter = get_meter(__name__)
status_code_counter = meter.create_counter(
    name='status_code', unit='1',
    description='Http response status code'
)


class StatusCodeMeterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Capture status code
        self.count_status_code(request, response)

        return response

    def count_status_code(self, request: Request, response: Response):
        status_code_counter.add(1, {
            "status_code": response.status_code,
            "route": request.url.path
        })
