"""Basic stuff for testing things"""

___title___        = "JustTesting"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = ["homescreen", "wifi", "http", "sleep", "app", "buttons"]
___bootstrapped___ = False
___launchable___   = True

import ugfx_helper, uos, wifi, ugfx, http, time, sleep, app, sys, database, buttons
from tilda import Buttons
from homescreen import *
from dialogs import *



def write_some_text():
    ugfx.clear(ugfx.html_color(0x000000))
    ugfx.orientation(270)
    ugfx.text(5, 5, "Text here", ugfx.WHITE)
    ugfx.text(5, 25, "More here", ugfx.WHITE)
    ugfx.text(5, 45, "Last line", ugfx.WHITE)


def a_was_pushed():
    ugfx.clear(ugfx.html_color(0x000000))
    ugfx.orientation(270)
    ugfx.text(5,5, "You pressed A", ugfx.WHITE)
    ugfx.text(5,45, "Press MENU to exit", ugfx.WHITE)
    while True:
        if buttons.is_triggered(Buttons.BTN_Menu):
            break


def main():

    init()

    start()

    write_some_text()

    while True:
        if buttons.is_triggered(Buttons.BTN_A):
            a_was_pushed():

    app.restart_to_default()


main()