# fast-string
Convert strings to little endian hexadecimal representation for fast, compiler-friendly comparisons in native languages (this was written to help with the development of a C99 program).

Currently hand limited to 512 bytes because it doesn't really make any sense to generate a constant bigger than what can fit in an avx512 register, but the code allows for arbitrarily long strings to be converted, just remove the statement.

## Some examples
``Hello`` turns into ``6f6c6c6548``
``Little-endian`` turns into ``6e6169646e652d656c7474694c``

If you need it to consider the null terminator too, just add a 00 in front of the number :).
