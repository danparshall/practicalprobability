# practicalprobability


## Is the new computer system buggy?
A friend complained that his work instituted a new front-end interface for their existing database.  The first day after the new interface was implemented, he ran into an error retrieving certain data (one which occasionally came about previously, but only once a year or so).  The tech support folks claimed this was pure coincidence, nothing more.  Intuitively, it seems unlikely that something would *just happen* to break right after a new system was implemented, even if new system wasn't supposed to affect the back-end.

My analysis: given that we have observed this error (E), we want to know the probability that the new system has a bug (B), P(B|E).  Bayes' theorem states:

P(B|E) = P(E|B) * P(B) / P(E)

That is, the probability of the system having a bug, given this error, is the chance of seeing an error if we *did* have a bug, times the chance that a bug exists, divided by the probability of seeing this error generally.

The chance of an error generally (the denominator) is the composite of two possible worlds.  The first is when the system does have a bug: P(E|B)*P(B).  We can't be positive of the value for P(E|B), but since this is the first day with the new system we can imagine it's around 50%.  The second possible world is when the system doesn't have a bug: P(E|~B) * P(~B).  Previous history tells us that P(E|~B) should be very low, only once or twice a year.  We'll set it at 2%

The prior probability of an error is P(B), we can get that from the tech support folks.  We need to get a well-calibrated estimate, which we can do by seeing how they feel about betting that their system doesn't have a bug.  If they claim that there's only a 1% chance of a bug, then they should be completely neutral about making a bet with 100-to-1 odds (i.e., paying out $100 if the system has a bug vs receiving $1 if it doesn't).  If they balk at that, then they don't *really* believe that it's only a 1% chance of a bug.  If they take 20-to-1 odds, we can figure the chance of a bug is 5%, so P(B) is 0.05, and P(~B) is 0.95
```
 	 			P(E|B) * P(B)						0.5 * 0.05
P(B|E) =  	  ------------------			=    -----------------
			P(E|B)*P(B) + P(E|~B)*P(~B)			0.5*0.05 + 0.02*0.95
```

P(B|E) = 0.56

Or a 56% chance that the system has a bug.  This matches nicely with our intuitive suspicion: we can't be absolutely sure that the new system is buggy, but it is *awfully suspicious* that this happened.

If the bug occurs again within the week, then we might revise our estimate of P(E|B) down slightly - only twice within 5 business days means it's 0.4.  But since our new prior for a buggy system is 56%, We end up extremely confident that there's a bug:
```
				0.4 * 0.56				.224	
P(B|E) = 		------------		=   -----	= 0.96
			0.4*0.56 + 0.02*0.44		.238 
```


## Monty Haul : a Bayesian perspective



## On heavy metals in protein powder

When trying to build muscle, it's important to get plenty of protein (the rule of thumb for weightlifters is daily protein intake should be 1 gram per pound of body mass).  It's certainly best to get protein from whole-food sources, but most people also use some powdered supplements.  Someone asked me about an article in Consumer Reports which found traces of heavy metals: 
http://www.consumerreports.org/cro/2012/04/protein-drinks/index.htm

My down-and-dirty analysis is this: If I'm going to eat protein, it's important to look at the levels of cadmium, mercury, etc *per unit of protein*. So for comparison, lead and cadmium in meat are generally found at the level of a few ug/kg, based on the abstract I found here:
http://www.ingentaconnect.com/content/tandf/tfac/2006/00000023/00000008/art00002

Seafood is generally significantly worse, roughly 100 ug/kg : 
http://www.ncbi.nlm.nih.gov/pubmed/12623648

I couldn't find much about chicken eggs from commercial sources, but a paper studying wild birds in a polluted area (New Jersey) found levels ranging from 100s to 1000s of ug/kg. This is almost certainly an upper limit on the amount of heavy metals I might be exposed to via eggs:
http://www.ncbi.nlm.nih.gov/pubmed/21679937

I figure that meat of any sort is roughly 1/3 water, 1/3 fat, and 1/3 protein. So a kilo of meat has 300g of protein. To get 75g of protein (the ballpark for 3 scoops of protein powder) I'll need to eat around 250g of meat (around 8 oz). That will also mean a few ug of heavy metals if eating meat, up to 10s of ug if eating fish. Protein powder falls in between those two, so I'm not going to worry about it.


