
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


# Configurações para o Telegram Bot
# Essas variaveis acima do WITH, tem que está setada em um json nomeado .secrets
TOKEN: str                  = ...
CHAT_ID: int                = ...
with open(".secrets.json", "r") as file:
    import json    
    __secrets = json.load(file)
    globals().update(__secrets)
    del json

MSG_ALERTA = "*⚠ ALERTA:* Tenha cuidado o nível de gás tóxico no ambiente está acima do normal, podendo haver riscos à saúde humana. ⚠"
MSG_PERIGO = "☠ *PERIGO:* O nível de gás tóxico no ambiente está *ELEVADO*, totalmente prejudicial à saúde humana.! ☠"
