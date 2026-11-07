# Univariate Random Variables

## Discrete Univariate Distributions

Let

$$m(t) = \frac{1}{6} e^t + \frac{2}{6} e^{2t} + \frac{3}{6} e^{3t}$$

Find the following:

1. $\operatorname E(Y)$

    $$\operatorname E(Y)
        = m'(0)
        = \frac{1}{6} + \frac{2 \cdot 2}{6} + \frac{3 \cdot 3}{6}
        = \frac{7}{3}$$

1. $\operatorname V(Y)$

    $$\operatorname E(Y^2)
        = m''(0)
        = \frac{1}{6} + \frac{2^2 \cdot 2}{6} + \frac{3^2 \cdot 3}{6}
        = 6$$
    $$\operatorname V(Y)
        = 6 - {\left(\frac{7}{3}\right)}^2
        = \frac{5}{9}$$

1. The distribution of $Y$

    The coefficient of $e^{ty}$ in $m(t) = \operatorname E(e^{tY})$ is $P(Y = y)$, so $Y$ is discrete with $P(Y = 1) = \frac{1}{6}$, $P(Y = 2) = \frac{2}{6}$, $P(Y = 3) = \frac{3}{6}$.

---

Consider the following discrete distributions:

- Discrete uniform random variable with $n = 10$
- Binomial random variable with $n = 10$ and $p = 0.6$
- Hypergeometric random variable with $n = 5$, $B = 10$, and $G = 30$
- Poisson random variable with $\lambda = 4$
- Geometric random variable with $p = 0.25$
- A negative binomial variable with $r =3$ and $p = 0.5$

For each of these distributions, calculate the probability that

1. The random variable is within one standard deviation of the mean
1. The random variable is within two standard deviations of the mean
1. The random variable is within three standard deviations of the mean

*Note*: For the normal distribution, these probabilities are 68.26%, 95.44%,and 99.74% respectively.

Each entry is $P(\mu - k\sigma \leq X \leq \mu + k\sigma)$; the discrete uniform is on $\{1, \dots, 10\}$; the hypergeometric counts the $B$-type items in the sample of $n = 5$ from $N = B + G = 40$; the geometric counts trials up to and including the first success (support $\{1, 2, \dots\}$); the negative binomial counts trials up to and including the $r$th success (support $\{3, 4, \dots\}$).

| Distribution | $\mu$ | $\sigma$ | $k = 1$ | $k = 2$ | $k = 3$ |
| --- | --- | --- | --- | --- | --- |
| Discrete uniform ($n = 10$) | 5.5 | 2.8723 | 0.6000 | 1.0000 | 1.0000 |
| Binomial ($n = 10$, $p = 0.6$) | 6 | 1.5492 | 0.6665 | 0.9817 | 0.9983 |
| Hypergeometric ($n = 5$, $B = 10$, $G = 30$) | 1.25 | 0.9172 | 0.6941 | 0.9900 | 0.9996 |
| Poisson ($\lambda = 4$) | 4 | 2 | 0.7977 | 0.9786 | 0.9972 |
| Geometric ($p = 0.25$) | 4 | 3.4641 | 0.8665 | 0.9437 | 0.9822 |
| Negative binomial ($r = 3$, $p = 0.5$) | 6 | 2.4495 | 0.7305 | 0.9453 | 0.9888 |

The roughly symmetric, unimodal distributions come closest to the normal percentages; the skewed geometric deviates the most.

### Binomial

If $X ~ \operatorname{binomial}(n, p)$ and $p$ is $P ~ \operatorname{beta}(\alpha, \beta)$, what is the pmf of $X$?

$$P(X = k)
    = \int_0^1 \binom{n}{k} p^k {(1 - p)}^{n - k}
        \cdot \frac{p^{\alpha - 1} {(1 - p)}^{\beta - 1}}{B(\alpha, \beta)} \, dp \\
    = \frac{\binom{n}{k}}{B(\alpha, \beta)}
        \int_0^1 p^{k + \alpha - 1} {(1 - p)}^{n - k + \beta - 1} \, dp \\
    = \binom{n}{k} \frac{B(k + \alpha, n - k + \beta)}{B(\alpha, \beta)}
    = \binom{n}{k} \frac{\Gamma(\alpha + \beta) \, \Gamma(k + \alpha) \, \Gamma(n - k + \beta)}{\Gamma(\alpha) \, \Gamma(\beta) \, \Gamma(n + \alpha + \beta)}$$

for $k = 0, 1, \dots, n$ — the beta-binomial distribution.

### Geometric

In modeling the number of claims filed by an individual under an automobile policy during a three-year period, an actuary makes the simplifying assumption that for all integers $n \geq 0$

$$p_{n + 1} = \frac{1}{5} p_n$$

where $p_n$ represents the probability that the policyholder files $n$ claims during the period. Under this assumption, what is the probability that a policyholder files more than one claim during the period?

$$p_0 \Sigma_{i = 0}^\infty \frac{1}{5^i} = 1$$
$$p_0 \frac{1}{1 - \frac{1}{5}} = 1$$
$$p_0 \cdot \frac{5}{4} = 1$$
$$p_0 = \frac{4}{5}$$
$$1 - (p_0 + p_1) \\
    = 1 - \left(p_0 + \frac{1}{5} p_0\right) \\
    = 1 - p_0 \frac{6}{5} \\
    = 1 - \frac{4}{5} \cdot \frac{6}{5} \\
    = \frac{1}{25}$$

### Hypergeometric

A catch-and-release program estimates the population size of an animal in a region. During the catch phase, 20 animals are tagged. Several months later, 30 animals are captured, and 7 of them have tags. What is the most likely population size?

Assumptions:

- Enough time passes between the two catches so that the animals disperse throughout the region
- No tags fall off between the two catches
- No new animal enters the population by birth between the catches; no animal exits the population by death between the catches
- No animals migrate into or out of the region
- Both catches involve sampling without replacement
- Capturing is done so that each uncaptured animal is equally likely to be captured

Let $N$ be the population size; the number of tagged animals among the 30 captured is hypergeometric.

$$L(N) = \frac{\binom{20}{7} \binom{N - 20}{23}}{\binom{N}{30}}$$
$$\frac{L(N)}{L(N - 1)}
    = \frac{(N - 20)(N - 30)}{N (N - 43)}
    \geq 1
    \iff 7N \leq 600$$

$L(N)$ increases while $N \leq \frac{600}{7} \approx 85.7$ and decreases afterward, so

$$\hat N = \left\lfloor \frac{20 \cdot 30}{7} \right\rfloor = 85$$

### Negative Binomial

If

$$M_x(t) = {\left(\frac{0.70}{1 - 0.3e^t}\right)}^5$$

what is the distribution of $X$?

$$\operatorname{NB}(5, 0.70)$$

### Poisson

There are three highways in the county. The number of daily accidents that occur on these highways are Poisson random variables with respective parameters 0.3, 0.5, and 0.7. Find the expected number of accidents that will happen on any of these highways today.

$$0.3 + 0.5 + 0.7 = 1.5$$

---

Assume that a policyholder is four times more likely to file exactly two claims as to file exactly three claims. Assume also that the number $X$ of claims of this policyholder is Poisson. Determine the expectation $\operatorname E(X^2)$.

$$P(X = 2) = 4 P(X = 3)
    \iff \frac{\lambda^2 e^{-\lambda}}{2!} = 4 \cdot \frac{\lambda^3 e^{-\lambda}}{3!}
    \iff \lambda = \frac{3}{4}$$
$$\operatorname E(X^2)
    = \operatorname V(X) + {\operatorname E(X)}^2
    = \lambda + \lambda^2
    = \frac{3}{4} + \frac{9}{16}
    = \frac{21}{16}
    = 1.3125$$

### Uniform

## Continuous Univariate Distributions

A random variable $Y$ has distribution function

$$F(y) = \begin{cases}
    0 & \operatorname{if} & y < 0 \\
    y^2 + 0.1 & \operatorname{if} & 0 \leq y < 0.5 \\
    y & \operatorname{if} & 0.5 \leq y < 1 \\
    1 & \operatorname{if} & y \geq 1
\end{cases}$$

1. Give $F_1(y)$ and $F_2(y)$, the discrete and continuous components of $F(y)$.

    $F$ jumps by $0.1$ at $y = 0$ and by $0.5 - 0.35 = 0.15$ at $y = 0.5$ (total discrete mass $0.25$), and has density $F'(y) = 2y$ on $(0, 0.5)$ and $1$ on $(0.5, 1)$ (total continuous mass $0.75$). Rescaling each component to a proper cdf:

    $$F_1(y) = \begin{cases}
        0 & \operatorname{if} & y < 0 \\
        0.4 & \operatorname{if} & 0 \leq y < 0.5 \\
        1 & \operatorname{if} & y \geq 0.5
    \end{cases}$$
    $$F_2(y) = \begin{cases}
        0 & \operatorname{if} & y < 0 \\
        \frac{4}{3} y^2 & \operatorname{if} & 0 \leq y < 0.5 \\
        \frac{4y - 1}{3} & \operatorname{if} & 0.5 \leq y < 1 \\
        1 & \operatorname{if} & y \geq 1
    \end{cases}$$

1. Write $F(y)$ as $c_1 F_1(y) + c_2 F_2(y)$.

    $$F(y) = 0.25 F_1(y) + 0.75 F_2(y)$$

1. Find the expected value and variance of $Y$.

    $$\operatorname E(Y)
        = 0 \cdot 0.1 + 0.5 \cdot 0.15
            + \int_0^{0.5} y \cdot 2y \, dy
            + \int_{0.5}^1 y \, dy \\
        = \frac{3}{40} + \frac{1}{12} + \frac{3}{8}
        = \frac{8}{15}
        \approx 0.5333$$
    $$\operatorname E(Y^2)
        = 0.5^2 \cdot 0.15
            + \int_0^{0.5} y^2 \cdot 2y \, dy
            + \int_{0.5}^1 y^2 \, dy \\
        = \frac{3}{80} + \frac{1}{32} + \frac{7}{24}
        = \frac{173}{480}$$
    $$\operatorname V(Y)
        = \frac{173}{480} - {\left(\frac{8}{15}\right)}^2
        = \frac{547}{7200}
        \approx 0.0760$$

---

An insurance company insures a large number of homes. The insured value $X$ of a randomly selected home is assumed to follow a distribution with density function

$$f(y) = \begin{cases}
    3x^{-4} & \operatorname{for} & x > 1 \\
    0 & & \text{otherwise}
\end{cases}$$

Given that a randomly selected home is insured for at least 1.5, what is the probability that it is insured for less than 2?

$$\int_a^b f(y) \, dx \\
    = \int_a^b 3x^{-4} \, dx \\
    = -x^{-3} \right|_a^b \\
    = -b^{-3} + a^{-3}$$
$$\frac{P(1.5 \leq x < 2)}{P(x \geq 1.5)} \\
    = \frac{\int_{1.5}^2 f(y) \, dx}{\int_{1.5}^\infty f(y) \, dx} \\
    = \frac{-2^{-3} + {1.5}^{-3}}{0 + {1.5}^{-3}} \\
    \approx 0.578$$

---

A random variable $X$ has the cumulative distribution function

$$F(x) = \begin{cases}
    0 & \operatorname{for} & x < 1 \\
    \frac{x^2 - 2x + 2}{2} & \operatorname{for} & 1 \leq x < 2 \\
    1 & \operatorname{for} & x \geq 2
\end{cases}$$

Calculate the variance of $X$.

$F$ jumps by $F(1) - F(1^-) = \frac{1}{2}$ at $x = 1$ and has density $F'(x) = x - 1$ on $(1, 2)$.

$$\operatorname E(X)
    = 1 \cdot \frac{1}{2} + \int_1^2 x (x - 1) \, dx
    = \frac{1}{2} + \frac{5}{6}
    = \frac{4}{3}$$
$$\operatorname E(X^2)
    = 1^2 \cdot \frac{1}{2} + \int_1^2 x^2 (x - 1) \, dx
    = \frac{1}{2} + \frac{17}{12}
    = \frac{23}{12}$$
$$\operatorname V(X)
    = \frac{23}{12} - {\left(\frac{4}{3}\right)}^2
    = \frac{5}{36}
    \approx 0.1389$$

### Beta

Suppose that

$$Y ~ \beta (2, 5)$$

Find the median and the 95<superscript>th</superscript> percentile for $Y$.

$$f(y)
    = \frac{\Gamma(7)}{\Gamma(2) \, \Gamma(5)} y {(1 - y)}^4
    = 30 y {(1 - y)}^4$$
$$F(y)
    = \int_0^y 30 t {(1 - t)}^4 \, dt
    = 1 - {(1 - y)}^5 (1 + 5y)$$

Solving $F(y) = 0.5$ and $F(y) = 0.95$ numerically:

$$m \approx 0.2644$$
$$\pi_{0.95} \approx 0.5818$$

### Exponential

### Gamma

In a medical experiment, a rat has been exposed to some radiation. The experimenters believe that the rat's survival time $X$ (in weeks) has the pdf

$$f(x) = \frac{3x^2}{120^3} e^{-\left(\frac{x}{120\right)}^3$$

$$0 < x < \infty$$

1. What is the probability that the rat survives at least 100 weeks?
    Let
    $$y = {\left(\frac{x}{120}\right)}^3$$
    $$dy = \frac{1}{40} \cdot {\left(\frac{x}{120}\right)}^2 \, dx$$
    $$dx = 40 \cdot {\left(\frac{120}{x}\right)}^2 \, dy$$
    $$\int_{100}^\infty f(x) \, dx \\
        = \int_{100}^\infty
            \frac{3x^2}{120^3}
            e^{-\left(\frac{x}{120\right)}^3
            \, dx \\
        = \int_{{\left(\frac{100}{120}\right)}^3}^\infty
            \frac{3x^2}{120^3} e^{-y}
            \cdot 40
            \cdot {\left(\frac{120}{x}\right)}^2
            \, dy \\
        = \int_{\frac{125}{216}}^\infty e^{-y} \, dy \\
        = (-e^{-y}) \right|_{\frac{125}{216}}^\infty \\
        = e^{-y} \right|_\infty^{\frac{125}{216}}
        = e^{-\frac{125}{216}}$$
1. Find the expected value of the survival time. *Hint*: In the integral representing $\operatorname E(X)$, let

$$y = {\left(\frac{x}{120}\right)}^3$$

and get the answer in terms of a gamma function.

With $y = {\left(\frac{x}{120}\right)}^3$, so that $x = 120 y^{\frac{1}{3}}$ and $dy = \frac{3x^2}{120^3} \, dx$:

$$\operatorname E(X)
    = \int_0^\infty x \cdot \frac{3x^2}{120^3} e^{-{\left(\frac{x}{120}\right)}^3} \, dx \\
    = \int_0^\infty 120 y^{\frac{1}{3}} e^{-y} \, dy \\
    = 120 \, \Gamma{\left(\frac{4}{3}\right)}
    = 40 \, \Gamma{\left(\frac{1}{3}\right)}
    \approx 107.2 \text{ weeks}$$

### Normal

### Uniform

If $Y$ is uniformly distributed over (0, 5), what is the probability that the roots of the equation

$$4x^2 + 4xY + Y + 2 = 0$$

are both real?

The roots are real iff the discriminant is nonnegative:

$${(4Y)}^2 - 4 \cdot 4 (Y + 2) \geq 0
    \iff Y^2 - Y - 2 \geq 0 \\
    \iff (Y - 2)(Y + 1) \geq 0$$

On $(0, 5)$ this holds only for $Y \geq 2$, so

$$P(Y \geq 2) = \frac{5 - 2}{5 - 0} = \frac{3}{5}$$

## Applications

A pharmaceutical company wants to know whether an experimental drug has an effect on systolic blood pressure. Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact, their systolic blood pressures were recorded. The data appear below:

```
[172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]

```

1. Approximate the value of $s$ using the range approximation.

    $$s \approx \frac{172 - 108}{4} = 16$$

2. Calculate the values of $\bar y$ and $s$ for the 15 blood pressure readings.

    $$\bar y =
        \frac{172
            + 140
            + 123
            + 130
            + 115
            + 148
            + 108
            + 129
            + 137
            + 161
            + 123
            + 152
            + 133
            + 128
            + 142}{15}
        \approx 136$$
    $$s = \sqrt{\frac{{172 - 136}^2
        + {140 - 136}^2
        + {123 - 136}^2
        + {130 - 136}^2
        + {115 - 136}^2
        + {148 - 136}^2
        + {108 - 136}^2
        + {129 - 136}^2
        + {137 - 136}^2
        + {161 - 136}^2
        + {123 - 136}^2
        + {152 - 136}^2
        + {133 - 136}^2
        + {128 - 136}^2
        + {142 - 136}^2}{15 - 1}}
        = 17.1$$

3. Let $k \geq 1$. For any set of $n$ measurements, the fraction included in the interval $\bar y - ks$ to $\bar y + ks$ is at least $1 - \frac{1}{k^2}$.
    
    $$s^2 = \frac{1}{n - 1}\sum_{i = 1}^n (y_i - \bar y)^2$$
    
    Find values $a$ and $b$ such that at least 75% of the blood pressure measurements lie between $a$ and $b$.

    $$1 - \frac{1}{k^2} = 0.75$$
    $$k = 2$$
    $$a = y - ks = 102$$
    $$b = y + ks = 170$$

4. Did Tchebysheff's theorem work? That is, use the data to find the actual percent of blood pressure readings that are between the values $a$ and $b$ you found in *(3)*. Is this actual percentage greater than 75%?
    
    Yes

---

A tour operator has a bus that can accommodate 20 tourists. The operator knows that tourists may not show up, so he sells 21 tickets. The probability that an individual tourist will not show up is 0.02, independent of all other tourists. Each ticket costs 50 and is non-refundable if a tourist fails to show up. If a tourist shows up and a seat is not available, the tour operator has to pay 100 (ticket cost + 50 penalty) to the tourist. What is the expected revenue of the tour operator?

Ticket revenue is a fixed $21 \cdot 50 = 1050$; since only one tourist can be left without a seat, the 100 payment occurs exactly when all 21 tourists show up.

$$\operatorname E(R)
    = 1050 - 100 \cdot P(\text{all 21 show up}) \\
    = 1050 - 100 \cdot {0.98}^{21} \\
    \approx 1050 - 65.43
    = 984.57$$

---

An auto insurance company insures an automobile worth 15,000 for one year under a policy with a 1,000 deductible. During the policy year there is a 0.04 chance of partial damage to the car and a 0.02 chance of a total loss of the car. If there is partial damage to the car, the amount $X$ of damage (in thousands) follows a distribution with density function

$$f(x) = \begin{cases}
    0.5003e^{-\frac{x}{2}} & \operatorname{for} & 0 < x < 15 \\
    0 & & \text{otherwise}
\end{cases}$$

What is the expected claim payment?

With the 1 deductible (in thousands), a total loss pays $15 - 1 = 14$ and partial damage pays $\max(X - 1, 0)$, where $X$ has density $f(x) = 0.5003 e^{-\frac{x}{2}}$ on $(0, 15)$.

$$\int_1^{15} (x - 1) \cdot 0.5003 e^{-\frac{x}{2}} \, dx \\
    = 0.5003 \left[ -(2x + 2) e^{-\frac{x}{2}} \right]_1^{15} \\
    = 0.5003 \left( 4 e^{-\frac{1}{2}} - 32 e^{-\frac{15}{2}} \right)
    \approx 1.2049$$
$$\operatorname E(\text{claim})
    = 0.04 \cdot 1.2049 + 0.02 \cdot 14
    \approx 0.3282 \text{ thousand}
    \approx 328$$

---

The cumulative distribution function for health care costs experienced by a policyholder is modeled by the function

$$F(x) = \begin{cases}
    1 - e^{-\frac{x}{100}} & x > 0 \\
    0, & \text{otherwise}
\end{cases}$$

The policy has a deductible of 20. An insurer reimburses the policyholder for 100% of health care costs between 20 and 120. Health care costs above 120 are reimbursed at 50%. Let $G$ be the cumulative distribution function of reimbursements given that the reimbursement is positive. Calculate $G(115)$.

The reimbursement as a function of the cost $X$ is

$$R = \begin{cases}
    X - 20 & \operatorname{if} & 20 < X \leq 120 \\
    100 + 0.5 (X - 120) & \operatorname{if} & X > 120
\end{cases}$$
$$R \leq 115
    \iff 100 + 0.5 (X - 120) \leq 115
    \iff X \leq 150$$
$$G(115)
    = P(X \leq 150 \mid X > 20)
    = \frac{F(150) - F(20)}{1 - F(20)} \\
    = \frac{e^{-0.2} - e^{-1.5}}{e^{-0.2}}
    = 1 - e^{-1.3}
    \approx 0.7275$$

---

Let $F(x)$ represent the fraction of payroll earned by the highest paid fraction $x$ of employees in a company (for example, $F(0.2) = 0.5$ means that the highest paid 20% of workers earn 50% of the payroll). Gini's index of inequality, $G$ is one way to measure how evenly payroll is distributed among all employees and is defined as follows:

$$G = 2 \int_0^1 \lvert x - F(x) \rvert \, dx$$

In a certain company, the distribution of payroll is described by the density function:

$$f(x) = 3 {(1 - x)}^2$$

$$0 \leq x \leq 1$$

Calculate $G$ for this company.

The highest paid fraction $x$ earns

$$F(x)
    = \int_0^x 3 {(1 - t)}^2 \, dt
    = 1 - {(1 - x)}^3
    \geq x \quad \operatorname{on} \quad [0, 1]$$
$$G
    = 2 \int_0^1 \left( 1 - {(1 - x)}^3 - x \right) dx \\
    = 2 \left( 1 - \frac{1}{4} - \frac{1}{2} \right)
    = \frac{1}{2}$$

---

A thief is in a sinister, diabolical, fiendish, dark, circular dungeon with three identical doors. Once the thief chooses a door and passes through it, the door locks behind him. The three doors lead to

- a 6-hour tunnel that leads to freedom
- a 3-hour tunnel that returns him to the dungeon
- a 9-hour tunnel that returns him to the dungeon

Each door is chosen with equal probability. When he is dropped back into the dungeon by the second and third doors, he is a "Markov" thief in the sense that there is a memoryless choice of doors. He isn't able to mark the doors in any way. What is his expected time to escape?

$$E(t)
    = \frac{6 + (3 + E(t)) + (9 + E(t))}{3}
    = 6 + \frac{2E(t)}{3}$$
$$E(t) = 18$$
18 hours
