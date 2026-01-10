# Robustness

Robustness isn't a single metric in computer science. But it's a pervasive attribute. It describes an algorithm's ability to handle diverse inputs. It describes a system's capacity to function under stress. It describes code's flexibility to adapt to changing requirements. Robust fundamental software extends from the mathematical proofs of recurrences to the architectural design of data structures.

Robustness refers to a proof method's reliability when analyzing algorithm complexity. The **substitution method** stands out as an example in the study of recurrences. To use this method, one guesses the form of a bound and then uses mathematical induction to prove the guess correct and solve for constants. This requires a strong initial intuition proof - albeit it's perhaps the most robust method for solving recurrences, as it can be applied to a wide variety of recursive structures where simpler master theorems fail.

Just because you're asked to write code to check if a tic-tac-toe board has a winner doesn't mean you must assume a $3 \times 3$ board. Why not write the code in a more general way that implements it for an $N \times N$ board? Writing flexible code uses variables instead of hard-coded values in templates. If a problem can be solved in a more general way without adding excessive complexity, it should be. However, finesse must prevail - if a generalized solution poses a daunting task or seems unnecessary for the current scope, it's better to implement the expected case. Robustness should substantiate the project, not complicate it.

A way to design a good **hash function** for variable-length inputs is to use a hash function designed for cryptographic applications. Cryptic pseudorandom functions are widely implemented. The adjacency-list **representation** is quite robust. You can modify adjacency lists to represent weighted graphs[^1].

True robustness is found in simplicity rather than complexity.

> A designer knows he has arrived at perfection not when there is no longer anything to add, but when there is no longer anything to take away.

-- <cite>Antoine de Saint-Exupéry, aircraft designer</cite>

Programmers should judge their work by this criterion. Simple programs are more secure than their complex counterparts. They're easier to maintain and - most importantly - less likely to fail in unexpected ways.

Robustness is a virtue that exists in tension with efficiency. Efficiency is easily measured - we can objectively state that one program is $2.5 \times$ faster than another. Discussions on user interfaces, for instance, often get bogged down in personal tastes. We forge software that's not just fast but enduring by building on proven mathematical foundations.

[^1]: by storing weights within the list
