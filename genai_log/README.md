# GenAI Usage Log

Per the course policy, GenAI may be used only to **aid** (not generate) programming,
and a record of every interaction (prompts and responses) must be kept. The instructing
team may request these records.

Add one entry per interaction session below (or save full transcripts as separate
files in this folder and link them here).

| Date | Tool | Question / file | Purpose | Transcript |
|------|------|-----------------|---------|------------|
| 2026-11-06 | Claude Code | Repo setup | Created folder structure, report skeleton, placeholder stubs and zip script (no question content). Later moved the official templates and dataset into `code/`, renamed them and filled in the student name; TODO sections untouched. Stubs deleted. | Session 50aefb99 |
| 2026-11-06 | Claude Code | Policy | Asked whether Claude may say if I am right or wrong. Claude said yes for programming, and that the analytical parts are unclear under the policy. | Session 50aefb99 |
| 2026-11-06 | Claude Code | Q1a | Asked if 5 points are needed for the ellipse. Claude confirmed 5 and gave the reason (five unknowns, one linear equation per point, points in general position). | Session 50aefb99 |
| 2026-11-06 | Claude Code | Q1b | Asked Claude to create a Python script for Q1. Claude declined because it would be generated solution code. No script was produced. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Policy | Asked what AI may be used for. Claude gave its reading of the policy and advised confirming the unclear cases with the instructor or TA. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1a | I wrote successive drafts of the rationale and method; Claude reviewed each one, pointing out errors and gaps. Feedback included: independence applies to the rows of M, not the points; more than 5 points is overdetermined, not unsolvable; the fixed constant fails for conics through the origin; N singular and dᵀN⁻¹d = 1 need guards; Q should be checked after scaling by α. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1a | Claude wrote and ran short throwaway Python checks (not in this repo, made-up points only, not the assignment data) on the rank of M and on dᵀN⁻¹d for degenerate point sets. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1a | Correction: Claude first said the positive definite check rejects 3 collinear points, and I wrote that down. Claude then found that for intersecting lines dᵀN⁻¹d = 1, so the sample is rejected at step 3. Claude flagged this and I rewrote the bullet. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1a report | Claude typeset my write-up into `report/main.tex` in LaTeX, without the triangle example, and later inserted my rewritten 3-collinear bullet as I wrote it. | Session 50aefb99 |
| 2026-11-09 | Claude Code | GenAI log | Claude added these entries. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1b | Claude ran my script `MTE_544_AS2_Q1_ArjunMandair.py` and checked its output with a separate throwaway SVD computation (not in this repo), which matched. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1b | Claude made non-solution edits to my script at my request: print precision, run command in the header, axis units (assumed metres), and saving the plot to `report/figures/`. Fitting logic unchanged. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1b report | At my request, Claude wrote the Q1b section of `report/main.tex` from my script's output (values, verification, figure and caption) and added two TODO notes. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q1b report | At my request, Claude removed the TODO notes and changed the units assumption from metres to unitless in the script's axis labels, the report text and the caption. | Session 50aefb99 |

**Transcript:** "Session 50aefb99" is Claude Code session `50aefb99-4011-4854-99e8-9e4363846115`, stored locally at
`C:\Users\arjun\.claude\projects\c--Codes-mte-544-a2\50aefb99-4011-4854-99e8-9e4363846115.jsonl`.

**Policy status:** use of GenAI on the analytical parts (Q1a) has not been confirmed with the instructor or TA.
