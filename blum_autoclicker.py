'''
28/07/2024 
Author Ruben Vardanyan
Blum-autoclicker version 1.2
'''


import time
import pyautogui
import pygetwindow as gw



#telegram_window = gw.getWindowsWithTitle('Document - Google Chrome')[0]
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
    duration = 30  # Run for 30 seconds

    while time.time() - start_time < duration:
        
        # getting telegram window details
        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))
        
        # getting telegram window sizes
        width, height = scrn.size

        # coordinating the screen 
        
        for x in range(0, width, 15):# 15 
            for y in range(0, int(height/2), 15):# 15  
                r, g, b = scrn.getpixel((x, y))
                if 80 <= r <= 160 and 160 <= g <= 210 and 30 <= b <= 120:
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    pyautogui.click(screen_x +2, screen_y + 8)
                    time.sleep(0.004)
                    break
                