#########################################################################################
#   TODO Implementar envio de mensagem automatizada quando o gás tóxico for detectado   #
#########################################################################################

try:
    from pyfirmata import Arduino, util
except ModuleNotFoundError:
    import os
    print("módulo pyfirmata não encontrado, instalando localmente...")
    os.system("pip install pyfirmata")
finally:
    from pyfirmata import Arduino, util

from settings import *
from datetime import datetime


def setup():
    global board
    global it
    global sensor_analogico
    global sensor_digital
    global output

    board = Arduino(PORT)
    it = util.Iterator(board)
    it.start()

    sensor_analogico = board.get_pin(f"a:{PIN_ANALOGIC_SENSOR}:i")
    sensor_digital = board.get_pin(f"d:{PIN_DIGITAL_SENSOR}:i")
    output = board.get_pin(f"d:{PIN_DIGITAL_OUTPUT}:o")

    sensor_digital.enable_reporting()
    sensor_analogico.enable_reporting()

    loop()

def loop():
    import time

    next_execution_time = datetime.now()
    while True:
        time.sleep(LOOP_DELAY)

        current_time = datetime.now()
        gas_value = sensor_analogico.read()
        is_toxic = sensor_digital.read()

        if DEBUG:
            print(LOG_MSG.format(current_time, f"A: {gas_value:.3f} \t D: {is_toxic}"))
            
        if gas_value >= SENSOR_DANGER_ZONE and current_time >= next_execution_time:
            if is_toxic:
                print("\t[URGENTE] Nivel de gás tóxico está prejudicial à saúde!")
            else:
                print("\t[ALERTA] Nível de gás tóxico acima do normal.")
            next_execution_time = datetime.now() + MESSAGE_DELAY


if __name__ == '__main__':
    setup()

