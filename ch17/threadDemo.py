import threading
import time
print('Start of program.')


def take_an_ap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=take_an_ap)
threadObj.start()

print('End of program.')
