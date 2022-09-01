#########################################################################################
#   TODO Implementar envio de mensagem automatizada quando o gás tóxico for detectado   #
#########################################################################################

try:
    import pyfirmata
    import requests
except:
    import os
    print("[MAIN.SCRIPT] Installing dependency from project...")
    os.system("python -m pip -q install -r ./requirements.txt")


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
                send_message(MSG_PERIGO)
            else:
                send_message(MSG_ALERTA)

            next_execution_time = datetime.now() + MESSAGE_DELAY


if __name__ == '__main__':
    from pyfirmata import Arduino, util
    from settings import *
    from datetime import datetime
    from telegram_hook import send_message

    setup()
