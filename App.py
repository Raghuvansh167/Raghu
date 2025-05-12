import time
import datetime
import threading
from playsound import playsound  # Make sure you have an 'alarm.mp3' file

def play_sound():
    try:
        playsound("alarm.mp3")  # Replace with path to your own mp3 file
    except Exception as e:
        print("Sound error:", e)

def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("\n⏰ Alarm ringing! Wake up!")
            play_sound()
            break
        time.sleep(10)

def countdown_timer(seconds):
    print(f"⏳ Timer started for {seconds} seconds.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"Time left: {mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Timer finished!")
    play_sound()

def main():
    print("===== Python Alarm Clock & Timer =====")
    print("1. Set Alarm")
    print("2. Start Timer")
    choice = input("Choose (1 or 2): ")

    if choice == '1':
        alarm_time = input("Enter alarm time in HH:MM format (24-hour): ")
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M")
            threading.Thread(target=alarm_clock, args=(alarm_time,)).start()
        except ValueError:
            print("Invalid time format.")
    elif choice == '2':
        try:
            total_seconds = int(input("Enter time in seconds: "))
            threading.Thread(target=countdown_timer, args=(total_seconds,)).start()
        except ValueError:
            print("Invalid number.")
    else:
        print("Invalid choice.")

if name == "__main__":
    main()
