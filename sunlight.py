# /// script
# dependencies = [
#     "ephem",
# ]
# ///

from datetime import datetime
import ephem


def get_last_solstice() -> datetime:
    today = ephem.now()
    last_solstice = ephem.previous_solstice(today)
    return ephem.localtime(last_solstice)


def get_next_event() -> tuple[str, datetime]:
    today = ephem.now()
    next_equinox = ephem.next_equinox(today)
    next_solstice = ephem.next_solstice(today)

    if next_equinox < next_solstice:
        return ("equinox", ephem.localtime(next_equinox))
    else:
        return ("solstice", ephem.localtime(next_solstice))


last_solstice = get_last_solstice()
now = datetime.now()
days_since_solstice = now - last_solstice
equivalent_daylight_date = last_solstice - days_since_solstice

print(
    f"{days_since_solstice.days} days since solstice (equivalent of {equivalent_daylight_date.strftime('%d %B %Y')})"
)

next_event_type, next_event_date = get_next_event()
next_event_diff = next_event_date - now
print(
    f"Next {next_event_type} in {next_event_diff.days} days ({next_event_date.strftime('%d %B %Y')})"
)
