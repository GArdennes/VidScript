import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()
channel.basic_publish(exchange='test', routing_key='test',
                      body=b'Test message.')
connection.close()