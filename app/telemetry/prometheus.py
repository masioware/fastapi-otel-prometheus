from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.metrics import set_meter_provider


def setup_prometheus_provider():

    # Prometheus Reader setup
    reader = PrometheusMetricReader()

    # Binding Prometheus Reader on MetricProvider
    provider = MeterProvider(metric_readers=[reader])

    # Set Prometheus as global meter provider
    set_meter_provider(provider)
