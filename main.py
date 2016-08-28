#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import pygubu
from tkinter import ttk


class Bingo:
    def __init__(self, master):
        self.master = master
        # 1: Create a builder
        self.builder = pygubu.Builder()

        # 2: Load an ui file
        self.builder.add_from_file("sbr.ui")

        # 3: Create the widget using a master as parent
        self.frame = self.builder.get_object("frame", master)
        self.button_1 = self.builder.get_object("Button_1", master)
        self.button_2 = self.builder.get_object("Button_2", master)
        self.button_3 = self.builder.get_object("Button_3", master)
        self.button_4 = self.builder.get_object("Button_4", master)
        self.button_5 = self.builder.get_object("Button_5", master)
        self.button_6 = self.builder.get_object("Button_6", master)
        self.button_7 = self.builder.get_object("Button_7", master)
        self.button_8 = self.builder.get_object("Button_8", master)
        self.button_9 = self.builder.get_object("Button_9", master)
        self.button_10 = self.builder.get_object("Button_10", master)
        self.button_11 = self.builder.get_object("Button_11", master)
        self.button_12 = self.builder.get_object("Button_12", master)
        self.button_13 = self.builder.get_object("Button_13", master)
        self.button_14 = self.builder.get_object("Button_14", master)
        self.button_15 = self.builder.get_object("Button_15", master)
        self.button_16 = self.builder.get_object("Button_16", master)
        self.button_17 = self.builder.get_object("Button_17", master)
        self.button_18 = self.builder.get_object("Button_18", master)
        self.button_19 = self.builder.get_object("Button_19", master)
        self.button_20 = self.builder.get_object("Button_20", master)
        self.score_meter = self.builder.get_object("score", master)

        self.current_score = int(self.score_meter["text"])

        self.builder.connect_callbacks(self)

        self._setup_styles()

    def _setup_styles(self):

        s = ttk.Style()
        s.configure("TFrame", background="#004080")
        s.configure("TButton", foreground="#004080")
        s.configure("TLabelFrame", foreground="#004080")

    def bingo_alert(self):
        if self.current_score == 20:
            messagebox.showinfo("You win!", "Bingo! This scammer is certainly messing with you...")
        elif self.current_score == 10:
            messagebox.showinfo("Half way there!", "You are 10 steps behind from ratting out the scammer")
        else:
            pass

    def on_button_1_click(self):
        self.button_1["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_2_click(self):
        self.button_2["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_3_click(self):
        self.button_3["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_4_click(self):
        self.button_4["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_5_click(self):
        self.button_5["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_6_click(self):
        self.button_6["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_7_click(self):
        self.button_7["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_8_click(self):
        self.button_8["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_9_click(self):
        self.button_9["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_10_click(self):
        self.button_10["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_11_click(self):
        self.button_11["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_12_click(self):
        self.button_12["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_13_click(self):
        self.button_13["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_14_click(self):
        self.button_14["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_15_click(self):
        self.button_15["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_16_click(self):
        self.button_16["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_17_click(self):
        self.button_17["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_18_click(self):
        self.button_18["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_19_click(self):
        self.button_19["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_20_click(self):
        self.button_20["state"] = "disabled"
        self.score_meter["text"] = self.current_score + 1
        self.current_score = int(self.score_meter["text"])
        self.bingo_alert()

    def on_button_quit_click(self):
        self.master.quit()


if __name__ == "__main__":
    # app info
    window_title = "Scammer Bingo - Python Edition"
    window_icon = "resx/favicon.ico"

    root = tk.Tk()
    app = Bingo(root)
    app.master.title(window_title)
    root.iconbitmap(default=window_icon)
    root.mainloop()
