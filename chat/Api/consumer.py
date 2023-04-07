    from channels.generic.websocket import JsonWebsocketConsumer
    from channels.exceptions import DenyConnection
    
    from django.utils import timezone
    from django.contrib.auth.models import AnonymousUser
    from asgiref.sync import async_to_sync
    
    
    import logging
    logger = logging.getLogger("project")
    
    
    class SystemConsumer(JsonWebsocketConsumer):
        groups = ["WSbroadcast","WSsystemAPP"]
        
        def connect(self):
            # Called on connection.
            if self.scope['user'] == AnonymousUser():
               raise DenyConnection("Invalid User")
    
            async_to_sync(self.channel_layer.group_add)(
                    self.groups[0],
                    self.channel_name
                )
            
            if self.scope['user'].is_authenticated:
                try:
                    # To accept the connection call:
                    self.accept()
                    print('Websocket accepted: ' + str(self.scope))
                except Exception as ex:
                    print("Error accepting connection " + str(ex))
            else:
                raise DenyConnection("User not authenticated")
                
        def disconnect(self, close_code):
            # Called when the socket closes
            print('Websocket disconnected: ' + str(close_code))
            pass