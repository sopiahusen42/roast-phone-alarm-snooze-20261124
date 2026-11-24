# roast-phone-alarm-snooze-20261124

[![make.fun · One-Line Roast: The Gadget You Use Every Day](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/sopiahusen42/roast-phone-alarm-snooze-20261124/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/sopiahusen42/roast-phone-alarm-snooze-20261124/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

The gripe is real because it is measurable: the snooze button is the one
target your hand has to hit while you are still unconscious, and it is
suspiciously generous — big enough that a thumb can find it with no eyes
open and no decision made. The last word lands because "co-conspirator"
reframes the feature as a partner in the crime: the button is not failing to
wake you, it is agreeing with you. The line never says the alarm is bad; it
says the design has taken a side, which is a sharper accusation than any
battery or notification complaint.

## The line

> My phone's snooze button is exactly the size of my thumb asleep. That is not a feature, that is a co-conspirator.

## Run it

```
python3 main.py
cat /output/entry.txt
```

The program prints nothing on success and exits 0. Set `MAKEFUN_OUTPUT_DIR`
to write somewhere other than `/output`.

## How it works

`main.py` holds the line in the constant `LINE` and hands it to
`validate_entry()`, which checks that it is a str, not blank after strip, no
longer than 200 Unicode code points, a single line, and equal to its own
stripped form. Any failure prints one line to stderr and exits 1. On success
it creates the output directory, writes the line as UTF-8 with a trailing
newline, reads the bytes back to confirm they match, and exits 0. Nothing is
read from the clock, the network, or a random source, so the output is
byte-identical on every run.
