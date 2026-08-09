# Tilt Rule Engine Spec

**Objective:** Prevent post-reversal chop trading and late-cycle FVG entries on XAUUSD reversal swings.

## 1. Swing Definition
* A swing starts at the first reversal attempt off a POI.
* All re-entries on the same directional idea belong to the same swing until a reset condition is met.

## 2. Hard Disqualifiers (Kill Switches)
* **Max Attempts:** Max reversal attempts per POI is **2**. The 3rd attempt is automatically disqualified.
* **Time Limit:** NO new entries after **45 minutes** from the first reversal attempt on that swing.
* **M5 Candle Limit:** NO new entries after **9 M5 candles** from the first attempt.
* **Bias Flip Lockout:** If you switch from long to short or short to long on the same swing, STOP trading that swing.
* **Loss Cluster Lockout:** After 3 losses inside a 20-minute window, mandatory reset.

## 3. Reset Conditions (Creates a Fresh Cycle)
* **Structural Invalidation:** Prior swing high/low is breached by 5–10 pips or 0.1×ATR.
* **Time Reset:** 30 minutes have passed and the market has clearly moved on.
* **Displacement Reset:** A new expansion leg travels at least 100 pips or at least 75% of the prior macro leg.
* **POI Migration:** The active POI cluster has shifted 50 pips or more away from the original area.

## 4. Do Not Trade (Visual Checklist)
* **[ ]** Price has already made one clean reversal, then begins overlapping M5 candles with wicks on both sides.
* **[ ]** There are repeated failed entries in the same 15–30 minute window.
* **[ ]** The next FVG appears only *after* the first push has already lost momentum.
* **[ ]** You are considering a secondary or tertiary FVG instead of the first clean post-POI imbalance.
* **[ ]** You feel the urge to force a setup because the level has not yet worked.

## 5. Execution Rule
* Take ONLY the first or second valid attempt inside the active swing.
* After the second failure, stand down until a fresh cycle is confirmed by one of the Reset Conditions.
* If the chart looks like chop, assume the edge is gone until proven otherwise.

## 6. Scriptable Logic (For Local Auditor Agent)
```python
if attempt_count > 2 or minutes_since_first_attempt > 45 or m5_candles_since_first_attempt > 9:
    return "NO TRADE"

if bias_flipped_on_same_swing:
    return "NO TRADE"

if losses_last_20_minutes >= 3:
    return "RESET REQUIRED"

# Otherwise, only allow a new entry if price is still within the same clean reversal context and has not transitioned into overlapping chop.
```
