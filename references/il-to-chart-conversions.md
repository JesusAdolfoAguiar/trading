# Injection Logic (IL) Chart Conversions & Explanations

**Objective:** Translate psychological Injection Logics into objective, chart-based Edge Rules based on the `memory-test.md` and `tilt_rules_engine.md` strategy definitions. Identify which ILs govern the *chart* vs. which ILs govern the *operator*.

---

## PART 1: The Chart-Convertible ILs (Mechanical Execution)

### IL 1: "Zones are references, not walls. Trade the reaction."
**The Objective Chart Definition (What is a "reaction"?):**
* **Time Constraint:** A valid reaction is defined by the **5-7 Minute Rule**. When price hits a Main POI or Mid-POI, you must wait for **5 to 7 M1 candles**.
* **The Confirmation:** The M1 candle bodies must fail to close beyond the level (though wicks may pierce it). A true reaction is confirmed when this consolidation results in an **M1 Market Structure Shift (MSS)** and a pullback into an M1 FVG.

### IL 2: "Follow the structure, not the ego."
**The Objective Chart Definition (What is "structure"?):**
* **The Grid:** Target the immediate M5 FVG fill from POI to POI (~100 pips). Ego wants a 200+ pip breakout not on the screen.
* **Time Structure:** A valid move lasts exactly **35 to 45 minutes (7-9 M5 candles)**. Holding past the 9th M5 candle is trading ego, not structure.

### IL 3: "Trade what you see, not what you think."
**The Objective Chart Definition (What does "I see" mean?):**
* **What you see:** A sequence of candles from POI to POI closing in the exact same direction (a clean M5 FVG). 
* **What NOT to see (Chop):** Overlapping M5 candles with wicks on *both* sides in the middle of a range. 
* **Exhaustion:** Occurs *only* at POIs, looking like 5-7 M1 candles testing a level but failing to break it.

### IL 4: "Am I forcing my bias? / Trade against the trend"
**The Objective Chart Definition (Defining Trend & Cycle):**
* **Trend Exhaustion:** A trend only lasts **7-9 M5 candles**. If you attempt to buy a "continuation" on the 10th candle, you are forcing your bias into a dead cycle.
* **Tilt Lockout:** If you take a loss and flip your bias (e.g., short to long) on the *same 45-minute swing*, the `tilt_rules_engine` dictates this as forcing bias and triggers a lockout.

### IL 5: "No volume, no setup. Too much volume, no setup. Respect the cycle."
**The Objective Chart Definition (Defining Volume visually):**
* **"No Volume":** Price is stuck inside a single Mid-POI to Main-POI zone, printing overlapping M5 wicks (a sideways channel) without reaching target levels. 
* **"Too Much Volume":** News candles (CPI/NFP/8:30AM spikes). Massive M5 candles that cover >100 pips ($11.5) on a single print, blowing through POIs without establishing a clean FVG sequence. 

### IL 6: "Don't front-run the reversal. Let the LTF prove it." / "Wait for the shift, not the shape."
**The Objective Chart Definition (What is "Proof"?):**
* **Front-running:** Limit ordering the POI, or entering while the M1 is still strictly making Lower Lows (LL) and Lower Highs (LH) against your idea.
* **The "Proof":** The exact moment the M1 creates a Market Structure Shift (MSS) by breaking the last LH, and then pulls back to an M1 FVG. That M1 FVG is the physical chart location of "proof".

### IL 7: "Has structure actually changed, or am I just scared of losing profit?" / "Fear is not an exit signal."
**The Objective Chart Definition (Changed vs. Scared):**
* **"Structure Changed":** An M5 candle CLOSES beyond your invalidation level (breaking the structural sequence of the FVG).
* **"Scared":** Price is merely pulling back into the M5 FVG (a healthy retracement) and leaving wicks, but the M5 candle *body* has not closed against the structural narrative. 

### IL 8: "Let the LTF close the trade."
**The Objective Chart Definition:**
* Instead of exiting manually because a 1-minute candle flashed red, your exit is triggered *only* when an M1 Market Structure Shift occurs against your position as price reaches the opposing POI.

### IL 9: "New data, new direction. Discipline is adapting."
**The Objective Chart Definition:**
* **Structural Invalidation (from tilt rules):** When price ranges at a POI for 7-9 M5 candles, and then expands, breaking the previous swing high/low by 5-10 pips. The chart has structurally invalidated the previous idea, requiring a hard reset of your bias.

---

## PART 2: The Non-Convertible (Operator) ILs

The following ILs **cannot** be converted to chart patterns. Why? Because they do not govern the *Strategy* (the Chart)—they govern the *Hardware running the Strategy* (You). 

A perfect M5 FVG can print perfectly on the grid, but if the operator is compromised, the trade will fail. These ILs act as biological and psychological diagnostics.

**1. "No bandwidth, no trade."**
* **Why it's unchartable:** "Bandwidth" is physiological (sleep, stress, emotional baggage). A perfect A+ setup can exist on the chart, but if your biological bandwidth is zero, your execution and management will be flawed. The chart cannot measure your fatigue.

**2. "Do you wanna be right, or be profitable?"**
* **Why it's unchartable:** This is an ego-check. When a Stop Loss is hit or a structural invalidation occurs, the chart has already done its job (it proved you wrong). This IL exists strictly to stop your hand from revenge-clicking the mouse to try and "punish" the chart into proving you right.

**3. "If you can walk away with profits, you can do so with losses."**
* **Why it's unchartable:** This targets the psychological asymmetry of *loss aversion*. It addresses the emotional inability to accept a red day, which exists entirely inside the human brain, outside of candlestick data.

**4. "Would I take this in a backtest? If no, skip."**
* **Why it's unchartable:** This is a reality-check mechanism. It asks you to compare your *current emotional perception* (warped by live PnL and adrenaline) against your *cold, objective perception* during weekend backtesting. 

**5. "Tilt detected? Hands off the mouse."**
* **Why it's unchartable:** Tilt is a physiological adrenaline/cortisol response. The chart is entirely unaware that your heart rate just spiked.

**6. "One is too much, one thousand are not enough. Edge is gone, screen is off."**
* **Why it's unchartable:** This is a mantra for trading addiction. Once you enter the tilt spiral, no amount of winning trades will satisfy the anger, and one single loss will re-trigger the cascade. It dictates walking away from the computer entirely. No chart pattern can tell you to shut down your PC.
