import logging
from config import HOME
logger = logging.getLogger('SmartPET-Feeder Raspberry_pi')
logging.basicConfig(filename=HOME + '/smartpet.log',
                    # format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                    level=logging.INFO)
def feeded(amount: int):
    '''
    Log feeding event to log file.
    :param amount: amount of feeded food in grams.
    '''
    logger.warn(f"Feeder feed finished. Fed {amount} g.")

def add_plan(hour: int, minute: int, amount: int):
    '''
    Log adding plan event to log file
    :param hour: The feeding time in hour of new plan.
    :param minute: The feeding time in minute of new plan.
    :param amount: The feeding amount of the plan in gram unit.
    '''
    logger.warn(f"New plan feed {amount} gram at {hour}:{minute}.")

def del_plan(hour, minute):
    '''
    Log deleting plan event to log file
    :param hour: The feeding time in hour of the deleted plan.
    :param minute: The feeding time in minute of deleted plan.
    '''
    logger.warn(f"Delete plan feed at {hour}:{minute}")
