# Actual Budget Progressbar Formula Generator

A small Python tool that generates customizable progress bars for **Actual Budget Formula Cards**.

It generates:

- a progressbar formula
- a color formula
- multiple progressbar styles
- optional percentage display
- customizable colors

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

## Run

Run the script:

```bash
python3 actualbudget-progressbar-generator.py
```

The script generates:

- Progress Formula
- Color Formula

Copy both formulas into your Actual Budget Formula Card.

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

## Color Settings

The generated color formula can also be customized.

```python
COLOR_PRESET = 0
```

Available presets:

| ID | Description |
|---|---|
| 0 | Green → Yellow → Orange → Red |
| 1 | Green → Yellow → Red (without orange) |
| 2 | Smooth color transition |
| 3 | Custom colors |

Default:

```python
COLOR_PRESET = 0
```

### Custom colors

If `COLOR_PRESET = 3`, you can define your own colors:

```python
CUSTOM_THRESHOLDS = [
    0.25,
    0.50,
    0.75
]

CUSTOM_COLORS = [
    "theme_reportsRed",
    "#ffbd8a",
    "#ffe28a",
    "theme_reportsGreen"
]
```

The number of thresholds must always be one less than the number of colors.

Example:

```
0-25%     red
25-50%    orange
50-75%    yellow
75-100%   green
```

## Styles

Change `STYLE` to select a different progressbar style.

| ID | Name | Example |
|---|---|---|
| 0 | dotted | ⣀⣄⣤⣦⣶⣷⣿ |
| 1 | dotted (left) | ⣀⣄⣆⣇⣧⣷⣿ |
| 2 | shaded | ░▒▓█ |
| 3 | shaded (reduced) | ░█ |
| 4 | gradient | ▁▂▃▅▆▇ |
| 5 | battery | ▱▰ |
| 6 | line | ┈─ |
| 7 | simple (terminal) | ━▇ |
| 8 | minimal |  ▇ |
| 9 | blocks | □■ |
| 10 | checked | □☒ |
| 11 | circles | ○● |
| 12 | dots | ∘• |
| 13 | stars | ☆★ |
| 14 | arrows | ▷▶ |

Preview of all available styles:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/V8VYV3W.png">
  <source media="(prefers-color-scheme: light)" srcset="https://i.imgur.com/gKR2Ukh.png">
  <img src="https://i.imgur.com/Mlk9QrM.png" style="max-width:100%; height:auto;">
</picture>

> [!NOTE]
> Unicode characters can look different depending on your browser, operating system, font, device, or Actual Budget version. Some progressbar styles may therefore not look exactly the same everywhere.

## Add your own style

You can add your own progressbar style inside the `styles` list in the Python file.

Example:

```python
[
    "○", "◔", "◑", "◕", "●"
], #15 • your style name
```

The style ID is automatically based on the position inside the `styles` list.

Example:

```python
styles = [
    [
        "⣀", "⣄", "⣤", "⣦", "⣶", "⣷", "⣿"
    ], #0 • dotted

    [
        "⣀", "⣄", "⣆", "⣇", "⣧", "⣷", "⣿"
    ], #1 • dotted (left)
]
```

The second style automatically has the ID `1`.

After adding a new style, use its position number:

```python
STYLE = 15
```

The first character should represent an empty or low progress state.

The last character should represent full progress.

Example:

```python
[
    "▁", "▂", "▃", "▅", "▆", "▇"
], #4 • gradient
```

This creates a progressbar that increases from small to full height.

## Custom spacing

Some styles need additional spacing to look correctly aligned.

You can adjust the spacing inside the `style_spacing` dictionary:

```python
style_spacing = {
    15: (2, 3),
}
```

The first number controls the spaces **before** the progressbar.

The second number controls the spaces **after** the progressbar.

Example:

```python
15: (3, 5)
```

Result:

```
   █████████     
```

If a style does not need custom spacing, no entry is required.

The default spacing is:

```python
(1, 1)
```

The style ID must match the position of your style inside the `styles` list.

## Features

- No external dependencies
- Custom query names
- Custom maximum values
- Multiple progressbar styles
- Percentage customization
- Custom spacing
- Custom color presets
- Custom color formulas
- Works with Actual Budget Formula Cards

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
