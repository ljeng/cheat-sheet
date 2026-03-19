# Univariate Random Variables

## Discrete Univariate Distributions

#### Moments and Moment-generating Functions

Let

$$m(t) = \frac{1}{6} \exp t + \frac{2}{6} \exp {2t} + \frac{3}{6} \exp{3t}$$

Find the following:

1. $\operatorname E(Y)$
1. $\operatorname V(Y)$
1. The distribution of $Y$

### Binomial

### Geometric

### Hypergeometric

### Negative Binomial

### Poisson

There are three highways in the county. The number of daily accidents that occur on these highways are Poisson random variables with respective parameters 0.3, 0.5, and 0.7. Find the expected number of accidents that will happen on any of these highways today.

## Continuous Univariate Distributions

A random variable $Y$ has distribution function

$$F(y) =
\begin{cases}
    0 \operatorname{if} y < 0
    y^2 + 0.1 \operatorname{if} 0 \leq y < 0.5
    y \operatorname{if} 0.5 \leq y < 1
    1 \operatorname{if} y \geq 1
\end{cases}$$

1. Give $F_1(y)$ and $F_2(y)$, the discrete and continuous components of $F(y)$.
1. Write $F(y)$ as $c_1 F_1(y) + c_2 F_2(y)$.
1. Find the expected value and variance of $Y$.

### Beta

### Exponential

### Gamma

### Normal

### Uniform

If $Y$ is uniformly distributed over (0, 5), what is the probability that the roots of the equation $4x^2 + 4xY + Y + 2 = 0$ are both real?

## Applications

A pharmaceutical company wants to know whether an experimental drug has an effect on systolic blood pressure. Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact, their systolic blood pressures were recorded. The data appear below:

```
[172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]
```

1. Approximate the value of $s$ using the range approximation.
1. Calculate the values of $\bar y$ and $s$ for the 15 blood pressure readings.
1. Let $k \geq 1$. For any set of $n$ measurements, the fraction included in the interval $\bar y - ks$ to $\bar y + ks$ is at least $1 - \frac{1}{k^2}$.

$$s^2 = \frac{1}{n - 1}\[\sum_{i = 1}^n {(y_i - \bar y)}^2\]

Find values $a$ and $b$ such that at least 75% of the blood pressure measurements lie between $a$ and $b$.
1. Did Tchebysheff's theorem work? That is, use the data to find the actual percent of blood pressure readings that are between the values $a$ and $b$ you found in part *(c)*. Is this actual percentage greater than 75%?
