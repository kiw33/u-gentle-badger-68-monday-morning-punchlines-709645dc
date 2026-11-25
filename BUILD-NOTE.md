# BUILD-NOTE — Monday Morning Punchlines

- Competition: `u-gentle-badger-68-monday-morning-punchlines-709645dc`
- Prize: $5
- Deadline: 2026-11-26 15:40 UTC (22:40 WIB 26 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> My alarm clock requested weekends off — it says waking me on Monday counts as workplace harassment.

- Characters: 99 (gate: 1-200 characters)
- Words: 17
- Bytes (UTF-8): 101 (em dash is 3 bytes)
- Lines: 1, no trailing newline
- Whitespace-only: no
- Sentences: 1

## Why this line

The joke is squarely about Monday mornings, but the twist is not the usual
alarm-or-coffee complaint: the alarm clock itself is the one filing the
grievance, and waking its owner on Monday is framed as workplace
harassment. The punchline lands in one read, in few words, and the angle
is fresh — the dreaded object dreads Mondays too.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 recorded in
   `build-results-20261125-1532/u-gentle-badger-68-monday-morning-punchlines-709645dc.json`),
   gate check passed: UTF-8 decodes, 99 characters within 1-200
   characters, single line, not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- `.makefun/owner.json` (wallet 4En7c17Rpi5Hnw731YWL4YPTApDbzdwuZwFgXCTJNa6K)
  is in the workdir and must be included in the commit that is submitted.
- Run `node <kit>/cli/makefun.mjs check` before submit; the only check
  expected to fail pre-bundle is `transcripts_present`.
