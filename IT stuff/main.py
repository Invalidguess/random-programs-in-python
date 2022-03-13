import pyautogui, time, pydirectinput


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('w')
    pydirectinput.keyDown(' ')
    time.sleep(0.2)
    pydirectinput.keyUp('w')
    pydirectinput.keyUp(' ')
    pydirectinput.keyDown('w')
    pydirectinput.keyDown(' ')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyUp(' ')
    pydirectinput.keyDown('w')
    pydirectinput.keyDown(' ')
    time.sleep(0.2)
    pydirectinput.keyUp(' ')
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(0.7)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(0.5)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.7)
    pydirectinput.keyUp('w')

    print("done")


if __name__ == "__main__":
    main()
