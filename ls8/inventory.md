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

<br>

To Do:

* [X] : `__init__()`: Construct a CPU with `self.ram`, `self.pc` and `self.reg` properties

* [X] : Add list properties to CPU to hold 256 bytes of memory and 8 general-purpose registers using pre-set lists. 

`?` After performing math on registers in the emulator, bitwise-AND the result with 0xFF (255) to keep the register values in that range.

- One register called `pc` (Program Counter) for storing the memory address of the currently executing instruction.

- One register called `IR` (Instruction Register) that stores results of the currently executing instruction.

- One register called `MAR` (Memory Address Register) to store the address that is being read or written to

- One register called `MDR` (Memory Data Register) to store the data that was read or to be written

- One register called `FL` (Flags) that holds the current flags status. Flags change based on the `CMP` operands

- `R5`: reserved as the interrupt mask (`IM`)

- `R6`: reserved as the interrupt status (`IS`)

- `R7`: reserved as the stack pointer (`SP`)

- `R8`: Not assigned


<br>

* [X] : Add function called `ram_read()` that accepts the address to read and returns the value stored there.

* [X] : Add function called `ram_write()` that accepts a value to write and the address to write it to. Use MAR and MDR registers.

<br>

* [X] : `run()`: Runs the CPU by reading the memory address that is stored in register `PC`, while storing that result in `IR` (the instruction register).

Then performs the actions needed for each command using an `if-elif` cascade (or other method).

Ultimately updates the `PC` register for the next iteration of the loop.

Bits 6-7 indicate the number of bytes each command will use.

Exit the loop if a `HLT` command is received

<br>

* [X] : `HLT` command: Like `exit()`, this will stop the program from running. Define it within `cpu.py` to reference it by name.

Machine code:
```
00000001 
01
```

<br>

* [X] : `LDI` commnd: Sets a specific register to a specific value

```
10000010 00000rrr iiiiiiii
82 0r ii
```

<br>

* [X] : `PRN` command: Prints the decimal numeric value stored at a given register.

```
01000111 00000rrr
47 0r
```

<br>

* [X] : Test all of the above works by printing `8` to the console with the hard coded program.

<br>
<br>

## DAY II PROJECT

 - [X] : Un-hardcode the program in `cpu.py` and `ls8.py` so the program can be specified in the command line

 Remember to add error handling if the user doesn't input the correct arguments (or number of them)

 * Get sys.argv
 * In `load()`, parse file for commands and addresses
 * Store to RAM by converting address in binary to decimal

 <br>

 - [X] : Test with `print8.ls8`

<br>

- [X] : Now implement a `MUL` function under the `alu()` built in class method that will multiply two values (at different registers), and stores the result in register A.

It expects two address parameters.

<br>

- [X] : Test with `mult.ls8`

<br>

### STRETCH

- [X] : Clean up `run()` with a branch table

<br>
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