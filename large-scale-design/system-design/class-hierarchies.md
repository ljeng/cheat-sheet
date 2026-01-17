# Class Hierarchies

Object orientation revolves around **classes** and **objects**. A **class** is an abstract definition or something that has **attributes**[^1] and **actions**[^2]. An **object** is a specific instance of a class that has its own state separate from any other object instance.

```mermaid
classDiagram
    class Point {
        -int x
        -int y
        +Point(int x, int y)
        +int getX()
        +int getY()
        +void setX(int x)
        +void setY(int y)
        +double distanceTo(Point other)
        +String toString()
    }

```

This example shows **encapsulation** - the hiding of implementation details[^3].

`Point.java`

```java
public class Point {
  private int x, y;

  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  public Point(Point other) {
    this.x = other.getX();
    this.y = other.getY();
  }

  public int getX() {
    return x;
  }

  public int getY() {
    return y;
  }

  public Point relativeTo(int dx, int dy) {
    return new Point(x + dx, y + dy);
  }

  @Override
  public String toString() {
    return String.format("(%d, %d)", x, y);
  }

  public static void main(String[] args) {
    Point p1 = new Point(5, 10);
    Point p2 = p1.relativeTo(-5, 5);
    System.out.println(p2.toString()); // (0, 15)
  }
}

```

Inheritance allows a class to be defined as a modified or more specialized version of another. When class B inherits from class A, class A is B’s base class, and class B is A’s subclass. At the top of the hierarchy is the Shape class. The Ellipse classes could be further specialized into the Circle subclass. Polymorphism is the capability to provide multiple implementations of an action and to select the correct implementation based on the surrounding context. All the behaviors defined by class A are also part of class B in a modified form.

```mermaid
classDiagram
    class A {
        +method()
    }
    class B {
        +methodOverride()
    }
    A <|-- B

```

`Shape.java`

```java
import java.awt.Graphics;

public abstract class Shape {
  protected Point center;

  protected Shape(Point center) {
    this.center = center;
  }

  public Point getCenter() {
    return center;
  }

  public abstract Rectangle getBounds();
  public abstract void draw(Graphics g);
}

```

`Rectangle.java`

```java
class Rectangle extends Shape {
  private int w, h;

  public Rectangle(Point center, int w, int h) {
    super(center);
    this.w = w;
    this.h = h;
  }

  public Rectangle getBounds() {
    return this;
  }

  public void draw(Graphics g) {}
}

```

`Ellipse.java`

```java
class Ellipse extends Shape {
  private int a, b;

  public Ellipse(Point center, int a, int b) {
    super(center);
    this.a = a;
    this.b = b;
  }

  public Rectangle getBounds() {
    return new Rectangle(center, a * 2, b * 2);
  }

  public void draw(Graphics g) {}
}

```

Even though many shapes may be defined, the part of the app that draws them doesn’t need to do much work:

```java
void paintShapes(Graphics g, List<Shape> shapes) {
  for (Shape s : shapes) s.draw(g);
}

```
 
```mermaid
classDiagram
    class Card {
        -Suit suit
        -Rank rank
        +getSuit() Suit
        +getRank() Rank
        +toString() String
    }
    
    class Deck {
        -List~Card~ cards
        +shuffle() void
        +deal() Card
        +reset() void
        +getSize() int
    }
    
    class Suit {
        <<enumeration>>
        HEARTS
        DIAMONDS
        CLUBS
        SPADES
        +getSymbol() String
        +getColor() String
    }
    
    class Rank {
        <<enumeration>>
        ACE
        TWO
        THREE
        FOUR
        FIVE
        SIX
        SEVEN
        EIGHT
        NINE
        TEN
        JACK
        QUEEN
        KING
        +getValue() int
        +getDisplayName() String
    }
    
    Card "*" --o "1" Deck : contains
    Card --> "1" Suit : has
    Card --> "1" Rank : has

```

Think about the logic. How does a Deck shuffle? How does a Hand calculate its score?

## The Parking Lot

Track available spots, handle different vehicle types[^4], and manage specialized spots[^5].

| Objects   |
| ------- |
| ParkingLot |
| Level    |
| ParkingSpot |
| Vehicle   |

---

Use these prompts to practice your OOD skills:

1. Design the data structures for a **generic deck of cards** for particular card games.
1. Implement a `getCallHandler()`.

```mermaid
graph TD
    A[Incoming Call] --> B{Call Distribution System}
    
    B --> C1[Fresher 1]
    B --> C2[Fresher 2]
    B --> C3[Fresher 3]
    B --> C4[Fresher 4]
    
    C1 -.Escalate.-> D1[Team Leader 1]
    C2 -.Escalate.-> D1
    C3 -.Escalate.-> D2[Team Leader 2]
    C4 -.Escalate.-> D2
    
    D1 -.Complex Issues.-> E[Project Manager]
    D2 -.Complex Issues.-> E
    
    C1 --> F1[Resolve & Close]
    C2 --> F2[Resolve & Close]
    C3 --> F3[Resolve & Close]
    C4 --> F4[Resolve & Close]
    
    D1 --> G1[Resolve & Close]
    D2 --> G2[Resolve & Close]
    
    E --> H[Strategic Resolution & Close]
    
    style C1 fill:#a8d5ba
    style C2 fill:#a8d5ba
    style C3 fill:#a8d5ba
    style C4 fill:#a8d5ba
    style D1 fill:#f9d77e
    style D2 fill:#f9d77e
    style E fill:#ff9999
    style A fill:#e0e0e0

```

1. Design a musical jukebox using object-oriented principles.
1. Design a chess game using object-oriented principles.
1. **Online book reader**

```mermaid
erDiagram
    USER ||--o{ LIBRARY : "has"
    USER ||--o{ READING_SESSION : "creates"
    USER ||--o{ BOOKMARK : "creates"
    USER ||--o{ ANNOTATION : "makes"
    USER ||--o{ REVIEW : "writes"
    USER {
        string userId PK
        string email
        string username
        string passwordHash
        datetime createdAt
        datetime lastLogin
        string subscriptionType
    }
    BOOK ||--o{ LIBRARY : "contains"
    BOOK ||--o{ READING_SESSION : "tracks"
    BOOK ||--o{ BOOKMARK : "has"
    BOOK ||--o{ ANNOTATION : "contains"
    BOOK ||--o{ REVIEW : "receives"
    BOOK ||--|{ CHAPTER : "divided into"
    BOOK }o--|| PUBLISHER : "published by"
    BOOK }o--o{ AUTHOR : "written by"
    BOOK }o--o{ GENRE : "categorized as"
    BOOK {
        string bookId PK
        string isbn
        string title
        string description
        string coverImageUrl
        int totalPages
        datetime publishDate
        string language
        float rating
        int reviewCount
    }
    AUTHOR {
        string authorId PK
        string name
        string biography
        string photoUrl
        datetime birthDate
    }
    PUBLISHER {
        string publisherId PK
        string name
        string country
        string website
    }
    GENRE {
        string genreId PK
        string name
        string description
    }
    CHAPTER {
        string chapterId PK
        string bookId FK
        int chapterNumber
        string title
        string content
        int pageStart
        int pageEnd
    }
    LIBRARY {
        string libraryId PK
        string userId FK
        string bookId FK
        datetime addedAt
        string status
        int currentPage
        float progress
    }
    READING_SESSION {
        string sessionId PK
        string userId FK
        string bookId FK
        datetime startTime
        datetime endTime
        int startPage
        int endPage
        int durationMinutes
    }
    BOOKMARK {
        string bookmarkId PK
        string userId FK
        string bookId FK
        int pageNumber
        string chapterId FK
        string note
        datetime createdAt
    }
    ANNOTATION {
        string annotationId PK
        string userId FK
        string bookId FK
        string chapterId FK
        int pageNumber
        string selectedText
        string note
        string highlightColor
        datetime createdAt
        datetime updatedAt
    }
    REVIEW {
        string reviewId PK
        string userId FK
        string bookId FK
        int rating
        string reviewText
        datetime createdAt
        int helpfulCount
    }

```

1. Design the data structures to solve a jigsaw puzzle.
1. Design a chat server. Provide details about the backend components.
1. Implement the OOD for the game Othello.
1. Design the data structures for a file system. Illustrate with code examples.
1. Describe the data structures to implement a garbage collector in C++.

[^1]: properties/state
[^2]: methods/capabilities
[^3]: private fields
[^4]: Car, Bus, Motorcycle
[^5]: Handicapped
[^6]: Directories, Files
