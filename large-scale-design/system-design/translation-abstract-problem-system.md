# Translation of an Abstract Problem to a System

A limit order book is a set of outstanding limit orders at each price level. Prices are restricted to a discrete grid

$$\mathcal P = \\{k\delta, k = 1, 2, \ldots\\}$$

where $\delta > 0$ is the tick size. The limit order book consists of two sides: the ask side, which contains all sell limit orders, and the bid side, which contains all buy limit orders. Limit orders are stored in the order book until they are either executed against a market order or they are canceled.

We define an order $x$ as a tuple

$$x = (p, q, t)$$

where
- $p$ is the price
- $q$ is its size with positive values for buy orders and negative values for sell orders
- $t \in \mathbb R^+$ is the submission time

A limit order is an order to buy or sell a pre-specified quantity at a specified price or better. A market order is an order to buy or sell a specified quantity of an asset immediately at the best available price. A market order will generally execute at best ask or best bid. The state of the limit order book at time $t$ is the collection of all outstanding limit orders:

$$L(t) = \\{x : x \text{ is outstanding at time } t\\}$$

| Book | |
| --- | -------------------- |
| Bid | $$B(t) = \\{x \in L(t) \mid q_x > 0\\}$$ |
| Ask | $$A(t) = \\{x \in L(t) \mid q_x < 0\\}$$ |

Orders are ranked according to their price. A more aggressive price has priority - a high bid price or low ask price. Then sort on time. Orders entered earlier have priority. An order's individual priority is determined by its price and time. The best **bid** is the highest price at which there is a limit order to buy, and the best **ask** is the lowest price at which there is a limit order to sell:

$$b(t) := \max_{x \in B(t)} p(x)$$
$$a(t) := \min_{x \in A(t)} p(x)$$

Limit orders are executed strictly according to price then time priority. If the size of a market order exceeds the volume available at the best prevailing price, the remaining part of the market order executes at the next best available price, and so on, until the market order is fully filled. The gap between the best bid and best ask is called the bid-ask spread

$$s(t) := a(t) - b(t)$$

The order book is modified in real-time when a new order arrives or as an existing order is modified, canceled, or executed. Essentially, three types of orders can be submitted:

- A **limit order** (say a buy order) adds to the book if it is below the ask price or joins a FIFO queue and waits until it's filled or canceled.
- When a **cancellation** occurs, the canceled shares are removed from the corresponding queue in the order book.
- **Market orders** are executed against limit orders at the best available price. When your order size exceeds the available quantity at the best price, you experience slippage. Orders are allowed to "walk" up (down) the order book, consuming multiple price levels to complete a large order.
