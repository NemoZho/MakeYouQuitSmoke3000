import subprocess
import random
import paho.mqtt.client as mqtt

def on_message(client, obj, msg):
    print(f"TOPIC:{msg.topic}, VALUE:{msg.payload}")
    ran = random.randint(0,2)
    if ran == 0:

        subprocess.run(["aplay", "-D", "plughw:2,0", "../sound/1.wav"])
    elif ran == 1:
        subprocess.run(["aplay", "-D", "plughw:2,0", "../sound/2.wav"])
    else:
        subprocess.run(["aplay", "-D", "plughw:2,0", "../sound/3.wav"])

def main():
    # Establish connection to mqtt broker
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(host='192.168.87.2', port=1884)
    client.subscribe('violation', 0)

    try:
        client.loop_forever()
    except KeyboardInterrupt as e:
        pass

if __name__ == "__main__":
    main()

