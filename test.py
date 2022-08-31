from multiprocessing.sharedctypes import Value
import unittest
from settings import *
from pyfirmata import serial, BOARDS

CONFIGURED_BOARD = BOARDS[BOARD]


class Arduino(unittest.TestCase):
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
        self.assertRegex(PORT, r"^COM\d{2}$", msg_err)
if __name__ == "__main__":
    unittest.main()
