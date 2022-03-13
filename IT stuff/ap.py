import pyautogui, time, pydirectinput, pynput, keyboard


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pydirectinput.press('/')









    print("done")


if __name__ == "__main__":
    main()
