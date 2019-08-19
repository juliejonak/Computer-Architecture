# Inventory of LS-8

[inventory.md](inventory.md): lists all files within `ls8` with a short description and to do list

<br>

[README.md](README.md): A ReadMe tutorial of how to work through the LS-8 project

<br>

[cpu.py](cpu.py): Provides the CPU functionality of LS-8. 

Completed:

* `load()`: Loads a program into memory, with a currently hard coded program.

* `alu()`: Handles ALU operations, with commented out _elif_ capabilities to handle not-yet-written commands

* `trace()`: Prints the CPU state for debugging

To Do:

* `__init__()`: Construct a CPU with `self.ram`, `self.pc` and `self.reg` properties, and a function called `ram_read()`

* `run()`: Runs the CPU

<br>
<br>

There is also an `examples` directory that contains multiple `ls8` files for reference:

[call.ls8](call.ls8): Provides an example that should result in an output of:

```
20
30
36
60
```

<br>

[interrupts.ls8](interrupts.ls8): An example file that tests if the timer interrupt stretch goal is properly implemented. Should fire once per second.

<br>

[keyboard.ls8](keyboard.ls8): An example file possibly used to test the keyboard interrupt stretch goal.

> Purpose: TBD?

<br>

[mult.ls8](mult.ls8): An example file that tests if the CPU has been un-hard coded and a program can be specified from the command line.

<br>

[print8.ls8](print8.ls8): An example file that can also test if the CPU has been un-hard coded or to test the print command.

<br>

[printstr.ls8](printstr.ls8): An example file that appears to test how the LS=8 prints, containing LDI, CALL, HLT, JEW, PRA, INC, DEC and RET commands.

Appears to contain Print string tests and a print loop test.

> Purpose: TBD?

<br>

[sctest.ls8](sctest.ls8): An example file that contains 5 tests, with LDI, CMP, JEQ and PRN commands.

> Purpose: TBD?

<br>

[stack.ls8](stack.ls8): An example file that can help test if the system stack implementation works properly, which should output:

```
2
4
1
```

<br>

[stackoverflow.ls8](stackoverflow.ls8): An example file that contains LDI commands, plus a loop with PRN, ADD, PUSH and JMP commands.

> Purpose: TBD?

<br>