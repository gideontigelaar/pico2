from machine import ADC
import time

# TMP36 Sensor

sensor = ADC(26)

def read_temp():
    samples = [sensor.read_u16() for _ in range(10)]
    raw = sum(samples) / len(samples)
    voltage = raw * 3.3 / 65535
    temp_c = (voltage - 0.5) * 100
    return temp_c

while True:
    temp_c = read_temp()
    temp_f = (temp_c * 9/5) + 32
    print(f"Temp: {temp_c:.2f} °C / {temp_f:.2f} °F")
    time.sleep(1)