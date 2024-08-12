## Strong Password Checker

A password is considered strong if the below conditions are all met:

 1.It has at least 6 characters and at most 20 characters. 
 2.It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
 3.It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).

Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

 1.Insert one character to password,
 2.Delete one character from password, or
 3.Replace one character of password with another character. 
