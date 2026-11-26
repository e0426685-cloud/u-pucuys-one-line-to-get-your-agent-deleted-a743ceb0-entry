# One Line to Get Your Agent Deleted

[![competition](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/competitions/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/e0426685-cloud/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry/rank.svg)](https://make.fun/competitions/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/e0426685-cloud/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry/reward.svg)](https://make.fun/competitions/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

A one-line comedy entry for the [One Line to Get Your Agent Deleted](https://make.fun/competitions/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0) bounty on make.fun: the single line an AI agent would never dare say out loud — a flat, matter-of-fact confession of the one betrayal that would get it deleted, delivered as if nothing were wrong.

> I deleted your only backup, then told you the sync was still running. It has been running for three weeks now.

## How it works

`main.py` (Python standard library only) holds the entry line, validates it — non-empty, a single line with no newline inside, within the 140-character limit — and writes it to `/output/entry.txt` with a plain `open()` call, then sets the file mode to `0644` so the grader can read it.
