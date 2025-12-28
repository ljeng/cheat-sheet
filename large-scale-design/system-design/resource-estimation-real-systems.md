# Resource Estimation with Real Systems

The engineering technique of back-of-the-envelope calculations is a standard tool for practicing engineers. Yet it's neglected in computing. "How much water flows out of the Mississippi River in a day?" Bob Martin once asked this during a conversation on software engineering. The river is about a mile wide and twenty feet deep[^01] near its mouth. To answer, one estimates this. The flow rate is five miles an hour[^02]. The calculation is simple:

$$1 \text{ mile} \times \frac{1}{250} \text{ mile} \times 120 \frac{\text{miles}}{\text{day}} \
\approx 0.48 \frac{\text{miles}^3}{\text{day}}$$

This estimate is accurate to within an order of magnitude. Martin used this same logic to debunk a proposal for an Olympic communications system. He proved that the proposed design would only work if there were 120 seconds in every minute by measuring the time it took to send a single character of mail. The design was sent back to the drawing board, and the final system worked without a hitch.

- Will 2M nodes[^03] fit in 128MB of RAM? `sizeof(struct node)` is 8 bytes, yet dynamic **allocation** via malloc adds overhead. 8-byte records actually consumed 48 bytes each due to allocator overhead in one system, totaling 96MB for 2M records - nearly exhausting the available **memory**.
- If a numerical **algorithm** is dominated by $n^3$ square root operations and $n = 1000$, how long will it take? A billion square roots, at ~200 nanoseconds each, would take ~200 seconds.

Innumeracy obtrudes perspective on large numbers. For example, a million **seconds** pass in 11.5 days; a billion seconds take nearly 32 years. All the human **blood** in the world[^04] would fit into a cube 870 feet on each side or cover New York’s Central Park to a depth of just under 20 feet. A Concorde jet[^05] is 400k$\times$ faster than a snail[^06]. However, a supercomputer is over a billion times faster than a human at adding ten-digit numbers.

| **mean**[^07] | Calculated by adding all values and dividing by the number of entries. It's easily skewed by extreme outliers. |
| **median**  | The middle value; half the group is above it, half below. |
| **mode**    | The most frequently occurring value. |

A neighborhood's **mean** income is $250K. The area seems prosperous. It's a legitimate average. But the mean is misleading because the millionaires boost the total enormously.

A company reports an average wage of $96K[^08]. This includes the owner’s massive salary. A business can make its payroll look generous to the public. It pleads poverty during tax assessments by switching between these figures.

If the first group of users shows no improvement, a toothpaste company simply suppresses the data. It runs the test again until they get the headline they want.

"$4\times$ more fatalities occur at 7pm than at 7am" doesn't mean 7pm is more dangerous. It simply means there are more people on the road at that time.

1 in 100 people has a disease. A clinic can save time by pooling blood samples from 50 people. The expected number of tests for a group of 50 is ~21. It saves significantly over testing everyone individually.

In the carnival game Chuck-a-Luck, you bet on a number[^09]. Three dice are rolled. The house wins. The probability of your number *not* appearing[^10] outweighs the payouts for single, double, and triple matches.

How do you choose the best spouse or candidate when you meet them sequentially? And you can't go back? Probability theory suggests you should reject the first $\frac{1}{e} \approx 37\%$ of your total expected pool to establish a baseline. Then choose the very next person who's better than everyone you've seen so far.

"The average number of things in a system is the product of the average rate at which they leave and the average time they spend there." If you have 150 cases and drink 25 per year, you hold each case for 6 years. If a club holds 60 people and the average stay is 3 hours, people enter at a rate of 20 per hour. If there are 20 people in line, you'll wait one hour.

John Roebling designed the Brooklyn Bridge to be six times as strong as required because he recognized the limits of his knowledge regarding aerodynamic lift. In software and engineering, we should derate our systems in software - estimating cost with a safety factor to compensate for our ignorance.

| **Type I error** | rejecting a true hypothesis[^11] |
| **Type II error** | accepting a false hypothesis[^12] |

Liberals worry about Type I errors[^13], while conservatives worry about Type II errors[^14] in society. The concern shifts in justice: liberals fear Type II errors[^15], while conservatives fear Type I errors[^16].

The prisoner's dilemma shows that two individuals acting in their own self-interest may end up with a worse outcome than if they had cooperated. Whether in an arms race, a marriage, or a business transaction, the temptation to double-cross for a higher individual payoff portends mutual destruction. Cooperation is only sustained when parties expect to interact repeatedly, providing a tit-for-tat incentive for loyalty.

[^01]: `1/250` of a mile
[^02]: 120 miles a day
[^03]: an integer and a pointer
[^04]: 5B gallons
[^05]: 2K mph
[^06]: 0.005 mph
[^07]: arithmetic average
[^08]: the mean
[^09]: 1-6
[^10]: `125/216`
[^11]: a false negative in a search for truth
[^12]: a false positive
[^13]: the deserving not receiving help
[^14]: the undeserving receiving help
[^15]: punishing the innocent
[^16]: letting the guilty go free
