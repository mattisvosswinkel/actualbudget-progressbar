# Actual Budget Progressbar Formula Generator

A small Python tool that generates customizable progress bars for **Actual Budget Formula Cards**.

It generates:

- a progressbar formula
- a color formula
- multiple progressbar styles
- optional percentage display

## Requirements

- Python 3
- No external packages required

## Important

This tool uses Actual Budget's experimental formula features.

Before using the generated formulas, enable:

`Settings → Show advanced settings → Experimental features → Formula cards`

Documentation:

https://actualbudget.org/docs/experimental/formulas/

## Download

Download the latest version of the generator:

[`actualbudget-progressbar-generator.py`](https://raw.githubusercontent.com/mattisvosswinkel/actualbudget-progressbar/main/actualbudget-progressbar-generator.py)

Or clone the repository:

```bash
git clone https://github.com/mattisvosswinkel/actualbudget-progressbar.git
```

## Configuration

Open the script with your preferred text editor, for example:

```bash
nano actualbudget-progressbar-generator.py
```

Adjust the settings at the top of the file:

```python
MAX_VALUE = 1500
# Maximum value / target value that represents 100%

QUERY_NAME = "reserva"
# Actual Budget query name

BAR_LENGTH = 20
# Number of characters used for the progressbar length

STYLE = 0
# Select style number from the styles list below

SHOW_PERCENT = 1
# Show percentage value (1 = enabled, 0 = disabled)

PERCENT_POSITION = 0
# Percentage position (0 = before bar, 1 = after bar)

PERCENT_DECIMALS = 0
# Decimal places of percentage
# 0 = 73%
# 2 = 72.53%
# 3 = 72.534%
```

## Styles

Change `STYLE` to select a different progressbar style.

| ID | Name | Example |
|---|---|---|
| 0 | dotted | ⣀ ⣄ ⣤ ⣦ ⣶ ⣷ ⣿ |
| 1 | shaded | ░ ▒ ▓ █ |
| 2 | shaded (reduced) | ░ █ |
| 3 | gradient | ▁ ▂ ▃ ▅ ▆ ▇ ▉ |
| 4 | blocks | □ ■ |
| 5 | battery | ▱ ▰ |
| 6 | lines | ⎯ ▬ |
| 7 | checked | □ ☒ |
| 8 | circles | ○ ● |
| 9 | dots | ∘ • |
| 10 | stars | ☆ ★ |
| 11 | arrows | ▷ ▶ |

Preview of all available styles:

<img src="https://i.imgur.com/stPXsys.png" style="max-width:100%; height:auto;">

## Add your own style

You can add your own progressbar style inside the `styles` list in the Python file.

Actual Budget may display some characters differently depending on the font, device, or browser. If a character looks wrong, try another Unicode character or a different style.

Add a new list with your characters:

```python
[
    "○", "◔", "◑", "◕", "●"
], #12 • your style name
```

The style ID is automatically based on the position of the style inside the `styles` list.

Example:

```python
styles = [
    [
        "⣀", "⣄", "⣤", "⣦", "⣶", "⣷", "⣿"
    ], #0 • dotted

    [
        "░", "▒", "▓", "█"
    ], #1 • shaded
]
```

The second style in the list automatically has the ID `1`.

After adding a new style, use the position number as the `STYLE` value:

```python
STYLE = 12
```

The first character should represent an empty or low progress state.

The last character should represent full progress.

Example:

```python
[
    "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"
], #12 • height gradient
```

This creates a progressbar that increases from small to full height.

## Run

Run the script:

```bash
python3 actualbudget-progressbar-generator.py
```

The script generates:

- Progress Formula
- Color Formula

Copy both formulas into your Actual Budget Formula Card.

## Features

- No external dependencies
- Custom query names
- Custom maximum values
- Multiple progressbar styles
- Percentage customization
- Color formula generation
- Works with Actual Budget Formula Cards

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
