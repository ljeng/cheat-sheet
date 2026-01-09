# Trade-offs

There's rarely a single correct answer in SWE. Every design choice - from the way we hire to the way we structure a loop - embodies a trade-off, an inescapable compromise shaped by the discord among time, space, complexity, and elegance.

A wise programmer navigates the design space before writing a single line of code. The goal is not just to solve the problem but to solve the *right* problem.

## The Ten Commandments for Programmers

1. Work on the right problem.
2. Navigate the design space.
3. Look at the data.
4. Use back-of-the-envelope calculations.
5. Exploit symmetry.
6. Design with components.
7. Build prototypes.
8. **Make trade-offs when you have to.**
9. Keep it simple.
10. Strive for elegance.

---

There's no single design for TinyURL that works **perfectly**. Two excellent engineers might produce substantially different designs because they begin from different initial assumptions. Explain your choices; that's more important than the solution itself.

The most classic trade-off in computer science is between execution speed and memory consumption. Hash tables are the quintessential example - they achieve constant-time lookup in **exchange** for increased memory usage. Conversely, a two-pass algorithm might halve a program's **space** requirements but double its runtime, illustrating how optimization is a delicate balancing act; yet, in rare and serendipitous cases, compressing space occasionally *also* liberates time. For example, using a compact bitmap enables a dataset to reside entirely in main memory, avoiding the massive time penalty of disk access. **Dynamic programming** is a deliberate trade-off: we use additional memory to store subproblem solutions, which can transform an exponential-time algorithm into a polynomial-time one[^1].

How you implement an algorithm is just as important as the algorithm itself. **Recursion** is more elegant and simpler to implement[^2], it carries the call stack's overhead. **Iterative** solutions are more performant but harder to write. An **array** is superior for fixed sets of ASCII strings when building a lookup table[^3]. However, a **hash table** is better suited for sparse sets of Unicode strings. No single **sorting** algorithm is optimal in all cases. An algorithm with a terrible worst-case[^4] is the best choice for nearly sorted data, while others are chosen for their low memory footprint.

Trade-offs shift toward modularity at the system level. Of course, to have multiple processes increases **flexibility** but also increases **complexity** in database design. You risk creating a system that's hopelessly convoluted if you try to account for every possible edge case. An online monolith[^5] decreases **modularity** and increases complexity because it requires tight integration between components. It may be the only way to meet **performance** requirements in a controlled environment. There are many ways to **design objects**. You should generally trade immediate cleverness for ease of maintenance.

Programming is an exercise in optimism, but wise programmers build for failure. For a **small function, the path to a gem is long** - define the problem, select data structures, write elegant pseudocode, and build **scaffolding**. Build a test harness to probe a function in isolation rather than slipping the function into a massive system and hoping it runs. The result is a program you can actually trust. Don't take the easy path. Groping around in a huge system to fix an integrated function is a disaster. Build the tools to test it thoroughly first.

Trade-offs even exist in how we build our teams. From a company perspective, it's acceptable to reject some good candidates[^6] provided that those who *are* hired are truly excellent. This is a trade-off between recruiting costs and workforce quality. If you need to hire exactly once without interviewing everyone, you must decide when to stop looking. This is the ultimate trade-off: minimizing the amount of interviewing versus maximizing the quality of the hire.

Whether you're choosing between a 32-bit and 64-bit architecture or deciding whether to add an optimization that makes code harder to read, remember: **everything has a cost**. A strong developer isn't one who knows the best way but one who understands the trade-offs among disparate solutions and knows when to use each one.

[^1]: rod cutting
[^2]: as seen in depth-first search
[^3]: for finding non-repeated characters
[^4]: like Quicksort
[^5]: processing data as it arrives
[^6]: false negatives
