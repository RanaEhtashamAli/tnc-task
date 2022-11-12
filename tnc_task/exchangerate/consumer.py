from channels.generic.websocket import AsyncWebsocketConsumer


class TNCConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('exchange_rate', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('exchange_rate', self.channel_name)

    async def send_exchange_rate(self, event):
        print(event)
        exchange_rate = event['text']
        await self.send(exchange_rate)
