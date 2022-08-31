
from datetime import timedelta

# Setar esse valor como verdadeiro quando precisar verificar o valor de retorno do SENSOR.
DEBUG: bool                 = True


# Configurações relacionadas ao arduíno
BOARD: str                  = 'arduino'
PORT: str                   = ...
PIN_DIGITAL_OUTPUT: int     = ...
PIN_DIGITAL_SENSOR: int     = ...
PIN_ANALOGIC_SENSOR: int    = ...


# Configurações a nível de execução e lógica de programa
SENSOR_DANGER_ZONE: float   = 0.5
MESSAGE_DELAY: timedelta    = timedelta(minutes=15)
LOOP_DELAY: float           = 1
LOG_MSG: str                = "[{0:%Y-%m-%d %H:%M:%S}] {1}"