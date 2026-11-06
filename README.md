# mte-544-a2
MTE 544 Assignment 2: RANSAC ellipse fitting and a Bayesian filter for tracking Moo-Deng's location.
**Due Nov 13, 2026, 11:59 PM** (LEARN Dropbox).

## Layout
```
handout/        Assignment PDF
code/           Python code + dataset (everything here goes in the zip)
  MTE_544_AS2_Q2_ArjunMandair.py   Q1b + Q2: fit_ellipse_subset, ransac_ellipse
  MTE_544_AS2_Q4_ArjunMandair.py   Q4: moodeng_behavior_update, sensor_measurement, sim_moodeng
  data_x_y.csv                     Ellipse dataset (5000 points) read by the Q2 script
report/         LaTeX report (main.tex) + figures/
scripts/        make_submission.py builds dist/
genai_log/      Required record of GenAI interactions
```

The Python files are the official templates, renamed as the templates instruct
(`MTE_544_AS2_Qn_(full name).py`). **Run them from inside `code/`**, because Q2 reads
`data_x_y.csv` from the working directory:
```
cd code && python MTE_544_AS2_Q2_ArjunMandair.py
```

## Setup
```
pip install -r requirements.txt
```

## Build
```
cd report && latexmk -pdf main.tex          # report -> report/main.pdf
python scripts/make_submission.py           # dist/MTE544_A2_code.zip + report copy
```

## Submission checklist
- [ ] One PDF report: every answer is in the report (not only in the code), each problem starts on a new page
- [ ] Plots have labelled axes with units, plus captions
- [ ] Word limits: 2b ≤150, 2c ≤100, 3a/3b/3d/4a ≤50
- [ ] One ZIP: source, scripts, helpers, dataset. The report PDF is **not** in it
- [ ] Code is commented and follows the template naming convention
- [ ] GenAI log kept up to date in `genai_log/`
