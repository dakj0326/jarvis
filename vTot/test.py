import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0 (CE0)
spi.max_speed_hz = 1350000  # Set SPI speed

# Function to read MCP3008 channel
def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])  # Send read command
    data = ((adc[1] & 3) << 8) | adc[2]  # Combine bytes to get 10-bit result
    return data

# Main loop to read mic data
try:
    print("Reading microphone data... Press Ctrl+C to stop.")
    while True:
        mic_value = read_adc(0)  # Read from CH0
        print(f"Microphone (CH0) Value: {mic_value}")
        time.sleep(0.1)  # Adjust sampling rate as needed
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    spi.close()  # Close SPI interface
