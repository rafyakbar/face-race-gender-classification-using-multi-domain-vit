"""Time conversion helpers."""


def seconds_to_time(seconds: float) -> dict:
    """
    Convert seconds to a human-readable time breakdown.

    Returns:
        Dict with days, hours, minutes, seconds, and a formatted text string.
    """
    seconds = float(seconds)
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining = round(seconds % 60, 2)

    return {
        "input_seconds": seconds,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": remaining,
        "text": f"{days} hari {hours} jam {minutes} menit {remaining} detik",
    }
