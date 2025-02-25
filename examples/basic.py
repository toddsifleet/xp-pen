import asyncio

from xp_pen import Event, XPPenClient


async def on_event(event: Event):
    print(f"[XP Pen] EVENT: {event.method}:{event.value}")


if __name__ == "__main__":
    client = XPPenClient(on_event)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start())
