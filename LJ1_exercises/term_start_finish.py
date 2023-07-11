import requests
from icalendar import Calendar

def fetch_calendar_data(calendar_url):

    response = requests.get(calendar_url)
    if response.status_code == 200:
        ics_content = response.text
        calendar = Calendar.from_ical(ics_content)

        # Perform desired operations with the calendar data
        # For example, events can be accessed using the 'walk' method
        for component in calendar.walk():
            if component.name == "VEVENT" and "T5" in component.get('summary'):
                # Extract event details
                event_summary = component.get('summary')
                event_start = component.get('dtstart').dt
                event_end = component.get('dtend').dt

                # Process or print event details and a separator
                print(f"Summary: {event_summary}")
                print(f"Start Time: {event_start}")
                print(f"End Time: {event_end}")
                print('-'*30)

    else:
        print(f"Failed to fetch calendar data. Status Code: {response.status_code}")

calendar_url = ' https://my.uopeople.edu/calendar/export_execute.php?userid=284165&authtoken=657373427168eb286398d9d5bf265f135b4f7632&preset_what=all&preset_time=custom'

fetch_calendar_data(calendar_url)
