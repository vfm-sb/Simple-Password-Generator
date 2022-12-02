# Simple Password Generator by VFM | SB

A CLI-Based Simple Password Generator

<br>

## Usage (Version 0.2)

Choose of the two main options: `random` or `manual`.
* `random` generates a 12 character long password.
    * Generated password at least has an uppercase, a lowercase, a symbol and a digit.
* If `manual` keyword is given;
    * Asks the user for:
        * password length,
        * minimum number of uppercase letters,
        * minimum number of lowercase letters,
        * minimum number of special symbols (certain characters removed from the pool for compatibility),
        * minimum number of digits.
* If `readable` command is given addition to `random` or `manual` commands:
    * A dash character (`-`) will be added to original password for better readability.
        * Frequency of dash characters will be determined by the user.

<br>

## Road Map

- Optimizations
- Word or Phrase Based Password Generation


<br>

## License

Distributed under the MIT License. See `LICENSE` file for more information.
