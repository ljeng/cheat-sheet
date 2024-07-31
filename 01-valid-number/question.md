# Valid Number Checker

This script checks whether a given string `s` is a valid number. A valid number can be either an integer number or a decimal number, optionally followed by an exponent.

## Formal Definition of a Valid Number

1. **Integer Number**: Defined with an optional sign '-' or '+' followed by digits.

2. **Decimal Number**: Defined with an optional sign '-' or '+' followed by one of the following:
   - Digits followed by a dot `.`.
   - Digits followed by a dot `.` followed by digits.
   - A dot `.` followed by digits.

3. **Exponent**: Defined with an exponent notation 'e' or 'E' followed by an integer number.

**Note**: The digits are defined as one or more digits.

## Examples of Valid Numbers
- `"2"`
- `"0089"`
- `"-0.1"`
- `"+3.14"`
- `"4."`
- `"-.9"`
- `"2e10"`
- `"-90E3"`
- `"3e+7"`
- `"+6e-1"`
- `"53.5e93"`
- `"-123.456e789"`

## Examples of Invalid Numbers
- `"abc"`
- `"1a"`
- `"1e"`
- `"e3"`
- `"99e2.5"`
- `"--6"`
- `"-+3"`
- `"95a54e53"`