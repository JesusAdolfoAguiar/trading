## 26/08/2026
Prevention is the word of today. It's way easier prevent to be involved in situations, aka
market conditions that get me on tilt, that trying to stop the emotions as they start to escalate.
## Scenario 1: intraday chop:
When price enters a directionless status ('range' of < 50 pips), just wicks up an down on m1/m5, for longer than 20 minutes.
Action: close positions, and call it a day. If you still have bandwidth (time) to trade, wait until the next displacement happens. 
If price 


Stop Loss: stop before the loss
## Prompt for the agent:
Based on this week's notes, and on my edge, I need that you identify those situations that could put me on a tilt state.

Tilt happens when price doesn't move anywhere. Why?
If price stops me out and keeps dumping with strength, if I'm calmed, I know I'll wait for the exhaustion, and buy the dip.
Same for when price uptrends too much.

Task 2: I need a validator. I need an auditor system. Why? 
1) I need to better train my agent. I've seen that, as the agent is created to infer tags when info not available (which can happen)
2) I need that the agent tells me what does he look when looking at a picture. Can it recognize a clean m5 fvg?
3) I've seen the agent applying incorrect tags. The idea is reduce my manual work, but as this moment, the agent is not trained
good enough. 
As my edge is clean m5 reversals, the only two possible context scenarios are:
Context: 
1) range, easy, poi to poi, 100 pip range. 
2) trend: bull run or selloff, depending on the strenght of the move.

So, my bias (mind) needs to be opposite of the context, as I'm tradig reversals.

IF the current market condition is range, it's poi to poi
If market condition is selloff, bias is bullish > it happened today. Price sold off on Pre Ny (context), then it went back up (bias > bullish)

## About my edge and conditions
That's another thing about my edge that I've itendified. To win in trading, I need to trade in the direction of the move. One of my current strategy flaws, as I menetioned
is that price makes a strong push, up or down, ok, and then after that move is exhausted, I trade what in my mind is a clean m5 fvg reversal.
Example: Price makes a 400 pip dump (over 2-3 hours). Of that dump, the last 200-300 pips were of a clean m5 fvg. Cool. Then, the immediate first reverse move is a clean m5 fvg
as well. So, I identify that second clean m5 fvg as a 'poi to poi' chance, when in reality is the begining of the trend change, the reversal of the strong move of before. 
So, that's another thing that i need to recognize, when it's price on a intraday extension, when it's poi to poi, and when it's poi to previous session highlows.


## About the retraining
Again, I'm trying to reduce manual work, but as of right now, each tag category should have its why. But this would be anty DRY right? 
The Why that the agent currently proposes could be the base, but I do need to guide the agent further. The agent is being great in generating the tags,
and incorporating them into tradezella as well, to the T, but If I import bad data, I'll get also bad data as result.

## Task: attach Injection Logics with the actual chart patterns I will see on screen

## Tradezella agent
Now, in the technical part (about my edge and conditions), I'd like to leverage the tradezella agent. I believe he can give me good insights as he has my records, executions, screenshots, etc.I'll need a prompt for him as well.
This could be leverage or source of truth in terms of the technical narrative. The local agent is more of a data processor/agregator.

## For the local agent
Another would be going through all the notes, processed and raw, and get patterns he can see. 


This is my brainstorm. I need that you help me organize my ideas, and create a plan to move forward. 

