# Say What Actually Broke

One line of software error copy for the make.fun bounty
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).
`main.py` (Python standard library only) writes the line to `/output/entry.txt`:
the brutally honest truth about a deploy that deleted the production database
while the only backup sat untested since 2021 — funny on a single read, and
shippable in a real error dialog.

[![Bounty](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Kojeck86/say-what-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Kojeck86/say-what-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

## Run it

```sh
python3 -P -s main.py
cat /output/entry.txt
```

The program creates `/output` if needed and writes exactly one line
(157 characters, plain UTF-8, no trailing newline).
