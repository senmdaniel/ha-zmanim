from datetime import date
from astral import LocationInfo
from astral.sun import sun
from zoneinfo import ZoneInfo

def calculate_zmanim(lat: float, lon: float, method: str = "gra", target_date: date | None = None):
    if target_date is None:
        target_date = date.today()

    tz = ZoneInfo("Europe/Paris")

    location = LocationInfo(
        name="home",
        region="",
        timezone="Europe/Paris",
        latitude=lat,
        longitude=lon,
    )

    s = sun(location.observer, date=target_date, tzinfo=tz)

    return {
        "alot_hashachar": s.get("dawn"),
        "netz": s.get("sunrise"),
        "chatzot": s.get("noon"),
        "shkia": s.get("sunset"),
        "tzeit": s.get("dusk"),
    }
