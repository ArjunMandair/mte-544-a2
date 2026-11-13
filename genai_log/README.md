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
| 2026-11-09 | Claude Code | Q2a, Q2b | Claude ran and reviewed my `fit_ellipse_subset` and `ransac_ellipse` twice, using throwaway checks (not in this repo) that included a corrected reference fit. Claude pointed to line 58 as not matching my Q1a row; I fixed that line myself. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2 helpers, Q1a report | At my request, Claude changed non-TODO code: fixed the template's `plot_ellipse` radii to 1/sqrt(eigenvalue) and removed its 9.80665 scaling, set the axis labels to unitless, and saved the figure to `report/figures/`. Claude also reworded the last Q1a sentence to match the code (raises `LinAlgError`). | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2 helpers | At my request, Claude reverted all of its changes to the lab-provided parts of the Q2 file (`plot_ellipse`, imports, main block). Only my TODO sections and the name in the header differ from the template. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2 report | At my request, Claude ran my unmodified Q2 script (with a seed set from a throwaway runner outside this repo) and wrote its results into the 2(a) and 2(b) sections of `report/main.tex`, with TODO notes for the 2(b) explanation, the figure and all of 2(c). | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2b | I wrote the 2(b) explanation. Claude typeset it into `report/main.tex` as written, counted the words, and ran a throwaway copy of my code (not in this repo) with the line 101 filters disabled to test my claim about large ellipses. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2b figure | At my request, Claude wrote the plotting helper `code/MTE_544_AS2_Q2_figure_ArjunMandair.py`, which imports my `ransac_ellipse` and draws the figure. It does not change the Q2 file. Claude added the figure and caption to `report/main.tex` and replaced the two figure/seed TODO notes. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2c | At my request, Claude wrote the helper `code/MTE_544_AS2_Q2_sweep_ArjunMandair.py`, ran the parameter study on my `ransac_ellipse`, and added the table, figure and setup sentences to `report/main.tex`. It does not change the Q2 file. The 100-word comments are left for me to write. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2c | I wrote the 2(c) comments with placeholders for the numbers. Claude filled the placeholders from the results table, typeset the comments into `report/main.tex`, counted the words and checked each claim against the table. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2c | At my request, Claude reworded the first clause of my N comment to match the table (inlier percentage roughly steady, centre stabilises up to N = 500). | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q2c | At my request, Claude rewrote my 2(c) comments to fit 100 words: it kept my points, removed the numbers, added a sentence introducing Table 1 and Figure 3, and changed the N comment to match the table. Claude also removed the setup paragraph earlier at my request. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q3a | I wrote the answer and explanation. Claude checked the arithmetic and transition values against the handout, counted the words, and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q3b | I wrote the matrix and explanation. Claude checked each entry against the handout, counted the words, and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q3c | I wrote the derivation. Claude checked it with a throwaway exact-fraction and eigenvector calculation (not in this repo) and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q3d | I wrote the matrix and explanation. Claude checked each entry against the handout, counted the words, and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q3e | I wrote the filter derivation and example. Claude checked the formulas and example with a throwaway calculation (not in this repo) and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q4 | Claude ran my Q4 script and checked it with throwaway scripts (not in this repo): sampling frequencies against A and C, a separate filter recursion, and accuracy over many runs. At my request, Claude wrote the 4(b) sentence and the 4(c) text and results table from a run (seed 0 set from outside the script) in `report/main.tex`, with a TODO for my 4(a) explanation. | Session 50aefb99 |
| 2026-11-09 | Claude Code | Q4a | I wrote the 4(a) explanation. Claude counted the words, tested the long-run frequency claim with a throwaway run (not in this repo), and typeset it into `report/main.tex` as written. | Session 50aefb99 |
| 2026-11-13 | Claude Code | Q1, Q2 code | Claude explained my Q1 script and my `ransac_ellipse`. At my request, Claude removed my bounding-box filter from `ransac_ellipse` to test it. Every seed then returned a huge ellipse with 100% inliers, so I reverted the change myself. | Session 995aad48 |
| 2026-11-13 | Claude Code | Report formatting | At my request, Claude removed the due date, the point values and word limits from the headings, and the subheading descriptions. Claude changed labels from 1(a) to 1a, removed colons from explanatory sentences, rewrote the two 1a bullets as full sentences, and removed "(next case)" and "(maximum consensus)". | Session 995aad48 |
| 2026-11-13 | Claude Code | Q2 figures | At my request, Claude deleted the helper `MTE_544_AS2_Q2_figure_ArjunMandair.py` and its figure, removed the extremes figure from the 2c sweep helper (keeping the table), and updated the 2b caption and 2c text. I save the 2b figure myself from the unmodified template's main block. | Session 995aad48 |
| 2026-11-13 | Claude Code | Q2c | At my request, Claude deleted the sweep helper `MTE_544_AS2_Q2_sweep_ArjunMandair.py` and its results table, and removed the table and its intro sentence from 2c. I base 2c on my own runs of the template's main block. | Session 995aad48 |
| 2026-11-13 | Claude Code | Q2c | I made and saved seven plots from the template's main block. At my request, Claude renamed them (`q2c_N_*`, `q2c_iterations_*`, `q2c_threshold_*`), added them to 2c as three figures with captions, trimmed their white borders in LaTeX, and pointed the opening sentence of 2c at them. | Session 995aad48 |

**Transcript:** "Session 50aefb99" is Claude Code session `50aefb99-4011-4854-99e8-9e4363846115`, stored locally at
`C:\Users\arjun\.claude\projects\c--Codes-mte-544-a2\50aefb99-4011-4854-99e8-9e4363846115.jsonl`.
"Session 995aad48" is Claude Code session `995aad48-fdea-417b-a6c7-bbda13c34e24`, stored locally at
`C:\Users\arjun\.claude\projects\c--Codes-mte-544-a2\995aad48-fdea-417b-a6c7-bbda13c34e24.jsonl`.

**Policy status:** use of GenAI on the analytical parts (Q1a) has not been confirmed with the instructor or TA.
