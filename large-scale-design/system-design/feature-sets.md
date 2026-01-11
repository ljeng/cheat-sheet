# Feature Sets

You must define a system's boundaries before designing it. Start by asking clarifying questions to understand the environment. For a parking lot, does it have multiple levels? What types of vehicles[^1] are supported? How does **data** enter the system?[^2] Is the service paid or free? Are there different tiers of user accounts?

Functional requirements define **what the system does**. These are the features the user interacts with.

## Example: Tiny URL

- Users can derive a **shortened** alias from a long URL.
- Retrieve the original URL associated with the short link and **redirect** the user.
- Track click rates.
Allow more users to sign up to manage their links.

## Example: Financial Dashboard

- Support advanced filters[^3].
- Store historical records for long-term retrieval.

---

Non-functional requirements define **how the system performs**. These are the *-ilities* that ensure the system is production-ready.

- *Reliability*: The system must be resilient to failures and not lose data.
- *Scalability*: The system should handle growth in data volume without performance degradation.
- *Maintainability*: The architecture should obviate the need for manual intervention when bug fixes are required.
- *Security*: Maintain data integrity through encrypted access.
- *Compliance*: Adhere to industry standards[^4].

Determine the technical infrastructure that will support features once they're defined. Always consider storing **raw data** rather than just processed summaries. We can't predict future analytics needs. Raw data is paramount - it allows us the latitude to re-process information if we add new features later or face compliance audits. Using a standard SQL database yields immediate benefits:

- Alleviate the need for manual engineering by enabling data processing[^5] without custom code.
- Incorporate robust, mature tools for security.[^6]
- SQL is a standard interface, making it **easy** for clients to plug into the data layer.

When adding a feature to the scope, ask:

1. Does this change the **functional** scope[^7]?
1. How does this impact **non-functional** requirements?[^8]
1. Do we have the **raw data** necessary to support this, or do we need to change our ingestion method?

[^1]: compact, large, electric
[^2]: In a banking app, is data pushed or pulled by our service?
[^3]: "Return all stocks with an open price >*N* and a close price <*M*"
[^4]: financial or privacy regulations
[^5]: like the stock price example
[^6]: don't reinvent the wheel
[^7]: what it does
[^8]: Will it slow the system down?
