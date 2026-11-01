# General Probability

## Basic Concepts of Probability

Compute the probability that a hand of 13 cards contains

1. the ace and king of at least one suit

    Let $A_i$ be the event that the hand contains both the ace and king of suit $i$. By inclusion-exclusion,

    $$P(A_1 \cup A_2 \cup A_3 \cup A_4)
        = \frac{\binom{4}{1} \binom{50}{11}
            - \binom{4}{2} \binom{48}{9}
            + \binom{4}{3} \binom{46}{7}
            - \binom{4}{4} \binom{44}{5}}{\binom{52}{13}} \\
        = \frac{139565328072}{635013559600}
        \approx 0.2198$$

1. all 4 of at least 1 of the 13 denominations

    Let $B_j$ be the event that the hand contains all 4 cards of denomination $j$ (at most 3 such events fit in 13 cards). By inclusion-exclusion,

    $$P(B_1 \cup \dots \cup B_{13})
        = \frac{\binom{13}{1} \binom{48}{9}
            - \binom{13}{2} \binom{44}{5}
            + \binom{13}{3} \binom{40}{1}}{\binom{52}{13}} \\
        = \frac{21717689136}{635013559600}
        \approx 0.0342$$

---

A person tried by a 3-judge panel is declared guilty if at least 2 judges cast votes of guilty. Suppose that when the defendant is in fact guilty, each judge will independently vote guilty with probability 0.7, whereas when the defendant is in fact innocent, this probability drops to 0.2. If 70 percent of defendants are guilty, compute the conditional probability that judge number 3 votes guilty given that

1. judges 1 and 2 vote guilty

    Let $G$ denote the event that the defendant is guilty, $P(G) = 0.7$; given $G$ each judge votes guilty independently with probability $0.7$, and given $G^c$ with probability $0.2$.

    $$P(E_3 \mid E_1 E_2)
        = \frac{P(E_1 E_2 E_3)}{P(E_1 E_2)}
        = \frac{0.7 (0.7)^3 + 0.3 (0.2)^3}{0.7 (0.7)^2 + 0.3 (0.2)^2} \\
        = \frac{0.2425}{0.355}
        = \frac{97}{142}
        \approx 0.6831$$

1. judges 1 and 2 cast 1 guilty and 1 not guilty vote

    $$P(E_3 \mid \text{split})
        = \frac{0.7 \times 2 (0.7) (0.3) (0.7) + 0.3 \times 2 (0.2) (0.8) (0.2)}{0.7 \times 2 (0.7) (0.3) + 0.3 \times 2 (0.2) (0.8)} \\
        = \frac{0.225}{0.39}
        = \frac{15}{26}
        \approx 0.5769$$

1. judges 1 and 2 both cast not guilty votes

    $$P(E_3 \mid E_1^c E_2^c)
        = \frac{0.7 (0.3)^2 (0.7) + 0.3 (0.8)^2 (0.2)}{0.7 (0.3)^2 + 0.3 (0.8)^2} \\
        = \frac{0.0825}{0.255}
        = \frac{11}{34}
        \approx 0.3235$$

Let $E_i$, $i = 1, 2, 3$ denote the event that judge $i$ casts a guilty vote. Are these events independent? Are they conditionally independent? Explain.

Not independent: $P(E_i) = 0.7 (0.7) + 0.3 (0.2) = 0.55$ but $P(E_i E_j) = 0.7 (0.7)^2 + 0.3 (0.2)^2 = 0.355 \neq 0.55^2 = 0.3025$ — a guilty vote is evidence that the defendant is guilty, which raises the probability that another judge votes guilty. They are conditionally independent given $G$ or $G^c$: once the defendant's guilt status is fixed, the judges vote independently by assumption.

---

A health study tracked a group of persons for five years. At the beginning of the study, 20% were classified as heavy smokers, 30% as light smokers, and 50% as nonsmokers. Results of the study showed that light smokers were twice as likely as nonsmokers to die during the five-year study but only half as likely as heavy smokers. A randomly selected participant from the study died over the five-year period. Calculate the probability that the participant was a heavy smoker.

| Smoker | $\Pi$ |
| ----- | ----- |
| Heavy | $0.40$ |
| Light | $0.30$ |
| Non   | $0.25$ |

$$\frac{0.40}{0.40 + 0.30 + 0.25} \approx 0.421$$

---

A study of automobile accidents produced the following data: An automobile from one of the model years 1997, 1998, and 1999 was involved in an accident.

| Model | Proportion of All Vehicles | Probability of Involvement in an Accident |
| ---- | --------------- | ---------------------------- |
| 1997 | 0.16            | 0.05                         |
| 1998 | 0.18            | 0.02                         |
| 1999 | 0.20            | 0.03                         |
| Other | 0.46            | 0.04                         |

Determine the probability that the model year of this automobile is 1997.


| Model | $\Pi$ |
| ---- | ----- |
| 1997 | 0.0080 |
| 1998 | 0.0036 |
| 1999 | 0.0060 |
| Other | 0.0184 |

$$\frac{0.0080}{0.0080 + 0.0036 + 0.0060 + 0.0184} \approx 0.222$$

---

Suppose that two defective refrigerators have been included in a shipment of six refrigerators. The buyer begins to test the six refrigerators one at a time. Let the random variable $Y$ represent the number of the test in which the last defective refrigerator is identified. Compute the probabilities for each value of $Y$.

The positions of the two defectives are equally likely to be any of the $\binom{6}{2} = 15$ pairs of test numbers, and $Y = y$ requires one defective at test $y$ with the other among the first $y - 1$ tests:

$$P(Y = y) = \frac{y - 1}{\binom{6}{2}} = \frac{y - 1}{15}, \qquad y = 2, 3, 4, 5, 6$$

| $y$ | $2$ | $3$ | $4$ | $5$ | $6$ |
| --- | --- | --- | --- | --- | --- |
| $P(Y = y)$ | $\frac{1}{15}$ | $\frac{2}{15}$ | $\frac{3}{15}$ | $\frac{4}{15}$ | $\frac{5}{15}$ |

---

A hospital receives two fifths of its flu vaccine from Company A and the remainder from Company B. Each shipment contains a large number of vials of vaccine. From Company A, 3% of the vials are ineffective; from Company B, 2% are ineffective. A hospital tests $n = 25$ randomly selected vials from one shipment and finds that 2 are ineffective. What is the conditional probability that this shipment came from Company A?

Let $D$ be the event that 2 of the $n = 25$ tested vials are ineffective. With priors $P(A) = \frac{2}{5}$, $P(B) = \frac{3}{5}$ and binomial likelihoods (the $\binom{25}{2}$ cancels),

$$P(A \mid D)
    = \frac{P(A) \binom{25}{2} (0.03)^2 (0.97)^{23}}{P(A) \binom{25}{2} (0.03)^2 (0.97)^{23}
        + P(B) \binom{25}{2} (0.02)^2 (0.98)^{23}} \\
    = \frac{0.4 (0.03)^2 (0.97)^{23}}{0.4 (0.03)^2 (0.97)^{23} + 0.6 (0.02)^2 (0.98)^{23}}
    = \frac{0.0001787}{0.0001787 + 0.0001508}
    \approx 0.5423$$

---

An insurance company determines that $N$, the number of claims received in a week, is a random variable with:

$$P[N = n] = \frac{1}{2^{n + 1}}$$

where $n \geq 0$.

The company also determines that the number of claims received in a given week is independent of the number of claims received in any other week.

Calculate the probability that exactly seven claims will be received during a given two-week period.

$$\frac{1}{2^{0 + 1}} \times \frac{1}{2^{7 + 1}} \\
        + \frac{1}{2^{1 + 1}} \times \frac{1}{2^{6 + 1}} \\
        + \frac{1}{2^{2 + 1}} \times \frac{1}{2^{5 + 1}} \\
        + \frac{1}{2^{3 + 1}} \times \frac{1}{2^{4 + 1}} \\
        + \frac{1}{2^{4 + 1}} \times \frac{1}{2^{3 + 1}} \\
        + \frac{1}{2^{5 + 1}} \times \frac{1}{2^{2 + 1}} \\
        + \frac{1}{2^{6 + 1}} \times \frac{1}{2^{1 + 1}} \\
        + \frac{1}{2^{7 + 1}} \times \frac{1}{2^{0 + 1}} \\
    = \frac{1}{64}$$

---

You win at craps by throwing a 7 or 11 on the first toss or by throwing a 4, 5, 6, 8, 9, or 10 on the first toss (the number tossed is referred to as a "point") and subsequently throwing your point before you throw a seven. Find the probability of winning at craps.

Let $P(s)$ be the probability of rolling sum $s$. Once a point $p$ is thrown, only rolls of $p$ or $7$ matter, so the point is made with probability $\frac{P(p)}{P(p) + P(7)}$. By symmetry of the point pairs $\{4, 10\}$, $\{5, 9\}$, $\{6, 8\}$,

$$P(\operatorname{win})
    = P(7) + P(11) + \sum_{p \in \{4, 5, 6, 8, 9, 10\}} \frac{P(p)^2}{P(p) + P(7)} \\
    = \frac{6}{36} + \frac{2}{36}
        + 2 \left[\frac{3}{36} \times \frac{3}{9}
            + \frac{4}{36} \times \frac{4}{10}
            + \frac{5}{36} \times \frac{5}{11}\right] \\
    = \frac{2}{9} + \frac{134}{495}
    = \frac{244}{495}
    \approx 0.4929$$

## Discrete Mathematics

We have 20 thousand dollars that must be invested among 4 possible opportunities. Each investment must be integral in units of 1 thousand dollars, and there are minimal investments that need to be made if one is to invest in these opportunities. The minimal investments are 2, 2, 3, and 4 thousand dollars. How many different investment strategies are available if

1. an investment must be made in each opportunity?

    The minimums use $2 + 2 + 3 + 4 = 11$ thousand, leaving $9$ to distribute freely among the 4 opportunities:

    $$x_1 + x_2 + x_3 + x_4 = 9, \quad x_i \geq 0
        \implies \binom{9 + 3}{3} = \binom{12}{3} = 220$$

1. investments must be made in at least 3 of the 4 opportunities?

    Investing in exactly 3 (dropping the opportunity with minimum $4$, $3$, $2$, or $2$) leaves $13$, $12$, $11$, or $11$ thousand above the remaining minimums, each distributed among 3 opportunities in $\binom{r + 2}{2}$ ways; add the all-4 count:

    $$220 + \binom{15}{2} + \binom{14}{2} + \binom{13}{2} + \binom{13}{2}
        = 220 + 105 + 91 + 78 + 78
        = 572$$

---

An auto insurance company has 10,000 policyholders. Each policyholder is classified as

1. young or old
1. male or female
1. married or single

Of these policyholders, 3000 are young, 4600 are male, and 7000 are married. The policyholders can also be classified as 1320 young males, 3010 married males, and 1400 young married persons. Finally, 600 of the policyholders are young married males. How many of the company's policyholders are young, female, and single?

Young: $3000$
Male: $4600$
Married: $7000$
Young male: $1320$
Married male: $3010$
Yong married: $1400$
Young married male: $600$

$$(3000 - 1320) - (1400 - 600) = 880$$

---

Thirty items are arranged in a 6-by-5 array as shown.

| $A_1$  | $A_2$   | $A_3$    | $A_4$    | $A_5$    |
| $A_6$  | $A_7$   | $A_8$    | $A_9$    | $A_{10}$  |
| $A_{11}$ | $A_{12}$ | $A_{13}$ | $A_{14}$ | $A_{15}$ |
| $A_{16}$ | $A_{17}$ | $A_{18}$ | $A_{19}$ | $A_{20}$ |
| $A_{21}$ | $A_{22}$ | $A_{23}$ | $A_{24}$ | $A_{25}$ |
| $A_{26}$ | $A_{27}$ | $A_{28}$ | $A_{29}$ | $A_{30}$ |

Calculate the number of ways to form a set of three distinct items such that no two of the selected items are in the same row or same column.

Choose 3 of the 6 rows, choose 3 of the 5 columns, then match the chosen rows to the chosen columns:

$$\binom{6}{3} \binom{5}{3} \times 3! = 20 \times 10 \times 6 = 1200$$

---

How many of the first 1000 positive integers are multiples of neither 6 nor 9?

$$1000 - \lfloor 1000 / 6 \rfloor
        - \lfloor 1000 / 9 \rfloor
        + \lfloor 1000 / \operatorname{lcm}(6, 9) \rfloor
    = 778$$
