# practicalprobability

This is just a scratchpad of various probability estimates, with occasional code snippets.  Also practice for using GitHub's markdown system.

## Is the new computer system buggy?
A friend complained about a computer change at his work.  They instituted a new front-end interface for their existing database.  The first day after the new interface was implemented, he ran into an error retrieving certain data (one which occasionally came about previously, but only once a year or so).  The tech support folks claimed this was pure coincidence, nothing more.  Intuitively, it seems unlikely that something would *just happen* to break right after a new system was implemented, even if new system wasn't supposed to affect the back-end.  He wanted to know how likely it was that the system really was buggy.

Bayes' theorem states:

```
P(B|E) = P(E|B) * P(B) / P(E)
```
where

```
	P(E|B) : the probability that if the system *is* buggy, this error would be seen
	P(B)   : the baseline probability of a bug (prior to seeing the evidence)
	P(E)   : the probability that this error would be seen, whether or not there is a bug

	P(B|E) : The updated probability the system is buggy, given that we have seen an error
```

The term P(B|E) is what we want to know, and so we need values for the right-hand side of the equation.  The trick to useful real-world probability calculations is getting reasonable estimates for the key terms.

The baseline probability of an error is P(B), which we can get from the tech support folks.  We need to get a well-calibrated estimate, and to get around that we need to overcome the natural human inclination against admitting any possibility of being wrong.  One great way to do that is by making people place [bets](https://en.wikipedia.org/wiki/Prediction_market) upon their beliefs.  If tech support claims that there's only a 1% chance of a bug, then they should be completely neutral about making a bet with 100-to-1 odds (i.e., paying out $100 if the system has a bug vs receiving $1 if it doesn't).  If they balk at that, then they don't *really* believe that it's only a 1% chance of a bug.  If they take 20-to-1 odds, we can figure the chance of a bug is 5%, so P(B) is 0.05, and P(~B) is 0.95 (technically the probability is 1 in 21, but 5% is close enough).

The chance of an error generally (the denominator) is the composite of both of our possible worlds (an error when the system has a bug, and when it doesn't).  The chance of an error without bugs is P(E|~B).  Previous history tells us that this should be very low, only once or twice a year.  We'll set it at 2% to be generous.  

The other possible world is when the system does have a bug: P(E|B)*P(B).  We can't be positive of the value for P(E|B), but since this is the first day with the new system we can imagine it's around 50% (if we had gone several days before seeing this bug, the value would be lower).

```
 	 			P(E|B) * P(B)						0.5 * 0.05
P(B|E) =  	  ------------------			=    -----------------		= 0.56
			P(E|B)*P(B) + P(E|~B)*P(~B)			0.5*0.05 + 0.02*0.95
```

Or a 56% chance that the system has a bug.  This matches nicely with our intuitive suspicion: we can't be absolutely sure that the new system is buggy, but it is *awfully suspicious* that this happened.

If the bug occurs again within the week, then we might revise our estimate of P(E|B) down slightly - only twice within 5 business days means it's 0.4.  But since our new prior for a buggy system is 56%, We end up extremely confident that there's a bug:

```
				0.4 * 0.56				.224	
P(B|E) = 		------------		=   -----	= 0.96
			0.4*0.56 + 0.02*0.44		.238 
```



## Monty Hall : a quick simulation

The famous [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) continues to frustrate people, because the correct solution is so counterintuitive.  Based on an old game show, the problem goes like this:

```
	1) There are three doors.  Behind one is hidden a fabulous prize, behind the other two are booby prizes.
	2) You choose a door.  There is a 1/3 probability that it has a prize.  There is a 2/3 probability the prize is behind one of the other doors.
	3) The host (Monty) opens one of the other two doors, revealing a booby prize.
	4) Monty offers you a chance to switch to the remaining door.  Should you?

```
The intuitive (but incorrect) answer is that switching is irrelevant: it seems that since there are two doors, each has a 50% probability of hiding the prize.  But the correct answer is that you should definitely switch.  

If Monty opened one of the two alternate doors at random, then you might learn something about your own door.  Specifically, one-third of the time Monty would open the door onto the real prize, and you would learn that your door held a booby prize.  The other two-thirds of the time, Monty would reveal a booby prize, and so your chance of winning would be 1/2, whether you switched or not.

But Monty isn't opening doors at random; he's using behind-the-scenes information.  No matter which door has the real prize, Monty is going to show you a booby prize.  So there's still a 1/3 chance that your door is a winner, and a 2/3 chance that one of the alternate doors is a winner.  Since there's only one alternate door left, you should switch to it, and double your chances of winning.

This is such an astonishing result that almost no one believes it the first time (not even the famed mathematician Paul Erdos).  But it checks out; people have analyzed the old game show, and found that switching really was the better option.  But you don't have to take my word for it.  I wrote a quick simulation that allows the user to easily verify the result: keeping the same door wins 1/3 of the time, changing doors wins 2/3 of the time.


## On heavy metals in protein powder

When trying to build muscle, it's important to get plenty of protein (the rule of thumb for weightlifters is daily protein intake should be 1 gram per pound of body mass).  It's certainly best to get protein from whole-food sources, but most people also use some powdered supplements.  Someone asked me about an [article](http://www.consumerreports.org/cro/2012/04/protein-drinks/index.htm) in Consumer Reports which found traces of heavy metals.

My down-and-dirty analysis is this: If I'm going to eat protein, it's important to look at the levels of cadmium, mercury, etc *per unit of protein*. So for comparison, lead and cadmium in meat are generally found at the level of a few ug/kg, based on the abstract I found here:
http://www.ingentaconnect.com/content/tandf/tfac/2006/00000023/00000008/art00002

Seafood is generally [significantly worse](http://www.ncbi.nlm.nih.gov/pubmed/12623648), roughly 100 ug/kg. 

I couldn't find much about chicken eggs from commercial sources, but a [paper](http://www.ncbi.nlm.nih.gov/pubmed/21679937) studying wild birds in a polluted area (New Jersey) found levels ranging from 100s to 1000s of ug/kg. This is almost certainly an upper limit on the amount of heavy metals I might be exposed to via eggs

I figure that meat of any sort is roughly 1/3 water, 1/3 fat, and 1/3 protein. So a kilo of meat has 300g of protein. To get 75g of protein (the ballpark for 3 scoops of protein powder) I'll need to eat around 250g of meat (around 8 oz). That will also mean a few ug of heavy metals if eating meat, up to 10s of ug if eating fish. Protein powder falls in between those two, so I'm not going to worry about it.


