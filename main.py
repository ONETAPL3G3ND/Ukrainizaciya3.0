import threading
import time
import tokengraber
import asyncio
import os
import logging
from ProxySetup import ProxySetup
import DiscordManager
import LaunchingUkrainizaciya

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("requests.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


async def main():
    logger.info("Proxy installation.")

    proxy = "http=localhost:8080;https=localhost:8080"
    ProxySetup.set_proxy(proxy)

    logger.info("The proxy is installed and the settings are saved.")

    await tokengraber.start()

    while os.path.exists("token.txt") == False:
        time.sleep(1)

    logger.info("Deactivating a proxy.")
    ProxySetup.deactivate_proxy()

    logger.info("Starting Discord Bot")


if __name__ == "__main__":
    asyncio.run(main())
    logger.info("Build Thread")
    thread = threading.Thread(target=LaunchingUkrainizaciya.start)
    logger.info("Starting Thread")
    thread.start()
    DiscordManager.Start()