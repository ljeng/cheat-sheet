# Interfaces

**What's the difference between an interface and an abstract class in object-oriented programming?** The implementation details vary by language[^01], but these distinctions should not obscure the conceptual differences that influence software design.

An **interface** declares a set of related methods outside of any class hierarchy. It defines a **contract**[^02] that independent classes can agree to follow. An incomplete class definition, an **abstract class** declares methods without defining them, but it also features fully implemented methods that consolidate a **base** for a family of classes.

| Feature      | Interface                          | Abstract Class                               |
| ---------- | -------------------------------- | ----------------------------------------- |
| **inheritance**        | A class can implement multiple interfaces.     | A class usually inherits from only one abstract class. |
| **implementation**        | contains no method bodies (only signatures)[^03] | contain implemented methods and abstract methods |
| **data members**  | usually can't have instance variables[^04]        | has instance variables[^05] to store state.       |
| **relationship**  | a **can-do** capability[^06]               | an **is-a** relationship[^07]                  |
| **instantiation** | can't be instantiated                  | can't be instantiated                        |

An interface in C++ is simulated by creating a class with no data members and only **pure virtual functions**.

```java
class StatusCallback {
public:
	virtual void updateStatus(int oState, int nState) = 0;
};

class MyClass : public SomeOtherClass, public StatusCallback {
public:
  void updateStatus(int oState, int nState) override {
    if (nState > oState) {
			// Implementation logic
    }
  }
};

```

Java dedicates an interface keyword to delineate the distinction explicitly.

```java
public interface StatusCallback {
  void updateStatus(int oState, int nState);
}

public class MyClass extends SomeOtherClass implements StatusCallback {
  @Override
  public void updateStatus(int oState, int nState) {
    if (nState > oState) {
      // Implementation logic
    }
  }
}

```

A powerful pattern is to **implement** an interface using an abstract class by **default**. This helps reduce boilerplate code for the end dev. The **interface** defines the full contract. **The abstract class** implements one method using the other, leaving only the core logic for the subclass.

```java
public interface XMLReader {
  XMLObject fromString(String str);
  XMLObject fromReader(Reader in);
}

public abstract class XMLReaderImpl implements XMLReader {
  @Override
  public XMLObject fromString(String str) {
    return fromReader(new StringReader(str));
  }

  public abstract XMLObject fromReader(Reader in);
}

```

**Use an abstract class** when you want to share code[^08] among several closely related objects[^09]. **Use an interface** when you want to define a specific behavior that can be implemented by any class, regardless of where it sits in the class hierarchy[^10].

A **class** marked **abstract** can't be instantiated. It's subclassed. All **interfaces are implicitly abstract** in Java; the modifier is optional. An **abstract method** is declared without a body. If a class contains an **abstract method**, the class itself **must** be declared abstract.

[^01]: Java vs. C++
[^02]: an API
[^03]: Java 8+ allows default and static methods in interfaces.
[^04]: only constants
[^05]: fields
[^06]: Runnable
[^07]: Animal
[^08]: field and method implementations
[^09]: **is-a** relationship
[^10]: **can-do** relationship
[^11]: `public abstract void run();`
