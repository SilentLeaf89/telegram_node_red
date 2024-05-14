import argparse
import asyncio
import time

from telethon import TelegramClient

from core.config import project_settings


parser = argparse.ArgumentParser()
parser.add_argument("--chat", "-c", help="chat where you want to write")
parser.add_argument("--message", "-m", help="Message to be sent")
args = parser.parse_args()


async def main():
    """Send message '-m' to chat '-c' from arguments"""
    client = TelegramClient("anon", project_settings.api_id, project_settings.api_hash)
    check = False
    while not check:
        try:
            await client.connect()
            await client.send_message(args.chat, args.message)
            await client.disconnect()
            check = True
        except ConnectionError:
            time.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
