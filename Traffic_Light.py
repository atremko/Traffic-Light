from gpiozero import LED
from time import sleep

ledGreen = LED(17)
ledYellow = LED(27)
ledRed = LED(18)

try:
    # Start an infinite loop to toggle the Traffic Light
    while True:
        # Turn on the Green LED and print a message to the console
        ledGreen.on()
        print('GREEN LED ON')

        # Wait for 10 seconds with the Green LED on
        sleep(10)

        # Turn off the Green LED and print a message to the console
        ledGreen.off()
        print('GREEN LED OFF')
        
        # Turn on the Yellow LED and print a message to the console
        ledYellow.on()
        print('YELLOW LED ON')

        # Wait for 3 seconds with the Yellow LED on
        sleep(3)

        # Turn off the Yellow LED and print a message to the console
        ledYellow.off()
        print('YELLOW LED OFF')
        
        # Turn on the Red LED and print a message to the console
        ledRed.on()
        print('RED LED ON')

        # Wait for 10 seconds with the Red LED on
        sleep(10)

        # Turn off the Red LED and print a message to the console
        ledRed.off()
        print('RED LED OFF')

except KeyboardInterrupt:
    # Breaks loop by hitting CTRL + C 
    pass
