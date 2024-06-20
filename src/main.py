from config.logger import logger
from service.process import start
from config.setup import setup


def main():
    logger.log("info", "Starting simulator...")
    instances, module, SIMULATION_INTERVAL, SENDING_INTERVAL, OPEN_WHEATHER_INTERVAL = setup()

    logger.log("info", "Starting simulation process...")
    start(instances, module, SIMULATION_INTERVAL, SENDING_INTERVAL, OPEN_WHEATHER_INTERVAL)


if __name__ == "__main__":
    main()
