import time

from mitmproxy import options
from mitmproxy.tools.dump import DumpMaster
import asyncio
import logging
from mitmproxy.addonmanager import Loader


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("requests.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
finished = False

class RequestLogger:
    def load(self, loader: Loader):
        loader.add_option(
            name="listen_host", typespec=str, default="127.0.0.1",
            help="Proxy listen address"
        )
        loader.add_option(
            name="listen_port", typespec=int, default=8080,
            help="Proxy listen port"
        )
    def request(self, flow):
        global finished
        request = flow.request
        for header, value in request.headers.items():
            if header == "authorization" and "discord.com" in request.url:
                logger.info("---------------------------------------")
                logger.info(f"DETECTED TOKEN DISCORD: {value}")
                logger.info("---------------------------------------")
                with open("token.txt", "w") as file:
                    file.write(value)
                finished = True
            else:
                logger.info(f"URL: {flow.request.url}")
                logger.info("Request Headers:")
                for key, value in flow.request.headers.items():
                    logger.info(f"{key}: {value}")
                logger.info("\n")

async def start():
    global finished
    opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
    pconf = opts.keys()
    m = DumpMaster(opts)

    m.addons.add(RequestLogger())

    try:
        asyncio.create_task(m.run())
        while finished == False:
            await asyncio.sleep(1)
        logger.info("Closing TokenGraber Proxy")
        m.shutdown()


    except SystemExit:
        ...


if __name__ == "__main__":
    asyncio.run(start())
    start()
