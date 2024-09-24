import board
import digitalio
import time
import supervisor

from config import config
from train_board import TrainBoard
from metro_api import MetroApi, MetroApiOnFireException
from adafruit_display_text import LabelBase

from adafruit_esp32spi import adafruit_esp32spi
from adafruit_matrixportal import matrixportal

# esp = adafruit_esp32spi.ESP_SPIcontrol(SPI, ESP32_CS, ESP32_READY, ESP32_RESET)
# pyportal = matrixportal(esp=esp, external_spi= SPI, debug=PYPORTAL_DEBUG)

STATION_CODE = config['metro_station_code']
REFRESH_INTERVAL = config['refresh_interval']

def refresh_trains(stat_cde, train_group: str) -> [dict]:
    try:
        print('Refreshing now!')
        return MetroApi.fetch_train_predictions(stat_cde, train_group)
        
    except MetroApiOnFireException:
        print('WMATA Api is currently on fire. Trying again later ...')
        supervisor.reload() ; # soft reset
        return None

train_group = config['train_group_1']
active_station = config['metro_station_code']

train_board = TrainBoard(lambda: refresh_trains(active_station, train_group))

while True:
    try:
        train_board.refresh()
        time.sleep(REFRESH_INTERVAL)
        train_group = config['train_group_1'] if train_group == config['train_group_2'] else config['train_group_2']
        active_station = config['metro_station_code'] if active_station == config['metro_station_code_secondary'] else config['metro_station_code_secondary']
        print(active_station)
    except:
        print("Caught Error")
        train_board.refresh()
        