
Skip to content
This repository

    Explore
    Features
    Enterprise
    Pricing

3
7

    5

skiwithpete/relaypi

relaypi/8port/script1.py
skiwithpete on Jun 13 Uploading First commit

0 contributors
executable file 60 lines (47 sloc) 1.12 KB
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  GPIO.output(3, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);  
  GPIO.output(4, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.output(27, GPIO.LOW)
  print "FIVE"
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print "SIX"
  time.sleep(SleepTimeL);
  GPIO.output(10, GPIO.LOW)
  print "SEVEN"
  time.sleep(SleepTimeL);
  GPIO.output(9, GPIO.LOW)
  print "EIGHT"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g

    Status API Training Shop Blog About Pricing 

    Â© 2015 GitHub, Inc. Terms Privacy Security Contact Help 
