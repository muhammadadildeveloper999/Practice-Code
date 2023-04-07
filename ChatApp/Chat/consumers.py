from channels.consumer  import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import asyncio
import json

# SyncConsumer

class MySyncConsumer(SyncConsumer):    
    def websocket_connect(self,  event):
            print('Websocket Connected...',event)
            print('Channel Layer...', self.channel_layer)
        #     channels layer get from a project
            print('Channel Name..', self.channel_name)
        #     channels layer get from a project
            self.group_name = self.scope['url_route']['kwargs']['groupkaname']
            print('Group name', self.group_name)
            # Name
            async_to_sync(self.channel_layer.group_add)(
                   self.group_name , # group ame
                   self.channel_name
                   )
            
            self.send({
                'type': 'websocket.accept'
            })
    
    def websocket_receive(self,  event):
            print('Messaged Recieved From Client...',  event['text'])
            
            async_to_sync(self.channel_layer.group_send)(self.group_name,{
                   'type' : 'chat.message',
                   'message' : event['text']
            })
    
    def chat_message(self, event):
        print('Event...', event)   
        print('Actual Data...', event['message'])   
        self.send({
                'type' : 'websocket.send',
                'text' : event['message']
        })
    def websocket_disconnect(self,  event):
            print('websocket Disconnected....',event)
            print('Channel Layer...', self.channel_layer)
        #     channels layer get from a project
            print('Channel Name..', self.channel_name)
        #     channels layer name get from a project
            async_to_sync(self.channel_layer.group_discard)(
                        self.group_name, 
                        self.channel_name)
            raise StopConsumer()

# AsyncConsumer
class MyAsyncConsumer(AsyncConsumer):    
    async def websocket_connect(self,  event):
            print('Websocket Connected...',event)
            print('Channel Layer...', self.channel_layer)
        #     channels layer get from a project
            print('Channel Name..', self.channel_name)
        #     channels layer get from a project
            self.group_name = self.scope['url_route']['kwargs']['groupkaname']
            print('Group name', self.group_name)
            # Name
            await  self.channel_layer.group_add(
                   self.group_name , # group ame
                   self.channel_name
                   )
            
            await self.send({
                'type': 'websocket.accept'
            })
    
    async def websocket_receive(self,  event):
            print('Messaged Recieved From Client...',  event['text'])
            
            await self.channel_layer.group_send(self.group_name,{
                   'type' : 'chat.message',
                   'message' : event['text']
            })
    
    async def chat_message(self, event):
        print('Event...', event)   
        print('Actual Data...', event['message'])   
        await self.send({
                'type' : 'websocket.send',
                'text' : event['message']
        })
    async def websocket_disconnect(self,  event):
            print('websocket Disconnected....',event)
            print('Channel Layer...', self.channel_layer)
        #     channels layer get from a project
            print('Channel Name..', self.channel_name)
        #     channels layer name get from a project
            await self.channel_layer.group_discard(
                        self.group_name, 
                        self.channel_name)
            raise StopConsumer()