from time import time
from datetime import datetime, timezone

utc_timestamp = time()

scientific_notation = f"{utc_timestamp:.2e}"

utc_datetime = datetime.fromtimestamp(utc_timestamp, tz=timezone.utc)

formatted_datetime = utc_datetime.strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {utc_timestamp:,.4f} \
    or {scientific_notation} in scientific notation"
)
print(formatted_datetime)
