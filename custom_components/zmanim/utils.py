from datetime import date
from astral import LocationInfo
from astral.sun import sun
from zoneinfo import ZoneInfo

def calculate_zmanim(lat: float, lon: float, method: str = "gra", target_date: date | None = None):
    """Bereken Zmanim tijden."""
    if target_date is None:
        target_date = date.today()

    tz = ZoneInfo("Europe/Brussels")
    location = LocationInfo(
        name="Antwerp",
        region="",
        timezone="Europe/Brussels",
        latitude=lat,
        longitude=lon,
    )

    s = sun(location.observer, date=target_date, tzinfo=tz)

    return {
        "date": str(target_date),
        "status": "ok",
        "zmanim": {
            "shkia": {"time": str(s["sunset"].time()), "ts": int(s["sunset"].timestamp())},
            "chatzos": {"time": str(s["noon"].time()), "ts": int(s["noon"].timestamp())},
        },
    }
