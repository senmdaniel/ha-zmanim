from datetime import datetime

def get_zman_times(location="Amsterdam"):
    """
    Simpele demo Zmanim functie.
    Later kun je hier echte berekeningen toevoegen.
    """

    now = datetime.now()

    # PLACEHOLDER times (later vervangen door echte berekening)
    return {
        "location": location,
        "date": now.strftime("%Y-%m-%d"),
        "sunrise": "06:42",
        "sunset": "20:15",
        "shabbat_start": "18:45",
        "shabbat_end": "21:30"
    }
