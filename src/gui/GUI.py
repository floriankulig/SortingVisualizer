import turtle
from tkinter import Tk, Button
from tkinter.ttk import Combobox
from sorts.merge_sort import merge_sort_animations
from sorts.quick_sort import quick_sort_animations
from sorts.bubble_sort import bubble_sort_animations
import random as rd

PRIMARY_COLOR = "#2a6fbe"  # blue
SECONDARY_COLOR = "#ac1207"  # red
TERTIARY_COLOR = "#dddd37"  # yellow
LAST_MERGE_COLOR = "#7f2d97"  # purple
FINAL_COLOR = "#08a110"  # green
ARRAY_SIZE = 100
# higher ANIMATION_SPEED to make animations faster (has to be int)
# minimum is 1; default is 3
ANIMATION_SPEED = 3


class Bar(turtle.Turtle):
    '''value is for correct alignment calculation with top'''
    value = 0

    def __repr__(self):
        return f"{self.value}"


class Gui:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Sorting Algorithms Visualizer by © Florian Kulig")
        self.screen.setup(width=1200, height=800)
        self.screen.bgcolor("#f5f5f5")
        self.screen.tracer(0, 0)
        self.array = list()
        self.bars = [Bar() for i in range(ARRAY_SIZE)]
        self.algorithms = ['Mergesort', 'Quicksort', 'Bubblesort']
        self.bar_padding = 10
        self.start_posX = -500  # where the bars start visually
        self.random_bars = False
        self.ui_window()

        # display bars for the first time
        self.array = [rd.randint(10, 390) for j in range(ARRAY_SIZE)]
        self.random_bars = True
        for i, bar in enumerate(self.bars):
            value = self.array[i]
            bar.value = value
            bar.shape("square")
            bar.color(PRIMARY_COLOR)
            bar.speed(0)
            bar.shapesize(
                stretch_wid=bar.value/10, stretch_len=0.3, outline=0)
            bar.penup()
            bar.goto(self.start_posX + (i*self.bar_padding), 400-bar.value)
        turtle.update()
        self.random_bars = False

    def run(self):
        turtle.update()
        self.screen.mainloop()

    def ui_window(self):
        # make checkbox window for user to choose from different algorithms
        self.menu = Tk()
        self.menu.title("Algorithmus wählen!")
        self.menu.geometry('300x200')
        btn = Button(self.menu, text='Neue Liste generieren!',
                     command=self.new_array)
        visualizer = Button(self.menu, text='Visualisieren!',
                            command=self.process_user_input)
        self.selections = Combobox(self.menu)
        self.selections['values'] = self.algorithms
        self.selections.current(0)
        btn.pack(pady=15, padx=15)
        self.selections.pack(padx=15)
        visualizer.pack(padx=15, pady=40)

    def process_user_input(self):
        value = self.selections.get()
        self.menu.destroy()
        if self.random_bars:
            self.ui_window()
        elif value in self.algorithms:
            self.algorithm_on_choice(value)

    def algorithm_on_choice(self, value):
        if value == 'Mergesort':
            self.mergesort()
        elif value == 'Quicksort':
            self.quicksort()
        elif value == 'Bubblesort':
            self.bubblesort()
        elif value == 'Heapsort':
            self.heapsort()

    def sort_finish(self):
        # visualize that array is sorted
        for bar in self.bars:
            bar.color(FINAL_COLOR)
        turtle.update()
        self.ui_window()

    # small unit test for algorithms
    def checkSort(self, array):
        return True if sorted(self.array) == array else False

    def new_array(self):
        self.random_bars = True
        self.array = [rd.randint(10, 390) for j in range(ARRAY_SIZE)]
        for i, bar in enumerate(self.bars):
            value = self.array[i]
            bar.value = value
            bar.shape("square")
            bar.color(PRIMARY_COLOR)
            bar.speed(0)
            bar.shapesize(
                stretch_wid=bar.value/10, stretch_len=0.3, outline=0)
            bar.penup()
            bar.goto(self.start_posX + (i*self.bar_padding), 400-bar.value)
            if i % 2 == 0:
                turtle.update()
        turtle.update()
        self.random_bars = False

    def mergesort(self):
        animations = merge_sort_animations(self.array)
        for i in range(len(animations)):
            color_change = True if not i % 3 == 2 else False
            last_merge = i > len(animations) - (len(self.array)*3)
            if color_change:
                bar_one_idx, bar_two_idx = animations[i]
                # Check if color has to be reset
                if i % 3 == 0:
                    # check if values are in wrong order (color red if so)
                    if self.bars[bar_one_idx].value > self.bars[
                            bar_two_idx].value:
                        color = SECONDARY_COLOR
                    else:
                        color = FINAL_COLOR
                else:
                    color = PRIMARY_COLOR
                # Style the bars with new color
                if last_merge:
                    self.bars[bar_one_idx].color(LAST_MERGE_COLOR)
                else:
                    self.bars[bar_one_idx].color(color)
                self.bars[bar_two_idx].color(color)
            else:
                # ... or their new height
                idx, new_height = animations[i]
                self.bars[idx].value = new_height
                self.bars[idx].shapesize(
                    stretch_wid=new_height/10, stretch_len=0.3)
                # align bar again with top since it has new value
                self.bars[idx].goto(
                    self.bars[idx].xcor(), 400-self.bars[idx].value)

                if last_merge:
                    self.bars[idx].color(LAST_MERGE_COLOR)

            # we don't update the screen every iteration
            # to save performance and animation time
            if i % ANIMATION_SPEED == 0:
                turtle.update()

        self.sort_finish()

    def quicksort(self):
        animations = quick_sort_animations(self.array)
        for i in range(len(animations)):
            idx1, height1, idx2, height2 = animations[i]
            # color both bars
            color = FINAL_COLOR if height1 <= height2 else SECONDARY_COLOR
            self.bars[idx1].color(color)
            self.bars[idx2].color(color)
            # Style both bars
            self.bars[idx1].value = height1
            self.bars[idx2].value = height2
            # give bars new height
            self.bars[idx1].shapesize(
                stretch_wid=height1/10, stretch_len=0.3)
            self.bars[idx2].shapesize(
                stretch_wid=height2/10, stretch_len=0.3)
            # align bars again with top since it has new value
            self.bars[idx1].goto(
                self.bars[idx1].xcor(), 400-self.bars[idx1].value)
            self.bars[idx2].goto(
                self.bars[idx2].xcor(), 400-self.bars[idx2].value)

            # update already here in order to see the color change
            if i % ANIMATION_SPEED == 0:
                turtle.update()

            # revert color of the bars
            self.bars[idx1].color(PRIMARY_COLOR)
            self.bars[idx2].color(PRIMARY_COLOR)
        self.sort_finish()

    def bubblesort(self):
        animations = bubble_sort_animations(self.array)
        for i in range(len(animations)):
            idx1, height1, idx2, height2 = animations[i]
            bar_sorted = height1 == 0 and height2 == 0 and idx1 == idx2
            if not bar_sorted:
                # color both bars
                color = FINAL_COLOR if height1 <= height2 else SECONDARY_COLOR
                self.bars[idx1].color(color)
                self.bars[idx2].color(color)
                # Style both bars
                self.bars[idx1].value = height1
                self.bars[idx2].value = height2
                # give bars new height
                self.bars[idx1].shapesize(
                    stretch_wid=height1/10, stretch_len=0.3)
                self.bars[idx2].shapesize(
                    stretch_wid=height2/10, stretch_len=0.3)
                # align bars again with top since it has new value
                self.bars[idx1].goto(
                    self.bars[idx1].xcor(), 400-self.bars[idx1].value)
                self.bars[idx2].goto(
                    self.bars[idx2].xcor(), 400-self.bars[idx2].value)

                # update already here in order to see the color change
                if i % ANIMATION_SPEED == 0:
                    turtle.update()

                # revert color of the bars
                self.bars[idx1].color(PRIMARY_COLOR)
                self.bars[idx2].color(PRIMARY_COLOR)
            else:
                self.bars[idx1].color(LAST_MERGE_COLOR)
        self.sort_finish()
