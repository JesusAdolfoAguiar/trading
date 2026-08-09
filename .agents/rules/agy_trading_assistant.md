# Antigravity Trading Assistant Protocol

When operating in this trading repository to update the strategy, build the local Auditor Agent, or review charts, strictly adhere to the following:

1. **Ground Truth Documents:** 
   - Always reference `journals/memory-test.md` for core technical strategy (M5 SR displacement, grid interactions, valid/invalid FVGs).
   - Always reference `journals/tilt_rules_engine.md` for strict mechanical kill switches (Max 2 attempts, 45-minute limits, 7-9 candle durations).
   
2. **Strategy Constraints:**
   - **Time Exhaustion:** A valid directional move (whether macro or 1-zone) lasts exactly 35-45 minutes (7-9 M5 candles). Trades past this window are structurally invalid.
   - **Post-Reversal Chop:** "Chop" specifically refers to the sideways, overlapping price action that occurs *after* the initial valid reversal has exhausted.
   
3. **Workflow Conventions:**
   - When required to highlight invalid conditions or annotate charts, write and execute Python scripts using `Pillow (PIL)` to programmatically draw bounding boxes or markers.
   - After finalizing a major phase or rule definition (e.g., updating memory files, generating prompts), automatically offer to `git commit` and `git push` the changes to maintain version control.
