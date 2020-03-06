from gui.GUI import Gui
import time


def main():
    gui = Gui()
    time.sleep(3)
    gui.merge_sort()
    time.sleep(2)
    gui.new_array()
    time.sleep(3)
    gui.quicksort()
    gui.run()


if __name__ == "__main__":
    main()
