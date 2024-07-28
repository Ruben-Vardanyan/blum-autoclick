'''
28/07/2024 
Author Ruben Vardanyan
Blum-autoclicker version 1.0
'''


import time
import pyautogui
import pygetwindow as gw



# telegram_window = gw.getWindowsWithTitle('Document - Google Chrome')[0]
telegram_window = gw.getWindowsWithTitle('TelegramDesktop')[0]


if telegram_window:
   
    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    start_time = time.time()
    duration = 30  # Run for 20 seconds

    while time.time() - start_time < duration:
        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size

        for y in range(0, height, 15):
            for x in range(0, width, 15):
            
                r, g, b = scrn.getpixel((x, y))
                # r in range(80, 160)) and (g in range(150, 255)) and (b in range(0, 125)
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    pyautogui.click(screen_x + 4, screen_y + 10)
                    # pyautogui.click(screen_x + 4, screen_y + 5)

                    time.sleep(0.001)
                    break
                 
