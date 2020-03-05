from gui.GUI import Gui
import time


def main():
    gui = Gui()
    gui.new_array()
    time.sleep(3)
    gui.merge_sort()
    # gui.quicksort()
    gui.run()


if __name__ == "__main__":
    main()
