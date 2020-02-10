# Monadical PyCon.CO 2020 Coding Challenge

## Problem 1 (Easier)

You are trying to organize bringing a large group of Python developers from Bogota to Medellin for PyCon.

There are several different vehicles, each with a different capacity, and renting each one has a cost. Also, the company that is renting the vehicles will only rent them if they are all filled completely. If there are any empty seats, the vehicle cannot be used. Each vehicle can only be used once.

### Task
Write an algorithm that finds the least expensive way to send everyone from Bogota to Medellin, and prints the cost!

### Example

```python
def puzzle(num_people, vehicles):
    # your code here
    # ...
    return final_cost

>>> test_vehicles = (
    {'capacity': 10, 'cost': 250},
    {'capacity': 5,  'cost': 50},
    {'capacity': 15, 'cost': 275},
    {'capacity': 6,  'cost': 20},
)
>>> puzzle(num_people=15, vehicles=test_vehicles)
275
>>> puzzle(num_people=16, vehicles=test_vehicles)
270
```


## Problem 2 (Harder)

A stranger walks up to you in the conference and hands you an envelope. You open it up, but to your confusion there is a message inside that seems to be total nonsense.

Later that day, you get another message, and then another. Each time you receive one you try to ask the messenger what the letter means, but each time they tell you they just saw a python core dev and wander off excitedly.

Finally, you catch one of them before they wander off.

“What is the code for interpreting these letters?” you ask.

“Oh, it’s the same as all of the other ones.” she replies, “Oh wow, is that Guido?” and then she wanders away.

### Task

Crack the code, and write a function to decode any new messages you receive from mystery envelopes.

### Messages

Here are the messages you received:

```
"Ig Bsz swEo IrpHEtCxNN xLC ELDRLU, OSYP ocTiWp Bkauhn."
"Rfcg fhvCC DAzs MrQL OK GLPSQYI eVca eMYYh Rl yheiw MpthltAzm'C nyCv."
"Fftqesjv YoCqM HJrJM xKKRQICWWMSM bX TBlhWee gcia wdasu elu."
"Lbvh fz vrqsF WCuJ fIIPxLH ICFOX HeJi aa iefdl ako Zrukimhoht syFrzAyxwGwz."
"Ig Bsz DiwD FB vuK LNvNQCC JP QFIOQWO XROgdZfZ, pecqe kv f iwxu IEwIJvF vT pyQAI jYNJV fYcfU gURVbhb."
"Wjvk ynl ykypnG FIGCyxP, BRFCWII Ig GPe ARAZfgYt, wnu edr qlmy JAHF trLt DJ ANLVOQW."
"BfcxxnlBt sD osIJvJ NCwK TGMa."
"EyromhoA rC nrHIuI MBvJ GLPMKFMY."
"Sjospj pA lpFGsG KztH yLKOLFZ."
"CpospjD qB mqGHtH LAuI zMLPMKFEYKK."
"Fmcw ny jnDEqE IxrF HzOQCC."
"Sqcuwj pA lpFGsG KztH zBLRE."
"RfcgegosqCI oBICJJ."
```

### Example

```python
def puzzle(encoded_message):
    # your code here
    # ...
    return plaintext


>>> puzzle("RfcgegosqCI oBICJJ.")
...decrypted text here...
```
