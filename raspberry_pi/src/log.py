import logging
from config import HOME
logger = logging.getLogger('SmartPET-Feeder Raspberry_pi')
logging.basicConfig(filename=HOME + '/smartpet.log',
                    # format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                    level=logging.INFO)
def feeded(amount: int):
    logger.warn(f"Feeder feed finished. Feeded {amount} g.")

def add_plan(hour: int, minute: int, amount: int):
    logger.warn(f"New plan feed {amount} gram at {hour}:{minute}.")

def del_plan(hour, minute):
    logger.warn(f"Delete plan feed at {hour}:{minute}")
