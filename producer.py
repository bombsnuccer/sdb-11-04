import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = "Hello World"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent '{message}'")

connection.close()
