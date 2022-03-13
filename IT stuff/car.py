import pyautogui, time, pydirectinput


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pyautogui.moveTo(492, 709)
    pydirectinput.leftClick(492, 709)








    print("done")


if __name__ == "__main__":
    main()
