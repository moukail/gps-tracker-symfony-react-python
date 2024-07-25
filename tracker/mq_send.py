import asyncio
import aio_pika

async def main():
    # Establish connection
    connection = await aio_pika.connect_robust("amqp://rabbitmq:rabbitmq@localhost/projectx")

    # Creating a channel
    async with connection.channel() as channel:
        # Declaring a queue
        queue = await channel.declare_queue('hello', durable=True)

        # Sending a message
        message_body = 'Hello RabbitMQ with aio-pika!'
        await channel.default_exchange.publish(
            aio_pika.Message(body=message_body.encode()),
            routing_key=queue.name,
        )

        print(" [x] Sent 'Hello RabbitMQ with aio-pika!'")

    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())