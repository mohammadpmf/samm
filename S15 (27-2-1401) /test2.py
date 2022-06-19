from time import sleep
import threading

def countto10():
    for i in range(1,11):
        print(i)
        sleep(1)

def print_alaki():
    for i in range(10):
        print("alaki")

arad = threading.Thread(target=countto10)
sepehr = threading.Thread(target=countto10)
amirmahdi = threading.Thread(target=countto10)
mohammad = threading.Thread(target=print_alaki)
arad.start()
sepehr.start()
amirmahdi.start()
mohammad.start()

# ۱۰ ثانیه اجرایش طول میکشد.