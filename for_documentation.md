# For(IS,VERY,WEIRD

## Introduction
The For( command is weird. Some bits and pieces of its strangeness have been known [since the release of the CSE](http://tibasicdev.wikidot.com/for), but the first known partially-replete elaboration was done on the Cemetech Discord in August 2021 by yours truly while working on extensions to [`For(T,R,A,N`](https://www.cemetech.net/forum/viewtopic.php?t=16666&highlight=). The original Discord conversation is littered with unrelated moderation issues, and so will not be linked or transcribed here; instead, I summarize the details in a more readable format, along with additional discoveries made since then.

In short, `For(` is evil. It does things it should not do. It does things it has no right to do. It can evaluate lists. It can run solve(. It can set your clock. It can run until the end of time. The title of this document is valid syntax. `For(` is terrifying, and we may only hope to wrestle its horrors by endeavoring to understand it.

Note that this document is a purely descriptive account of `For(`, as we have yet to delve into the disassembly to pick out all of what’s going on (beyond a few one-off peeks when this was first discovered). Although, if `For(` is this despicable, one can only cower at TI’s code for it.

## Syntax Description
### Grammar
All `For(` commands are of the following form:

`For( first rest? , start , end , step paren? body? loop_end?`

### Parameters

#### `first`
The `first` parameter is a component of the first argument to `For(`.

* If `first` begins with a real var, finance var, list token, or matrix token, then first is taken to be that sole token.
* If `first` begins with `|L`, then `first` is taken to be a list name, parsed greedily; recall that list names are alphanumeric, cannot begin with a digit, and contain no more than 5 tokens.
* If `first` begins with a GDB token, `ERR: DATA TYPE` is raised.
* If `first` begins with a token which points to an archived var, `ERR: ARCHIVE` is raised.
* If `first` begins with any other token, `ERR: SYNTAX` is raised.

#### `rest`
The `rest` parameter is the entire remainder of the first argument to `For(` following `first`. For most purposes, the evaluation of `first rest` (i.e. the entire first argument to `For(`) dictates macroscopic loop behavior.

#### `start`
The `start` parameter is an expression which is evaluated to determine the second argument to `For(`. It must evaluate to a real number before `body` is executed.

#### `end`
The `end` parameter is an expression which is evaluated to determine the third argument to `For(`. It must evaluate to a real number before body is executed.

#### `step`
The `step` parameter is an expression which is evaluated to determine the fourth argument to `For(`, and has a default value of 1. It must evaluate to a real number before body is executed.

#### `paren`
The `paren` parameter is a single closing parenthesis, which may or may not exist. Its existence has strange consequences on the speed of the execution of the body of the `For(` loop.

#### `body`
The `body` parameter is a block of code which is executed in some capacity during the loop. Whether and how many times it is executed depends on the value of `first`, `rest`, `start`, `end`, `step`, and the existence of `loop_end`.

#### `loop_end`
The `loop_end` parameter is a single `End` statement which closes the body of the `For(` loop, and may or may not exist. The loop may only execute multiple times if `loop_end` exists, but the converse is not true. If `loop_end` does not exist but is nonetheless explicitly referred to, then it is taken to be the end of the program.

## Behavior

Any errors which might occur in the outlined steps for reasons not necessarily inherent to the behavior of `For(` in its own right are not explicitly stated. Unsurprisingly, such errors terminate all execution.

### Case 1: `first rest` is a real number

#### Case 1a: `rest` is empty

1. The expressions `start`, `end`, and `step` are evaluated
2. The var pointed to by `first` is updated to the value of `start`
3. How does start `compare` to `end`?
    * If `start` > `end` and `step` is positive, execution skips to the line after `loop_end`
    * If `start` < `end` and `step` is negative, execution skips to the line after `loop_end`
4. The first line in `body` is executed
    * If `paren` does not exist and the line is a conditional statement (`IS>(`, `DS<(`, or single-line `If`) which evaluates to false, execution will be monstrously slower
5. The remaining lines of `body` are executed
6. Does `loop_end` exist?
    * If `loop_end` exists, `first` is incremented by `step` and execution returns to Step 3
    * If `loop_end` does not exist, execution terminates

#### Case 1b: `rest` is non-empty

1. The expression `first rest` is evaluated
2. The expressions `start`, `end`, and `step` are evaluated
3. How does `start` compare to `end`?
    * If `start` > `end` and `step` is positive, execution skips to the line after `loop_end`
    * If `start` < `end` and `step` is negative, execution skips to the line after `loop_end`
4. Were any variables manipulated prior to the loop?
    * If so, the space taken up by the last non-program variable in the VAT is leaked
5. The first line in `body` is executed
    * If `paren` does not exist and the line is a conditional statement (`IS>(`, `DS<(`, or single-line `If`) which evaluates to false, execution will be monstrously slower
6. The remaining lines of body are executed
7. Does `loop_end` exist?
    * If `loop_end` exists, raise `ERR:UNDEFINED`
    * If `loop_end` does not exist, execution terminates

### Case 2: `first rest` is a list or matrix

1. Is `rest` empty?
    * If so, raise `ERR: DATA TYPE`
2. The expression `first rest` is evaluated
3. The expressions `start`, `end`, and `step` are evaluated
4. An invisible counter `invis` is set to the value of `start`
5. How does `start` compare to `end`?
    * If `start` > `end` and `step` is positive, execution skips to the line after `loop_end`
    * If `start` < `end` and `step` is negative, execution skips to the line after `loop_end`
6. The first line in `body` is executed
    * If `paren` does not exist and the line is a conditional statement (`IS>(`, `DS<(`, or single-line `If`) which evaluates to false, execution will be monstrously slower
7. Does `loop_end` exist?
    * If `loop_end` exists, `invis` is incremented by `step` and execution returns to Step 5
    * If `loop_end` does not exist, execution terminates

### Case 3: first rest is a string

1. Is `first` a string literal?
    * If so, raise `ERR: SYNTAX`
2. Is `rest` empty?
    * If so, raise `ERR: DATA TYPE`
3. The expression `first rest` is evaluated
4. The expressions `start`, `end`, and `step` are evaluated
5. An invisible counter `invis` is set to the value of start
6. How does `start` compare to `end`?
    * If `start` > `end` and `step` is positive, execution skips to the line after `loop_end`
    * If `start` < `end` and `step` is negative, execution skips to the line after `loop_end`
7. The first line in `body` is executed
    * If `paren` does not exist and the line is a conditional statement (`IS>(`, `DS<(`, or single-line `If`) which evaluates to false, execution will be monstrously slower
8. Does `loop_end` exist?
    * If `loop_end` exists, `invis` is incremented by step and execution returns to Step 6
    * If `loop_end` does not exist, execution terminates


## Miscellaneous Findings and Tidbits
* The expression `first rest` is evaluated with side-effects. For example:
    * `For(Asolve(X-1,X,0),0,1` will set X to 1
    * `For(AsetTime(11,0,0),0,1` will set the time to 11:00 AM
* The VAT leak described in Case 1b is dubbed the “invisible reals” bug. TI has been aware of this bug for (presumably) some time; see the discussion [here](https://www.cemetech.net/forum/viewtopic.php?t=18933).

