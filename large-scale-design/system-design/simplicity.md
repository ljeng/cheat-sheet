# Simplicity

> Simplicity is a prerequisite for reliability.

-- <cite>Edsger W. Dijkstra</cite>

> Simplicity is the ultimate sophistication.

-- <cite>Leonardo da Vinci</cite>

We need to build simple systems if we want to design good software. There's not enough focus on simplicity. "Simple"[^01] means "one twist." "Complex" means "multiple twists" or "braided together." In software, this refers to whether it's folded together or not. People usually interchange "simple" with "easy." "Easy"[^02] means "near" or "familiar." All that's familiar is somewhat easy. Easiness is relative.

Simple things have one role, task, objective, or concept. They may be one dimension of a problem. They don't interleave issues. Simplicity doesn't mean one of a kind. An interface could have multiple methods and still be simple. Simplicity is objective.

Symptoms of complexity:

- explosion of the state space
- tight coupling
- tangled dependencies
- inconsistent naming
- special casing

[Moseley and Marks](https://curtclifton.net/papers/MoseleyMarks06a.pdf) look at which bits of complexity are accidental and which are essential. Essential complexity is inherent in the problem itself[^03]. It's the complexity that would exist even in an ideal dev environment. Accidental complexity is complexity arising from implementation choices, suboptimal language and infrastructure, and performance issues. It's the complexity that could be avoided. Software engineering's goal should be to eliminate accidental complexity as much as possible and assist with essential complexity.

Avoid state and control where they aren't absolutely essential. Separate complexity that's either truly essential, or useful from a practical point of view from the rest of the system. Separate logic from state and essential complexity from accidental complexity. These principles aren't new.[^04]

Separate out the system's pure logic.

Essential state is the foundation. Changes to the essential state may require changes in other specifications, but changes in other specifications may never require changes to the essential state specification. Changes to the essential state may require changes to the logic, but changes to accidental state and control should never affect the essential logic. Accidental state and control are the least important conceptually. Changes here should never affect the other components.

A sharp focus on true essentials and avoiding useless complexity leads to less code. Good abstractions hide complexity. However, unneeded data abstraction can increase complexity due to subjectivity in grouping data. The relational model involves minimal commitment to subjective groupings, and this commitment has only minimal impact on the rest of the system.

Abstraction is a good tool for removing complexity. Good abstractions hide implementation details and behind a simple interface. For example, high-level programming languages hide machine code, and SQL hides data structures and concurrency.

- *What?* Define abstractions[^05] as sets of functions. Make them small. Use polymorphism.
- *Who?* Define the data/entities your abstractions will use. Pass subcomponents as arguments. - Don't hardwire.
- *How?* Implement the details, using polymorphism and isolating implementations.
- *When? Where?* Avoid connecting objects directly; use queues to decouple them.
- *Why?* Use declarative systems to implement policies and rules. Rules tend to increase complex control flow.

Keep information simple. Don't use objects to handle information. Use generic constructs[^06] to manipulate information. Don't tie data logic to its representation. Avoid ORM where possible.

| Construct           | Use                  |
| ---------------- | --------------------- |
| values            | final, persistent collections      |
| functions           | stateless methods           |
| namespaces          | languages with good namespace support |
| data             | maps, arrays, sets, XML, JSON, etc.   |
| polymorphism         | protocols, type classes       |
| managed references      | Clojure, Haskell         |
| set functions         | libraries              |
| queues            | libraries                |
| declarative data manipulation | SQL, LINQ, Datalog     |
| rules             | libraries or Prolog           |

Choose simple tools. Write simple code. Simplify existing code by disentangling it.

Avoid tools[^07] that generate complex outputs. Reliability tools[^08] are good but secondary. They don't enforce simplicity; they're just a safety net. Simplify the problem before starting to code. Use abstractions and design upfront.

Isolate and gentrify a system's disordered parts. One frequently constructs a façade to put a pretty face in front of the unpleasant that's swept under the rug. Intention-revealing selectors expose functionality. Consolidation hems unregulated growth that may have occurred during prototyping or expansion.

Daily builds[^09] and keeping the last working version around are nearly universal practices among successful maintenance programmers. Rigorous testing[^10] is vital for ensuring a working system. Refactoring maintains order.

Functional programming (FP) has roots in the stateless lambda calculus, equivalent in computational power to the Turing machine. Whilst object-oriented programming was developed out of a desire to manage the stateful von Neumann architecture, FP avoids state-related complexity. This has very significant benefits for testing and reasoning.

[^01]: from "sim" and "plex"
[^02]: from the Latin for "adjacent"
[^03]: as seen by the users
[^04]: [Kowalski's "Algorithm = Logic + Control"](https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf) is a classic example.
[^05]: interfaces, protocols
[^06]: maps, etc.
[^07]: constructs
[^08]: testing, refactoring
[^09]: Microsoft, Nortel
[^10]: extreme programming's unit tests
