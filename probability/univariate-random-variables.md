# Univariate Random Variables

## Discrete Univariate Distributions

Let

$$m(t) = \frac{1}{6} e^t + \frac{2}{6} e^{2t} + \frac{3}{6} e^{3t}$$

Find the following:

1. $\operatorname E(Y)$
1. $\operatorname V(Y)$
1. The distribution of $Y$

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

Suppose that

$$Y ~ \Beta (2, 5)$$

Find the median and the 95<superscript>th</superscript> percentile for $Y$.

### Exponential

### Gamma

In a medical experiment, a rat has been exposed to some radiation. The experimenters believe that the rat's survival time $X$ (in weeks) has the pdf

$$f(x) = \frac{3x^2}{120^3} e^{-\frac{x}{120}}^3$$

$$0 < x < \infty$$

1. What is the probability that the rat survives at least 100 weeks?
1. Find the expected value of the survival time. *Hint*: In the integral representing $\operatorname E(X)$, let

$$y = {\left(\frac{x}{120}\right)}^3$$

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

---

The cumulative distribution function for health care costs experienced by a policyholder is modeled by the function

$$F(x) = \begin{cases}
    1 - e^{-\frac{x}{100}} & x > 0 \\
    0, & \text{otherwise}
\end{cases}$$

The policy has a deductible of 20. An insurer reimburses the policyholder for 100% of health care costs between 20 and 120. Health care costs above 120 are reimbursed at 50%. Let $G$ be the cumulative distribution function of reimbursements given that the reimbursement is positive. Calculate $G(115)$.

---

Let $F(x)$ represent the fraction of payroll earned by the highest paid fraction $x$ of employees in a company (for example, $F(0.2) = 0.5$ means that the highest paid 20% of workers earn 50% of the payroll). Gini's index of inequality, $G$ is one way to measure how evenly payroll is distributed among all employees and is defined as follows:

$$G = 2 \int_0^1 |x - F(x)| \, dx$$

In a certain company, the distribution of payroll is described by the density function:

$$f(x) = 3 {(1 - x)}^2$$

$$0 \leq x \leq 1$$

Calculate $G$ for this company.
