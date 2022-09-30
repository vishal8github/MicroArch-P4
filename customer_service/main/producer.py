import pika, json

params = pika.URLParameters('amqps://jbzuojol:FMYCWDxg3fKJ6IOyK1R0u4uPQcchgPjx@puffin.rmq2.cloudamqp.com/jbzuojol')

conn = pika.BlockingConnection(params)

channel = conn.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
