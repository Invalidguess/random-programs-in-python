import pyautogui, time, pydirectinput


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pydirectinput.keyDown('d')
    time.sleep(0.5)
    pydirectinput.keyUp('d')
    pydirectinput.press(" ")
    pydirectinput.keyDown("w")
    time.sleep(0.5)
    pydirectinput.keyUp("w")
    pydirectinput.keyDown('d')
    time.sleep(0.3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    pydirectinput.press(' ')
    time.sleep(0.1)
    pydirectinput.keyUp('w')
    pydirectinput.press('q')
    pydirectinput.press('s')
    pydirectinput.press('d')
    pydirectinput.keyDown('w')
    pydirectinput.press(' ')
    time.sleep(0.2)
    pydirectinput.keyUp('w')
    pydirectinput.press('q')
    pydirectinput.keyDown('a')
    pydirectinput.keyDown(' ')
    time.sleep(0.2)
    pydirectinput.keyUp(" ")
    pydirectinput.keyUp("a")
    pydirectinput.keyDown('w')
    time.sleep(0.4)
    pydirectinput.keyUp('w')







    print("done")


if __name__ == "__main__":
    main()
