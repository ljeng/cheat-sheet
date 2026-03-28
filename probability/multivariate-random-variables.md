# Multivariate Random Variables

## Multivariate Distributions

Suppose that if a signal value $s$ is sent from location A, then the signal value received at location B is normally distributed with parameters ($s$, 1). $S$ is normally distributed with parameters ($\mu$, $\sigma^2$). Let $S$ denote the signal sent and $R$ the signal received.

1. Compute $\operatorname E\[R\]$.
1. Compute $\operatorname{Var}(R)$.
1. Is $R$ normally distributed?
1. Compute $\operatorname{Cov}(R, S)$.

---

Choose a random integer $X$ from the interval [0, 4]. Then choose a random integer $Y$ from the interval [0, $x$], where $x$ is the observed value of $X$. Make assumptions about the marginal pmf $f_X(x)$ and the conditional pmf $h(y | x)$ and compute $P(X + Y > 4)$.

## The Distribution of Order Statistics for Independent Random Variables

If $X_1, X_2, X_3, X_4, X_5$ are independent and identically distributed exponential random variables with the parameter $\lambda$, compute

1. $P \lbrace \operatorname{min}(X_1, \ldots, X_5) \leq a \rbrace$
1. $P \lbrace \operatorname{max}(X_1, \ldots, X_5) \leq a \rbrace$

---

Let $Y_1, Y_2, \ldots,Y_n$ denote a random sample from the uniform distribution $f(y) = 1, 0 \leq y \leq 1$. Find the probability density function for the range $R = Y_{(n)} − Y_{(1)}$

## Linear Combinations of Independent Random Variables

A.J. has 20 jobs that she must do in sequence, with the times required to do each of these jobs being independent random variables with mean 50 minutes and standard deviation 10 minutes. M.J. has 20 jobs that he must do in sequence, with the times required to do each of these jobs being independent random variables with mean 52 minutes and standard deviation 15 minutes.

1. Find the probability that A.J. finishes in less than 900 minutes.
1. Find the probability that M.J. finishes in less than 900 minutes.
1. Find the probability that A.J. finishes before M.J.

---

If $Y_1$ and $Y_2$ are independent random variables, each having a normal distribution with mean 0 and variance 1, find the moment-generating function of $U = Y_1 Y_2$. Use this moment-generating function to find $\operatorname E(U)$ and $\operatorname V(U)$. Check the result by evaluating $\operatorname E(U)$ and $\operatorname V(U)$ directly from the density functions for $Y_1$ and $Y_2$.

---

A charity receives 2025 contributions. Contributions are assumed to be independent and identically distributed with mean 3125 and standard deviation 250. Calculate the approximate 90<superscript>th</superscript> percentile for the distribution of the total contributions received.

---

The number of trees in one acre has a Poisson distribution with mean 60. Assuming independence, compute $P(5950 \leq X \leq 6100)$, approximately, where $X$ is the number of trees in 100 acres.

## Associated Applications

The times to process orders at the service counter of a pharmacy are exponentially distributed with mean 10 minutes. If 100 customers visit the counter in a 2-day period, what is the probability that at least half of them need to wait more than 10 minutes?
