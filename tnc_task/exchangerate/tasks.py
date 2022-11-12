from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .utils import get_exchange_rate
import json

channel_layer = get_channel_layer()


@shared_task
def exchange_rate_task():
    exchange_rate = get_exchange_rate()
    async_to_sync(channel_layer.group_send)('exchange_rate', {'type': 'send_exchange_rate', 'text': json.dumps(exchange_rate)})
