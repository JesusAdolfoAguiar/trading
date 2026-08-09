# Fair Value Gap (FVG) Training Memory

This document stores the specific criteria for identifying valid and invalid Fair Value Gaps (FVGs) based on visual training and chart examples.

## 1. Core Definition
* **Bullish FVG:** A gap between the high wick of Candle 1 and the low wick of Candle 3 in a 3-candle sequence, leaving a portion of Candle 2's body unmitigated by either wick.
* **Bearish FVG:** A gap between the low wick of Candle 1 and the high wick of Candle 3 in a 3-candle sequence, leaving a portion of Candle 2's body unmitigated by either wick.

## 2. Valid FVG Criteria
* **Example 1 (Bearish FVG after Main POI Rejection):** A valid FVG often forms *after* price successfully interacts with and rejects a Main POI (e.g., rejecting the 4369.5 level). The subsequent FVG provides confirmation of the reversal and often targets the next grid levels (e.g., dropping to 4346.5).
* **Example 2 (Mid-POI Rejection & Gap Fill):** When price breaks a Main POI (e.g., drops below 4346.5) creating a Bearish FVG, but fails to reach the next Main POI and instead strictly rejects the *Mid-POI* (e.g., 4329.25), that rejection often provides the momentum to reverse and completely *fill* the recently created FVG back up to the breached Main POI.

## 3. Invalid FVG Criteria
*(To be populated with user examples...)*

## 4. Market Structure & Levels (The Grid)
* **Main POIs (Points of Interest):** Dotted, yellow horizontal lines separated exactly by $11.5. These act as Major Support and Resistance zones.
* **Mid-POIs:** Solid white/gray horizontal lines placed exactly halfway between Main POIs (separated by $5.75).
* **Core Strategy Concept:** Gold tends to interact heavily with this specific mathematical grid structure. FVG validity and trade entries are likely dependent on their interaction with these levels.
* **Probabilistic Interactions (Margin of Error):** The market is probabilistic. While "perfect sweeps" (where a wick perfectly touches a level and immediately reverses) do happen—often at Mid-POIs—they are not guaranteed. Sometimes price will reach a level (especially a Main POI) and "stay there," consolidating, testing the level multiple times with wicks piercing through (margin of error), before finally reversing.
* **Macro Directional Moves (Length of Move):** During high volume sessions where these grid FVGs are created, the resulting directional moves (from POI reversal to next POI target) tend to be substantial. As a rule of thumb, look for macro moves of at least **$20.00 to $23.00 (200+ pips, or roughly 2 full POI zones)**. 
* **The 1-Zone Exception & "Fit on the Screen" Rule:** A smaller, 1-zone move (~$11.50 / 100 pips) is still an A+ setup *if* it is filling a clean, immediate M5 FVG. **Rule:** We trade ONLY the immediate reversal of the most recent FVG. This is a reversal strategy, not a breakout strategy. Target the immediate FVG fill (POI to POI). If a secondary FVG target does not fit on the immediate screen, do NOT hold the trade hoping for a breakout. Take the 100 pips and exit.

## 5. Execution Rules (M1 Timeframe)
* **The "First Touch" Danger:** Buying or selling the *first touch* of a Main POI is highly dangerous. The market often creates a trap (a small 2-4 minute bounce) before continuing through the zone to hunt liquidity (often finding true support at the next Mid-POI).
* **No Blind Limit Orders:** Never place blind limit orders (catching a falling knife) at POIs, even Mid-POIs. A level must prove it is holding. Blind orders expose you to algorithmic stop hunts and liquidity sweeps (e.g., price blowing through a Mid-POI to target the next Main POI).
* **The 5-7 Minute Rule:** When price hits a POI (especially a Main POI), you MUST wait 5-7 minutes (5 to 7 M1 candles) for confirmation. Let the level prove that it can hold the price action and absorb the momentum before considering an entry. 
* **M1 Confirmation:** Combine the 5-7 minute wait with a structural confirmation (e.g., an M1 Market Structure Shift and pullback into an M1 FVG) to ensure the HTF reversal is actually locked in.

## 6. Scripting & Processing Notes
*   We use Python with `Pillow` (PIL) for programmatic chart annotations based on visual/coordinate analysis.
