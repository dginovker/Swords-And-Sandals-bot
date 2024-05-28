import time

for _ in range(7):
    keyboard.send_keys('<shift>+<tab>')
    time.sleep(0.02)

keyboard.send_key('<enter>')
time.sleep(2)
keyboard.send_key('<escape>')
