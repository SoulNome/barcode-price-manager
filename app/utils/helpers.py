from datetime import datetime


def format_price(value: float | None) -> str:
    if value is None:
        return 'N/A'
    return f'${value:,.2f}'


def format_datetime(dt: datetime | None) -> str:
    if dt is None:
        return 'N/A'
    return dt.strftime('%Y-%m-%d %H:%M')
