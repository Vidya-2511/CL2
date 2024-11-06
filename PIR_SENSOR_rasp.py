import RPi.GPIO as GPIO
import time

IR_SENSOR_PIN = 35
LED_PIN = 11 
buzzer_pin=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
            print("Object detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(0.5)  # Delay to avoid multiple emails in quick succession
        else:
            print("no object detected.")
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
            GPIO.output(buzzer_pin, GPIO.LOW)
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()
