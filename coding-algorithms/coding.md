# Coding

## C++

#### Count the Repetitions

## APIs

## Object-Oriented Design and Programming

## How to Test Your Code

## Corner Cases and Edge Cases

#### String to Integer (atoi)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer. The algorithm for `myAtoi(string s)` is as follows:

1. *Whitespace*: Ignore any leading whitespace (`" "`).
1. *Signedness*: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
1. *Conversion*: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
1. *Rounding*: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

Return the integer as the final result.

```c++
int div = INT_MAX / 10, mod = INT_MAX % 10;

int myAtoi(string s) {
  int i, sign = 1, integer = 0;
  for (i = 0; s[i] == ' '; i++);
  if (s[i] == '-') {
    sign = -1;
    i++;
  }
  else if (s[i] == '+') i++;
  while ('0' <= s[i] && s[i] <= '9') {
    int digit = s[i++] - '0';
    if (integer > div || integer == div && digit > mod)
      return sign == 1 ? INT_MAX : INT_MIN;
    integer = integer * 10 + digit;
  }
  return sign * integer;
}

```

#### Valid Number

Given a string `s`, return whether `s` is a valid number. For example, all the following are valid numbers: `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e7", "-6e-1", "53.5e93", "-123.456e789"]`, while the following are not valid numbers: `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`. Formally, a *valid number* is defined using one of the following definitions:

1. An *integer number* followed by an optional exponent.
1. A *decimal number* followed by an optional exponent.

An *integer number* is defined with an optional sign (`-` or `+`) followed by digits. A *decimal number* is defined with an optional sign (`-` or `+`) followed by one of the following definitions:

1. Digits followed by a dot (`.`).
1. Digits followed by a dot (`.`) followed by digits.
1. A dot (`.`) followed by digits.

An exponent is defined with an exponent notation (`e` or `E`) followed by an integer number. The digits are defined as one or more digits.

```python
def isNumber(s):
    digits, dot, e, exponent = False, False, False, True
    for i, x in enumerate(s):
        if x.isdigit(): digits = exponent = True
        elif x == '.':
            if dot or e: return False
            dot = True
        elif x.lower() == 'e':
            if not digits or e: return False
            e, exponent = True, False
        elif x not in '-+' or i and s[i - 1].lower() != 'e': return False
    return digits and exponent

```
