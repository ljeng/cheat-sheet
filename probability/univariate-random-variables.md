# Univariate Random Variables

## Discrete Univariate Distributions

Let

$$m(t) = \frac{1}{6} e^t + \frac{2}{6} e^{2t} + \frac{3}{6} e^{3t}$$

Find the following:

1. $\operatorname E(Y)$
1. $\operatorname V(Y)$
1. The distribution of $Y$

### Binomial

### Geometric

In modeling the number of claims filed by an individual under an automobile policy during a three-year period, an actuary makes the simplifying assumption that for all integers $n \geq 0$

$$p_{n + 1} = \frac{1}{5} p_n$$

where $p_n$ represents the probability that the policyholder files $n$ claims during the period. Under this assumption, what is the probability that a policyholder files more than one claim during the period?

### Hypergeometric

### Negative Binomial

If

$$M_x(t) = {\left(\frac{0.70}{1 - 0.3e^t}\right)}^5$$

what is the distribution of $X$?

### Poisson

There are three highways in the county. The number of daily accidents that occur on these highways are Poisson random variables with respective parameters 0.3, 0.5, and 0.7. Find the expected number of accidents that will happen on any of these highways today.

---

Assume that a policyholder is four times more likely to file exactly two claims as to file exactly three claims. Assume also that the number $X$ of claims of this policyholder is Poisson. Determine the expectation $\operatorname E(X^2)$.

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
1. Write $F(y)$ as $c_1 F_1(y) + c_2 F_2(y)$.
1. Find the expected value and variance of $Y$.

---

An insurance company insures a large number of homes. The insured value $X$ of a randomly selected home is assumed to follow a distribution with density function

$$f(y) = \begin{cases}
    3x^{-4} & \operatorname{for} & x > 1 \\
    0 & & \text{otherwise}
\end{cases}$$

Given that a randomly selected home is insured for at least 1.5, what is the probability that it is insured for less than 2?

---

A random variable $X$ has the cumulative distribution function

$$F(x) = \begin{cases}
    0 & \operatorname{for} & x < 1 \\
    \frac{x^2 - 2x + 2}{2} & \operatorname{for} & 1 \leq x < 2 \\
    1 & \operatorname{for} & x \geq 2
\end{cases}$$

Calculate the variance of $X$.

### Beta

### Exponential

### Gamma

In a medical experiment, a rat has been exposed to some radiation. The experimenters believe that the rat's survival time $X$ (in weeks) has the pdf

$$ f(x) = \frac{3x^2}{120^3} e^{-\frac{x}{120}}^3$

$$0 < x < \infty$$

1. What is the probability that the rat survives at least 100 weeks?
1. Find the expected value of the survival time. *Hint*: In the integral representing $\operatorname E(X)$, let

$$y = {\frac{x}{120}}^3$$

and get the answer in terms of a gamma function.

### Normal

### Uniform

If $Y$ is uniformly distributed over (0, 5), what is the probability that the roots of the equation

$$4x^2 + 4xY + Y + 2 = 0$$

are both real?

## Applications

A pharmaceutical company wants to know whether an experimental drug has an effect on systolic blood pressure. Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact, their systolic blood pressures were recorded. The data appear below:

```
[172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]
```

1. Approximate the value of $s$ using the range approximation.
2. Calculate the values of $\bar{y}$ and $s$ for the 15 blood pressure readings.
3. Let $k \geq 1$. For any set of $n$ measurements, the fraction included in the interval $\bar y - ks$ to $\bar y + ks$ is at least $1 - \frac{1}{k^2}$.
    
    $$s^2 = \frac{1}{n - 1}\sum_{i = 1}^n (y_i - \bar y)^2$$
    
    Find values $a$ and $b$ such that at least 75% of the blood pressure measurements lie between $a$ and $b$.
4. Did Tchebysheff's theorem work? That is, use the data to find the actual percent of blood pressure readings that are between the values $a$ and $b$ you found in *(3)*. Is this actual percentage greater than 75%?

---

A tour operator has a bus that can accommodate 20 tourists. The operator knows that tourists may not show up, so he sells 21 tickets. The probability that an individual tourist will not show up is 0.02, independent of all other tourists. Each ticket costs 50 and is non-refundable if a tourist fails to show up. If a tourist shows up and a seat is not available, the tour operator has to pay 100 (ticket cost + 50 penalty) to the tourist. What is the expected revenue of the tour operator?

---

An auto insurance company insures an automobile worth 15,000 for one year under a policy with a 1,000 deductible. During the policy year there is a 0.04 chance of partial damage to the car and a 0.02 chance of a total loss of the car. If there is partial damage to the car, the amount $X$ of damage (in thousands) follows a distribution with density function

$$f(x) = \begin{cases}
    0.5003e^{\frac{x}{2}} & \operatorname{for} & 0 < x < 15 \\
    0 & & \text{otherwise}
\end{cases}$$

What is the expected claim payment?
