import pyautogui, time, pydirectinput


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pydirectinput.keyDown('d')
    time.sleep(6.6)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(0.6)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(3.4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(0.6)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(8)
    pydirectinput.keyUp('d')


    print("done")


if __name__ == "__main__":
    main()
