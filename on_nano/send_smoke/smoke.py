import time
import argparse
import RPi.GPIO as GPIO
import time

import psutil
import paho.mqtt.client as mqtt

def main():
    input_pin = 18
    # Establish connection to mqtt broker
    client = mqtt.Client()
    client.connect(host='192.168.87.2', port=1883)        
    client.loop_start()
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin

    # Intervally send topic message
    try:
        while True:
            value = GPIO.input(input_pin)

            print(value)
            if value == 1:
                payload = True
            else:
                payload = False
            client.publish(topic='smoke', payload=payload)      
            time.sleep(1)
    except KeyboardInterrupt as e:
        client.loop_stop()

if __name__ == '__main__':
    main()


