from pycricbuzz import Cricbuzz
import pyttsx3
import time
import json  # only for nice printing (optional)

# ────────────────────────────────────────
#   Text-to-Speech setup
# ────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 150)       # speed
engine.setProperty('volume', 0.9)     # 0.0 to 1.0

def speak(text):
    print("\n🗣️ Speaking:", text)
    engine.say(text)
    engine.runAndWait()

# ────────────────────────────────────────
#   Main logic
# ────────────────────────────────────────
def check_and_speak_live_matches():
    try:
        c = Cricbuzz()
        matches = c.matches()

        if not matches:
            print("No matches found right now.")
            return False

        live_found = False
        spoken = []   # avoid repeating same match

        print("\n" + "═" * 60)
        print("   Live / Recent Matches from Cricbuzz   ".center(60))
        print("═" * 60 + "\n")

        for match in matches:
            mid     = match.get('id')
            mtype   = match.get('type', 'Unknown')
            series  = match.get('series_name', '')
            status  = match.get('status', '')
            mstate  = match.get('mchstate', '')   # can be 'inprogress', 'preview', etc.
            team1   = match.get('team1', {}).get('s_name', '?')
            team2   = match.get('team2', {}).get('s_name', '?')

            title = f"{team1} vs {team2}"
            if series:
                title += f" – {series}"

            # Build clean URL
            url = f"https://www.cricbuzz.com/live-cricket-scores/{mid}"

            # Print always
            print(f"Match ID   : {mid}")
            print(f"Teams      : {title}")
            print(f"Type       : {mtype}")
            print(f"Status     : {status}")
            print(f"URL        : {url}")
            print("-" * 60)

            # Decide if it's LIVE
            is_live = False
            if "live" in status.lower() or "in progress" in status.lower():
                is_live = True
            elif mstate == "inprogress":
                is_live = True

            if is_live and title not in spoken:
                live_found = True
                message = f"Live now: {title}. Status: {status}"
                speak(message)
                spoken.append(title)

        if not live_found:
            print("No live matches running at the moment.")
            speak("No live cricket matches right now.")

        return live_found

    except Exception as e:
        print("Error:", str(e))
        speak("Sorry, could not fetch cricket data right now.")
        return False


# ────────────────────────────────────────
#   Run forever – check every 3 minutes
# ────────────────────────────────────────
if __name__ == "__main__":
    print("Starting Cricbuzz Live Match Speaker...")
    speak("Starting cricket live match speaker")

    while True:
        has_live = check_and_speak_live_matches()
        print("\nWaiting 180 seconds before next check...\n")
        time.sleep(180)   # 3 minutes – polite to server