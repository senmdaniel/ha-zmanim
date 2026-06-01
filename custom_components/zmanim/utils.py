from datetime import datetime, date
from astral import LocationInfo
from astral.sun import sun

def calculate_zmanim(lat: float, lon: float, method: str = "gra", target_date: date | None = None):
    if target_date is None:
        target_date = date.today()

    location = LocationInfo(
        name="Home",
        region="",
        timezone="Europe/Paris",
        latitude=lat,
        longitude=lon,
    )

    s = sun(location.observer, date=target_date, tzinfo=location.timezone)

    # basis zmanim (simpel maar uitbreidbaar)
    return {
        "alot_hashachar": s["dawn"],
        "netz": s["sunrise"],
        "chatzot": s["noon"],
        "shkia": s["sunset"],
        "tzeit": s["dusk"],
    }
