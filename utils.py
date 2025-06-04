from datetime import datetime
import pytz

# Change class timezones based on user-specified timezone
def convert_timezone(dt: datetime, to_tz: str) -> datetime:
    try:
        target_tz = pytz.timezone(to_tz)
        return dt.astimezone(target_tz)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Unknown timezone: {to_tz}")
