import pyautogui, time, pydirectinput


def main():
    pyautogui.FAILSAFE = True

    print("Starting", end="")
    for i in range(0, 1):
        print(".")
        time.sleep(1)
    print("Go")

    pydirectinput.moveTo(1920, 1080)








    print("done")


if __name__ == "__main__":
    main()
