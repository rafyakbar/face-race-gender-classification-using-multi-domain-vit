"""Display helpers for Jupyter and terminal."""

import re

import pandas as pd


def _is_notebook() -> bool:
    """Detect if running in Jupyter notebook environment."""
    try:
        from IPython import get_ipython
        shell = get_ipython()
        if shell is None:
            return False
        return shell.__class__.__name__ == "ZMQInteractiveShell"
    except ImportError:
        return False


IS_NOTEBOOK = _is_notebook()

# Lazy import IPython only when needed
_display = None
_HTML = None
if IS_NOTEBOOK:
    from IPython.display import display as _display, HTML as _HTML


def printhtml(html: str) -> None:
    """Display raw HTML in Jupyter, or print as text in terminal."""
    if IS_NOTEBOOK and _display and _HTML:
        _display(_HTML(html))
    else:
        clean = re.sub(r"<[^>]+>", "", html).strip()
        if clean:
            print(clean)


def html_br() -> None:
    """Display a line break in Jupyter, or print empty line in terminal."""
    if IS_NOTEBOOK and _display and _HTML:
        _display(_HTML("<br>"))
    else:
        print()


def h(level: int, text: str) -> None:
    """Display an HTML heading (h1-h6) in Jupyter, or print with prefix in terminal."""
    if not 1 <= level <= 6:
        raise ValueError("Heading level must be between 1 and 6.")
    if IS_NOTEBOOK and _display and _HTML:
        _display(_HTML(f"<h{level}>{text}</h{level}>"))
    else:
        prefix = "#" * level
        print(f"\n{prefix} {text}")


def index_ranges(data: list, n_items: list[int]) -> list[tuple[int, int]]:
    """
    Compute index ranges for paginated display.

    Args:
        data: Full data list.
        n_items: Number of items per segment [first, *middle, last].

    Returns:
        List of (start, end) tuples.
    """
    n = len(data)
    k = len(n_items)
    if k < 2:
        raise ValueError("Need at least 2 n_items values.")

    middle = n_items[1 : k - 1]
    divisor = len(middle) + 1
    distance = (n - sum(n_items)) // divisor

    ranges = [(0, n_items[0])]
    current = n_items[0]
    for ni in middle:
        current += distance
        ranges.append((current, current + ni))
        current += ni
    ranges.append((n - n_items[k - 1], n))
    return ranges


def display_table(
    data: list[dict],
    table_style: str = "width: 100%",
    column_widths: list[str] | None = None,
    text_aligns: list[str] | None = None,
    hidden_columns: list[str] | None = None,
    n_items: list[int] | None = None,
    save_excel: str | None = None,
    with_header: bool = True,
) -> list[dict]:
    """
    Display a list of dicts as an HTML table in Jupyter, or text in terminal.

    Args:
        data: List of dictionaries to display.
        table_style: CSS style string for the table.
        column_widths: Per-column width percentages.
        text_aligns: Per-column text alignment.
        hidden_columns: Columns to exclude from display.
        n_items: Pagination params [first, *middle, last] for large datasets.
        save_excel: If set, export to this Excel file path.
        with_header: Whether to show header row.

    Returns:
        The (possibly paginated) data that was displayed.
    """
    if not data:
        print("Data kosong.")
        return []

    headers = [k for k in data[0].keys() if k not in (hidden_columns or [])]

    if n_items and len(n_items) >= 2:
        new_data = []
        for start, end in index_ranges(data, n_items):
            new_data += data[start:end]
            new_data.append({h_key: "..." for h_key in headers})
        new_data = new_data[: len(new_data) - 1]
    else:
        new_data = data.copy()

    if save_excel:
        pd.DataFrame(new_data).to_excel(save_excel, index=False)

    if not text_aligns:
        text_aligns = ["left"] * len(headers)

    # Build HTML
    html = f'<table style="{table_style}; border-collapse: collapse;">\n'

    if with_header:
        html += "  <tr>\n"
        for i, header in enumerate(headers):
            w = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            a = f"text-align: {text_aligns[i]};"
            html += f'    <th style="border: 1px solid black; padding: 8px; {w} {a}">{header}</th>\n'
        html += "  </tr>\n"

    for row in new_data:
        html += "  <tr>\n"
        for i, key in enumerate(headers):
            w = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            a = f"text-align: {text_aligns[i]};"
            html += f'    <td style="border: 1px solid black; padding: 8px; {w} {a}">{row[key]}</td>\n'
        html += "  </tr>\n"

    html += "</table>"
    printhtml(html)
    return new_data
