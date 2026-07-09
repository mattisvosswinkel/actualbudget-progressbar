# Actual Budget Progressbar Formula Generator

# ==========================
# Settings
# ==========================

MAX_VALUE = 1000
# Maximum value / target value that represents 100%

QUERY_NAME = "reserves"
# Actual Budget query name

BAR_LENGTH = 10
# Number of characters used for the progressbar length

STYLE = 0
# Select style number from the styles list below

SHOW_PERCENT = 1
# Show percentage value (1 = enabled, 0 = disabled)

PERCENT_POSITION = 0
# Percentage position (0 = before bar, 1 = after bar)

PERCENT_DECIMALS = 2
# Decimal places of percentage (0 = 73%, 2 = 72.57%, 3 = 72.568%)

# ==========================
# Styles
# ==========================

styles = [
    [
        "⣀", "⣄", "⣤", "⣦", "⣶", "⣷", "⣿"
    ], #0 • dotted

    [
        "░", "▒", "▓", "█"
    ], #1 • shaded

    [
        "░", "█"
    ], #2 • shaded (reduced)

    [
        "▁", "▂", "▃", "▅", "▆", "▇", "▉"
    ], #3 • gradient

    [
        "□", "■"
    ], #4 • blocks

    [
        "▱", "▰"
    ], #5 • battery

    [
        "⎯", "▬"
    ], #6 • lines

    [
        "□", "☒"
    ], #7 • checked

    [
        "○", "●"
    ], #8 • circles

    [
        "∘", "•"
    ], #9 • dots

    [
        "☆", "★"
    ], #10 • stars

    [
        "▷", "▶"
    ] #11 • arrows
]


# ==========================
# Preparation
# ==========================

chars = styles[STYLE]
steps = len(chars)

query = f'QUERY("{QUERY_NAME}")'


# ==========================
# Progress Formula
# ==========================

parts = []

percent_format = (
    "0"
    if PERCENT_DECIMALS == 0
    else "0." + ("0" * PERCENT_DECIMALS)
)


percent = [
    '" "',
    f'TEXT({query}/{MAX_VALUE}*100,"{percent_format}")',
    '"%"'
]


if SHOW_PERCENT and PERCENT_POSITION == 0:
    parts.extend(percent)
    parts.append('" "')


for i in range(BAR_LENGTH):

    start = i / BAR_LENGTH
    end = (i + 1) / BAR_LENGTH

    formula = "IFS("

    for j, char in enumerate(chars):

        threshold = start + (
            (end - start) * ((j + 1) / steps)
        )

        formula += (
            f'{query}/{MAX_VALUE}<{threshold:.10f},"{char}",'
        )

    formula += f'TRUE(),"{chars[-1]}")'

    parts.append(formula)


if SHOW_PERCENT and PERCENT_POSITION == 1:
    parts.append('" "')
    parts.extend(percent)


parts.append('" "')


progress_formula = (
    "=CONCATENATE(" +
    ",".join(parts) +
    ")"
)


# ==========================
# Color Formula
# ==========================

color_formula = f"""=IFS(
  {query}/{MAX_VALUE}<0.25,theme_reportsRed,
  {query}/{MAX_VALUE}<0.50,"#ffbd8a",
  {query}/{MAX_VALUE}<0.75,"#ffe28a",
  TRUE(),theme_reportsGreen
)"""


# ==========================
# Terminal Colors (ANSI)
# ==========================

RESET = "\033[0m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"

# ==========================
# Output
# ==========================

print()

print(
    CYAN +
    "╔═════════════════════════════════════════════╗\n"
    "║ Actual Budget Progressbar Formula Generator ║\n"
    "╚═════════════════════════════════════════════╝"
    + RESET
)

print()

print(BLUE + "Settings" + RESET)
print("────────")
print(f"Query:             {QUERY_NAME}")
print(f"Max Value:         {MAX_VALUE}")
print(f"Length:            {BAR_LENGTH}")
print(f"Style:             {STYLE}")
print(f"Show Percent:      {SHOW_PERCENT}")
print(f"Percent Position:  {PERCENT_POSITION}")
print(f"Decimals:          {PERCENT_DECIMALS}")

print()

print(GREEN + "Progress Formula" + RESET)
print("─────────────────")
print()
print(YELLOW + progress_formula + RESET)

print()

print(GREEN + "Color Formula" + RESET)
print("──────────────")
print()
print(YELLOW + color_formula + RESET)

print()

print(CYAN + "✓ Done" + RESET)
print()
