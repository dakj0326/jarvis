import os

def check_voltage():
    try:
        # Read the voltage from Raspberry Pi system info
        with open("/sys/class/power_supply/rpi-poe/voltage_now", "r") as f:
            voltage = int(f.read().strip()) / 1000000  # Convert from microvolts to volts
            print(f"Measured System Voltage: {voltage}V")
    except FileNotFoundError:
        print("Could not read voltage from system. This might not work on all Raspberry Pi models.")

check_voltage()
