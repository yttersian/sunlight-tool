# sunlight

This simple sunlight tool calculates the days since last solstice, the equivalent day (in sunlight hours) from the period leading up to it, and the next solstice or equinox event.

### Dependencies

- Python 3.x
- `ephem`

### Usage

The script includes inline metadata, so if you are using [uv](https://docs.astral.sh/uv/), you can can simply add the following function (or alias) to your shell config:

```zsh
function sunlight {
    uv run --quiet /path/to/sunlight-tool/sunlight.py
}
```

### Example output

```
66 days since solstice (equivalent of 16 October 2023)
Next equinox in 22 days (20 March 2024)
```