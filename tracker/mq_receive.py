import asyncio
import aio_pika

async def main():
    # Establish connection
    connection = await aio_pika.connect_robust("amqp://rabbitmq:rabbitmq@localhost/projectx")

    # Creating a channel
    async with connection.channel() as channel:
        # Declaring a queue
        queue = await channel.declare_queue('hello', durable=True)

        # Define a callback function for consuming messages
        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                print(f" [x] Received {message.body.decode()}")

        # Set up the consumer
        await queue.consume(on_message)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
