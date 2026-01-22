import webbrowser
import pyautogui
import time

# ---------------- CONFIG ----------------
STAKE_URL = "https://stake.us/?tab=dailyBonus&currency=btc&modal=wallet"
TAB_COUNT = 7
TAB_WAIT = 1.15
PAGE_LOAD_WAIT = 20
FOCUS_WAIT = 1.15
DAILY_WAIT = (24 * 60 * 60) + 30
CLAIM_BUTTON_IMAGE = "button.png"  # Screenshot of the "Claim Bonus" button

# ---------------- HELPER FUNCTION ----------------
def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        hrs, rem = divmod(remaining, 3600)
        mins, secs = divmod(rem, 60)
        print(f"\r[INFO] Next bonus in {hrs:02d}:{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
    print("\r[INFO] Time to claim the daily bonus!           ")

def move_and_click_button():
    print("[INFO] Searching for 'Claim Bonus' button...")
    button_location = None
    while button_location is None:
        button_location = pyautogui.locateOnScreen(CLAIM_BUTTON_IMAGE, confidence=0.8)
        if button_location is None:
            print("[WARN] Button not found, retrying in 2 seconds...")
            time.sleep(2)
    center_x, center_y = pyautogui.center(button_location)
    print(f"[INFO] Moving mouse to button at ({center_x}, {center_y})...")
    pyautogui.moveTo(center_x, center_y, duration=0.8)  # smooth movement
    pyautogui.click()
    print("[SUCCESS] 'Claim Bonus' clicked ✅")

# ---------------- MAIN LOOP ----------------
while True:
    print("\n[INFO] Opening Stake website...")
    webbrowser.open(STAKE_URL)
    time.sleep(PAGE_LOAD_WAIT)

    # ---------------- FOCUS BROWSER ----------------
    screen_width, screen_height = pyautogui.size()
    focus_x = screen_width // 2
    focus_y = screen_height // 2 + 100
    print("[INFO] Focusing browser window...")
    pyautogui.moveTo(focus_x, focus_y, duration=0.3)
    time.sleep(FOCUS_WAIT)

    # ---------------- FIRST TAB NAVIGATION ----------------
    print(f"[INFO] Pressing TAB {TAB_COUNT} times...")
    for i in range(TAB_COUNT):
        pyautogui.press('tab')
        print(f"[INFO] Tab {i + 1}/{TAB_COUNT}")
        time.sleep(TAB_WAIT)

    print("[INFO] Pressing Enter...")
    pyautogui.press('enter')

    # ---------------- MOVE MOUSE AND CLICK BUTTON ----------------
    move_and_click_button()

    # ---------------- START COUNTDOWN ----------------
    countdown(DAILY_WAIT)
