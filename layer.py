from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from wordnik import *
import services


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if messageProtocolEntity.getType() == 'text':
            	    
            message = messageProtocolEntity.getBody()
            query =  message.split(' ', 1)[1] if len(message.split())>1 else message
	    command = message.split(' ')[0].lower() if len(message.split())>1 else None
	    
	    with open('logs.txt',"a") as f:
		f.write("\n"+str(messageProtocolEntity.getFrom()) + " ::  " + message)
	     	    
	    switch={
		  'define' : services.define,
		  'howdoi' : services.how_do_i,
		  'wiki'   : services.wiki 
		   }
	    
	    if command in switch:
		reply = switch[command](query)
	    else:
		reply = "Would you try one of these? \
                         \n 'define <word>' \n e.g. define love \
                         \n\n'howdoi <question> <language> [-n X ]' \
                         \n e.g. howdoi read file python -n 2 \
                         \n( -n argument is optional which is number of answers)\
                        \n\n'wiki <query>' \
 			\ne.g. wiki SBI \
			\n\n\n Cool isn't it ;)"

            outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                reply.encode('utf-8'),
                to = messageProtocolEntity.getFrom())

	    self.toLower(outgoingMessageProtocolEntity)
	    self.toLower(messageProtocolEntity.ack())
            self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

