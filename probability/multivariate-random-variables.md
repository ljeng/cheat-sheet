# Multivariate Random Variables

## Multivariate Distributions

Suppose that if a signal value $s$ is sent from location A, then the signal value received at location B is normally distributed with parameters ($s$, 1). $S$ is normally distributed with parameters ($\mu$, $\sigma^2$). Let $S$ denote the signal sent and $R$ the signal received.

1. Compute $\operatorname E\[R\]$.

    $$\operatorname E\[R\] = \mu$$

1. Compute $\operatorname{Var}(R)$.

    Given $S = s$, $R \sim \operatorname N(s, 1)$, so $R = S + \varepsilon$ with $\varepsilon \sim \operatorname N(0, 1)$ independent of $S$.

    $$\operatorname{Var}(R) = \operatorname{Var}(S) + \operatorname{Var}(\varepsilon) \\
        = \sigma^2 + 1$$

1. Is $R$ normally distributed?

    Yes, because $R = S + \varepsilon$ is a sum of independent normal random variables, so $R \sim \operatorname N(\mu, \sigma^2 + 1)$.

1. Compute $\operatorname{Cov}(R, S)$.

    $$\operatorname{Cov}(R, S) = \operatorname{Cov}(S + \varepsilon, S) \\
        = \operatorname{Var}(S) + \operatorname{Cov}(\varepsilon, S) \\
        = \sigma^2$$

---

Choose a random integer $X$ from the interval [0, 4]. Then choose a random integer $Y$ from the interval [0, $x$], where $x$ is the observed value of $X$. Make assumptions about the marginal pmf $f_X(x)$ and the conditional pmf $h(y \| x)$ and compute $P(X + Y > 4)$.

Assume $f_X(x) = \frac{1}{5}$ for $x = 0, 1, \ldots, 4$ and $h(y \| x) = \frac{1}{x + 1}$ for $y = 0, 1, \ldots, x$, so $f(x, y) = \frac{1}{5(x + 1)}$. Then $X + Y > 4$ only for $(x, y) \in \lbrace (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (4, 4) \rbrace$:

$$P(X + Y > 4) = 2 \times \frac{1}{5 \times 4} + 4 \times \frac{1}{5 \times 5} \\
    = \frac{13}{50} = 0.26$$

---

Suppose that we have the following information about basketball player shoe size $S$, and player height $H$.

<table style="border-collapse: collapse">
    <tr>
        <td colspan="2" style="border: none"></td>
        <td colspan="3" style="border: none">
            <span>H = Height</span>
        </td>
    </tr>
    <tr>
        <td colspan="2" style="border: none"></td>
        <th>68</th>
        <th>70</th>
        <th>73</th>
    </tr>
    <tr>
        <td rowspan="2" style="border: none">S = Shoe Size</td>
        <th>8.5</th>
        <td>0.25</td>
        <td>0.20</td>
        <td>0.15</td>
    </tr>
    <tr>
        <th>12</th>
        <td>0.05</td>
        <td>0.12</td>
        <td>?</td>
    </tr>
</table>

1. Find the expected height and expected shoe size of a basketball player.

    The missing entry is $1 - (0.25 + 0.20 + 0.15 + 0.05 + 0.12) = 0.23$, giving marginals $f_H = (0.30, 0.32, 0.38)$ and $f_S = (0.60, 0.40)$.

    $$\operatorname E\[H\] = 68(0.30) + 70(0.32) + 73(0.38) \\
        = 70.54$$

    $$\operatorname E\[S\] = 8.5(0.60) + 12(0.40) \\
        = 9.9$$

1. Find the expected shoe size, given that a player is 73 inches tall, $\operatorname E \lbracket S \| H = 73 \rbracket$.

    $$\operatorname E \lbracket S \| H = 73 \rbracket = \frac{8.5(0.15) + 12(0.23)}{0.38} \\
        = \frac{4.035}{0.38} \\
        \approx 10.62$$

1. Find the conditional coefficient of variation for shoe size, given the player is 5'8" tall.

    $$P(S = 8.5 \| H = 68) = \frac{0.25}{0.30} = \frac{5}{6}, \quad P(S = 12 \| H = 68) = \frac{1}{6}$$

    $$\operatorname E \lbracket S \| H = 68 \rbracket = 8.5 \times \frac{5}{6} + 12 \times \frac{1}{6} = \frac{109}{12}$$

    $$\operatorname{Var}(S \| H = 68) = 8.5^2 \times \frac{5}{6} + 12^2 \times \frac{1}{6} - \left( \frac{109}{12} \right)^2 \\
        = \frac{245}{144}$$

    $$\operatorname{CV}(S \| H = 68) = \frac{\sqrt{245 / 144}}{109 / 12} \\
        = \frac{7 \sqrt{5}}{109} \\
        \approx 0.1436$$

## The Distribution of Order Statistics for Independent Random Variables

If $X_1, X_2, X_3, X_4, X_5$ are independent and identically distributed exponential random variables with the parameter $\lambda$, compute

1. $P \lbrace \operatorname{min}(X_1, \ldots, X_5) \leq a \rbrace$

    $$P \lbrace \operatorname{min}(X_1, \ldots, X_5) \leq a \rbrace = 1 - P(X_1 > a, \ldots, X_5 > a) \\
        = 1 - \left( e^{-\lambda a} \right)^5 \\
        = 1 - e^{-5 \lambda a}$$

1. $P \lbrace \operatorname{max}(X_1, \ldots, X_5) \leq a \rbrace$

    $$P \lbrace \operatorname{max}(X_1, \ldots, X_5) \leq a \rbrace = P(X_1 \leq a, \ldots, X_5 \leq a) \\
        = \left( 1 - e^{-\lambda a} \right)^5$$

---

Let $Y_1, Y_2, \ldots,Y_n$ denote a random sample from the uniform distribution $f(y) = 1, 0 \leq y \leq 1$. Find the probability density function for the range $R = Y_{(n)} − Y_{(1)}$

The joint density of $\left( Y_{(1)}, Y_{(n)} \right)$ is $g(y_1, y_n) = n(n - 1)(y_n - y_1)^{n - 2}$ for $0 \leq y_1 \leq y_n \leq 1$. Fixing $R = y_n - y_1 = r$ and integrating out the minimum:

$$f_R(r) = \int_0^{1 - r} n(n - 1) r^{n - 2} \, dy_1 \\
    = n(n - 1) r^{n - 2} (1 - r), \quad 0 \leq r \leq 1$$

---

Let $X_1, X_2, \ldots, X_n$ be a random sample from a $\operatorname U(0, 1)$ population. Find the distribution of the sample range $X_{(n)} - X_{(1)}$.

The joint density of $\left( X_{(1)}, X_{(n)} \right)$ is $g(u, v) = n(n - 1)(v - u)^{n - 2}$ for $0 \leq u \leq v \leq 1$. With $R = X_{(n)} - X_{(1)} = r$:

$$f_R(r) = \int_0^{1 - r} n(n - 1) r^{n - 2} \, du \\
    = n(n - 1) r^{n - 2} (1 - r), \quad 0 \leq r \leq 1$$

$$F_R(r) = \int_0^r n(n - 1) t^{n - 2} (1 - t) \, dt \\
    = n r^{n - 1} - (n - 1) r^n, \quad 0 \leq r \leq 1$$

that is, $R \sim \operatorname{Beta}(n - 1, 2)$.

## Linear Combinations of Independent Random Variables

A.J. has 20 jobs that she must do in sequence, with the times required to do each of these jobs being independent random variables with mean 50 minutes and standard deviation 10 minutes. M.J. has 20 jobs that he must do in sequence, with the times required to do each of these jobs being independent random variables with mean 52 minutes and standard deviation 15 minutes.

1. Find the probability that A.J. finishes in less than 900 minutes.

    By the CLT, A.J.'s total time $A$ is approximately normal with mean $20 \times 50 = 1000$ and variance $20 \times 10^2 = 2000$.

    $$P(A < 900) \approx \Phi \left( \frac{900 - 1000}{\sqrt{2000}} \right) \\
        = \Phi(-2.236) \\
        \approx 0.0127$$

1. Find the probability that M.J. finishes in less than 900 minutes.

    M.J.'s total time $M$ is approximately normal with mean $20 \times 52 = 1040$ and variance $20 \times 15^2 = 4500$.

    $$P(M < 900) \approx \Phi \left( \frac{900 - 1040}{\sqrt{4500}} \right) \\
        = \Phi(-2.087) \\
        \approx 0.0184$$

1. Find the probability that A.J. finishes before M.J.

    $A - M$ is approximately normal with mean $1000 - 1040 = -40$ and variance $2000 + 4500 = 6500$.

    $$P(A < M) = P(A - M < 0) \approx \Phi \left( \frac{0 - (-40)}{\sqrt{6500}} \right) \\
        = \Phi(0.496) \\
        \approx 0.6901$$

---

If $Y_1$ and $Y_2$ are independent random variables, each having a normal distribution with mean 0 and variance 1, find the moment-generating function of $U = Y_1 Y_2$. Use this moment-generating function to find $\operatorname E(U)$ and $\operatorname V(U)$. Check the result by evaluating $\operatorname E(U)$ and $\operatorname V(U)$ directly from the density functions for $Y_1$ and $Y_2$.

Conditioning on $Y_1$ and using the $\operatorname N(0, 1)$ mgf $\operatorname E\[e^{s Y_2}\] = e^{s^2 / 2}$ with $s = t Y_1$, then the $\chi_1^2$ mgf $\operatorname E\[e^{\theta Y_1^2}\] = (1 - 2 \theta)^{-1/2}$ with $\theta = t^2 / 2$:

$$m_U(t) = \operatorname E\[\operatorname E\[e^{t Y_1 Y_2} \| Y_1\]\] \\
    = \operatorname E\[e^{t^2 Y_1^2 / 2}\] \\
    = (1 - t^2)^{-1/2}, \quad \lvert t \rvert < 1$$

$$m_U'(t) = t (1 - t^2)^{-3/2}, \quad m_U''(t) = (1 - t^2)^{-3/2} + 3 t^2 (1 - t^2)^{-5/2}$$

$$\operatorname E(U) = m_U'(0) = 0, \quad \operatorname V(U) = m_U''(0) - 0^2 = 1$$

Directly, by independence: $\operatorname E(U) = \operatorname E(Y_1) \operatorname E(Y_2) = 0$ and $\operatorname V(U) = \operatorname E(Y_1^2) \operatorname E(Y_2^2) - 0^2 = 1 \times 1 = 1$, matching.

---

A charity receives 2025 contributions. Contributions are assumed to be independent and identically distributed with mean 3125 and standard deviation 250. Calculate the approximate 90<sup>th</sup> percentile for the distribution of the total contributions received.

Let $T$ be the total of the 2025 contributions. By the CLT, $T$ is approximately normal with

$$\operatorname E\[T\] = 2025 \times 3125 = 6328125, \quad \operatorname{sd}(T) = 250 \sqrt{2025} = 11250$$

$$\pi_{0.90} \approx 6328125 + 1.282 \times 11250 \\
    = 6342547.5$$

---

What is the expected number of rolls of a fair die required to see all six outcomes? What is the population variance of the number of rolls of a fair die required to see all six outcomes?

Write $N = \sum_{i = 1}^6 N_i$, where $N_i$, the number of additional rolls to see the $i$-th new face, is $\operatorname{Geometric} \left( p_i = \frac{7 - i}{6} \right)$; the $N_i$ are independent.

$$\operatorname E\[N\] = \sum_{i = 1}^6 \frac{6}{7 - i} \\
    = 6 \left( 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} \right) \\
    = \frac{147}{10} = 14.7$$

$$\operatorname{Var}(N) = \sum_{i = 1}^6 \frac{1 - p_i}{p_i^2} \\
    = 0 + \frac{6}{25} + \frac{3}{4} + 2 + 6 + 30 \\
    = \frac{3899}{100} = 38.99$$

---

The number of trees in one acre has a Poisson distribution with mean 60. Assuming independence, compute $P(5950 \leq X \leq 6100)$, approximately, where $X$ is the number of trees in 100 acres.

$X$ is a sum of 100 independent $\operatorname{Poisson}(60)$ counts, so $X \sim \operatorname{Poisson}(6000)$ with mean and variance 6000. Using the normal approximation with continuity correction:

$$P(5950 \leq X \leq 6100) \approx \Phi \left( \frac{6100.5 - 6000}{\sqrt{6000}} \right) - \Phi \left( \frac{5949.5 - 6000}{\sqrt{6000}} \right) \\
    = \Phi(1.297) - \Phi(-0.652) \\
    \approx 0.6455$$

(The exact Poisson probability is 0.6449.)

## Associated Applications

The times to process orders at the service counter of a pharmacy are exponentially distributed with mean 10 minutes. If 100 customers visit the counter in a 2-day period, what is the probability that at least half of them need to wait more than 10 minutes?

$P(\text{wait} > 10) = e^{-10 / 10} = e^{-1} \approx 0.3679$, so the number who wait more than 10 minutes is $W \sim \operatorname{Binomial}(100, e^{-1})$ with mean $100 e^{-1} \approx 36.79$ and standard deviation $\sqrt{100 e^{-1} (1 - e^{-1})} \approx 4.822$. Using the normal approximation with continuity correction:

$$P(W \geq 50) \approx 1 - \Phi \left( \frac{49.5 - 36.79}{4.822} \right) \\
    = 1 - \Phi(2.636) \\
    \approx 0.0042$$

(The exact binomial probability is 0.0047.)

---

A driver and a passenger are in a car accident. Each of them independently has probability 0.3 of being hospitalized. When a hospitalization occurs, the loss is uniformly distributed on [0, 1]. When two hospitalizations occur, the losses are independent. Calculate the expected number of people in the car who are hospitalized, given that the total loss due to hospitalizations from the accident is less than 1.

$N \sim \operatorname{Binomial}(2, 0.3)$: $P(N = 0) = 0.49$, $P(N = 1) = 0.42$, $P(N = 2) = 0.09$. Let $L$ be the total loss: $P(L < 1 \| N \leq 1) = 1$, while for two independent uniform losses $P(L < 1 \| N = 2) = \frac{1}{2}$.

$$\operatorname E \lbracket N \| L < 1 \rbracket = \frac{1(0.42)(1) + 2(0.09) \left( \frac{1}{2} \right)}{0.49 + 0.42 + 0.09 \left( \frac{1}{2} \right)} \\
    = \frac{0.51}{0.955} \\
    = \frac{102}{191} \approx 0.5340$$

---

Cassie is interested in determining the average gas mileage for a fleet of a particular model of car. Previous data collection of gas mileage gives her confidence that the standard deviation of the gas mileages that she collects will have a standard deviation of 3.3 miles per gallon. How many cars should she sample in order to be at least 95% certain that the difference between the population mean and sample mean is less than 1 mile per gallon?

Require $P(\lvert \bar{X} - \mu \rvert < 1) \geq 0.95$, i.e. $\frac{1.96 \times 3.3}{\sqrt{n}} \leq 1$:

$$n \geq (1.96 \times 3.3)^2 = 41.84 \\
    \Rightarrow n = 42$$
