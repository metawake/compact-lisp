# Compact-lisp

CompactLisp is a tiny interpreter of LISP. It supports a few LISP functions 
and the project will eventually have more features. I am thinking of moving
closer to Scheme implementation.

I basically do this as a workout project to grasp both building interpreters
and to understand LISP better.
I am also considering to add some basic async features too.

The implementation is in Python.
The python interpreter accepts a Python list (nested list).
Python nested list is direct equivalent of LISP program.

E.g. consider this program in Scheme

(begin
  (set! custom_var_a 1)
  (set! another_var 2)
  (+ (get custom_var_a) (* (get another_var) 3)))

The interpeter would need the following representation as input
program = [
    "seq",
    ["set", "custom_var_a", 1],
    ["set", "another_var", 2],
    ["add", ["get", "custom_var_a"], ["mul", ["get", "another_var"], 3]],
]


# Supported functions
- seq (a sequence of functions)
- def (a definition of function)
- get (get variable)
- set (set variable)
- call (call a known function)


# TODO
## Functions to be added next
- car, cdr, cons
- map
- reduce