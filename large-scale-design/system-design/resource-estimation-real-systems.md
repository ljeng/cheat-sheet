# Resource Estimation with Real Systems

The engineering technique of "back-of-the-envelope" calculations is standard fare for practicing engineers. Unfortunately, it's neglected in computing. It was in the middle of a conversaton on software engineering that Bob Martin asked, "How much water flows out of the Mississippi River in a day?" Near its mouth, the river is about a mile wide and 20 feet deep[^01]. The flow rate is 5 mph[^02].

$$1 \text{ mile} \times \frac{1}{250} \text{ mile} \times 120 \frac{\text{miles}}{\text{day}} \
\approx 0.48 \frac{\text{miles}^3}{\text{day}}$$

The river discharges about half a cubic mile of water per day to within an order of magnitude. Martin used this same logic to debunk a proposal for an Olympic communications system. Martin's calculations showed that the proposed system could work only if there were >=120 seconds in each minute. The design was sent back to the drawing board, and the final system worked without a hitch.

- Will 2M nodes[^03] fit in 128MB of RAM? `sizeof(struct node)` is 8 bytes, yet dynamic **allocation** via malloc adds overhead. 8-byte records actually consumed 48 bytes each due to allocator overhead in one system, totaling 96MB for 2M records - nearly exhausting the available **memory**.
- If a numerical **algorithm** is dominated by $n^3$ square root operations and $n = 1000$, how long will it take? A billion square roots, at ~200 nanoseconds each, would take ~200 seconds.

Innumeracy obtrudes perspective on large numbers. For example, a million **seconds** pass in 11.5 days; a billion seconds take nearly 32 years. All the human **blood** in the world[^04] would fit into a cube 870 feet on each side or cover New York’s Central Park to a depth of just under 20 feet. A Concorde jet[^05] is 400K$\times$ faster than a snail[^06]. However, a supercomputer is over a billion times faster than a human at adding ten-digit numbers.

The word "average" is commonly used loosely to influence public opinion. When you're told that something is an average, you still don't know very much about it unless you can find out which of the common kinds of average it is - mean, median, or mode.

| **mean**[^07] | Calculated by adding all values and dividing by the number of entries. It's easily skewed by extreme outliers. |
| **median**  | The middle value; half the group is above it, half below. |
| **mode**    | The most frequently occurring value. |

Let's say you're looking to buy property not far from the Watchung Mountain in which I live. Most of my neighbors are small farmers. But three of the inhabitants are millionaire weekenders. I tell you that the average income in this neighborhood is \$65K a year, and that handsome figure sticks in your mind. As a member of some taxpayers' committee, I'm circulating a petition to keep the tax rate down or assessments down. My plea is that we can't afford the increase: the average income is only \$25k. Both these figures are legitimate averages. At the same time, one of them is misleading as the millionaire weekenders boost the total income enormously. If you draw a curve to represent a normal distribution, the **mean**, **median**, and mode fall at the same point. One kind of average is as good as another for describing the heights of men. But for describing their pocketbooks it's not. Instead of being symmetrical, this would be skewed. The mean would be quite a distance from the median.

You read an announcement by a corporation executive or business proprietor that the average pay of people who work in his establishment is some figure. You may be getting nothing more revealing than the average of the proprietor's \$370K income and the salaries of a crew of underpaid workers. The **mode** is \$16K.

Results that aren't indicative of anything can be produced by pure chance - given a small enough number of cases.

Let any small group of persons keep count of cavities for six months, then switch to Doakes'. By chance, a test group shows a big improvement worthy of a headline and perhaps a whole advertising campaign. If the group counts more cavities or about the same number, Doakes & Company files the figures well out of sight and tries again.

If you can't prove what you want to prove, demonstrate something else and pretend they're the same. Your nostrum killed 31,108 **germs** in a test tube. An antiseptic that works well in a test tube may not perform in the human throat. "$4\times$ more fatalities occur at 7 p.m. than at 7 a.m." But the conclusion doesn't follow. More people are killed in the evening because more people are on the highways. Electric power is **available** to $\frac{3}{4}$ of farms. This means that power lines go within ten miles of the farms. This doesn't mean that all those farmers actually have power.

The **expected value** is the average of its values weighted according to their probabilities.

Assume one person in 100 suffers from a disease. The clinic director pools 50 samples and tests them all together. If the pooled sample is negative, she could pronounce the whole group healthy. If not, she could then test each person individually. The expected number of tests necessary is ~21.

The spiel that goes with chuck-a-luck can be very persuasive. You pick a number from 1 to 6 and the operator rolls three dice. You have three chances to win. The expected value of your winnings is

$$\frac{1}{2} - \frac{{(6 - 1)}^3}{6^3} = \frac{1}{2} - \frac{125}{216} \approx -\text{\$}0.079$$

Thus, 125 out of 216 you play chuck-a-luck, you'll lose $1.

Assume Myrtle meets men sequentially, and once she's rejected someone, he's gone forever. Myrtle should reject approximately the first $\frac{1}{e} = 37\text%$ of the $N$ candidates she's likely to meet, and then accept the first suitor after that who's a heartthrob.

"The average number of things in a system is the product of the average rate at which they leave and the average time they spend there." If you have 150 cases and drink 25 per year, you hold each case for 6 years. If a club holds 60 people and the average stay is 3 hours, people enter at a rate of 20 per hour. If there are 20 people in line, you'll wait one hour.

John Roebling designed the Brooklyn Bridge to be six times as strong as required because he recognized the limits of his knowledge regarding aerodynamic lift. In software and engineering, we should derate our systems in software - estimating cost with a safety factor to compensate for our ignorance.

| **Type I error** | rejecting a true hypothesis[^08] |
| **Type II error** | accepting a false hypothesis[^09] |

Liberals worry about Type I errors[^10], while conservatives worry about Type II errors[^11] in society. The concern shifts in justice: liberals fear Type II errors[^12], while conservatives fear Type I errors[^13].

The prisoner's dilemma shows that two individuals acting in their own self-interest may end up with a worse outcome than if they had cooperated. Whether in an arms race, a marriage, or a business transaction, the temptation to double-cross for a higher individual payoff portends mutual destruction. Cooperation is only sustained when parties expect to interact repeatedly, providing a tit-for-tat incentive for loyalty.

[^01]: `1/250` of a mile
[^02]: 120 miles a day
[^03]: an integer and a pointer
[^04]: 5B gallons
[^05]: 2K mph
[^06]: 0.005 mph
[^07]: mean
[^08]: a false negative in a search for truth
[^09]: a false positive
[^10]: the deserving not receiving help
[^11]: the undeserving receiving help
[^12]: punishing the innocent
[^13]: letting the guilty go free
