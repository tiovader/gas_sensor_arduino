import main as _
from multiprocessing.sharedctypes import Value
import unittest
from settings import *
from pyfirmata import serial, BOARDS
from telegram_hook import send_message


CONFIGURED_BOARD = BOARDS[BOARD]

class ProjectTest(unittest.TestCase):
    def test_has_valid_digital_sensor(self):
        self.assertIsInstance(PIN_DIGITAL_SENSOR, int)
        self.assertTrue(PIN_DIGITAL_SENSOR in CONFIGURED_BOARD["digital"],
                        "O pino digital para o sensor não está definido corretamente.")

    def test_has_valid_digital_output(self):
        self.assertIsInstance(PIN_DIGITAL_OUTPUT, int)
        self.assertTrue(PIN_DIGITAL_OUTPUT in CONFIGURED_BOARD["digital"],
                        "O pino digital para o output [LED/LAMPADA] não está definido corretamente.")

    def test_has_valid_analogic_pins(self):
        self.assertIsInstance(PIN_ANALOGIC_SENSOR, int)
        self.assertTrue(PIN_ANALOGIC_SENSOR in CONFIGURED_BOARD["analog"],
                        "O pino analógico para o sensor não está definido corretamente.")

    def test_has_valid_board(self):
        self.assertIsInstance(BOARD, str)
        self.assertTrue(BOARD in BOARDS)

    def test_has_arduino_connected(self):
        from pyfirmata import Arduino

        conn = True
        try:
            Arduino(PORT)
        except (serial.SerialException, ValueError):
            conn = False
        self.assertTrue(
            conn, "A porta informada não está conectada a um Arduíno.")

    def test_has_valid_port(self):
        msg_err = "A porta de conexão fornecida não é válida!"
        self.assertIsInstance(PORT, str, msg_err)
        self.assertRegex(PORT, r"^COM\d{1,2}$", msg_err)
    
    def test_has_valid_telegram_credentials(self):
        test_msg = "*📋 TESTE UNITÁRIO*: O bot está configurado corretamente para enviar mensagens!"
        response = send_message(test_msg)
        self.assertEqual(response.status_code, 200, "As credenciais do TELEGRAM.BOT não estão setadas corretamente.")

if __name__ == "__main__":
    unittest.main()
