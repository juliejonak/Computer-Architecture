"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Each index is a byte
        # RAM stores 256 bytes
        self.ram = [0] * 256

        # Each index in reg is a register
        self.reg = [0] * 8

        # Store the Program Counter
        self.PC = self.reg[0]

        # Store operation handling
        self.commands = {
            0b00000001: self.hlt,
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b10100010: self.mul
        }

    def __repr__(self):
        return f"RAM: {self.ram} \n Register: {self.reg}"

    def ram_read(self, address):
        # Typically MAR stores the address of what to read and MDR stores the data to read
        # return self.MDR
        return self.ram[address]

    def ram_write(self, value, address):
        # MAR stores the address of where to write and MDR stores the value to write
        # self.ram[self.MAR] = self.MDR
        self.ram[address] = value

    def hlt(self, operand_a, operand_b):
        return (0, False)

    def ldi(self, operand_a, operand_b):
        # Sets register to value
        self.reg[operand_a] = operand_b
        return (3, True)

    def prn(self, operand_a, operand_b):
        # print the value at a register
        print(self.reg[operand_a])
        return (2, True)
    
    def mul(self, operand_a, operand_b):
        # Multiply two values and store in first register
        self.alu("MUL", operand_a, operand_b)
        return (3, True)

    def load(self, program):
        """Load a program into memory."""
        try:
            address = 0

            with open(program) as f:
                for line in f:
                    comment_split = line.split("#")

                    number = comment_split[0].strip()

                    if number == "":
                        continue
                    
                    value = int(number, 2)

                    self.ram_write(value, address)

                    address += 1

        except FileNotFoundError:
            print(f"{program} not found")
            sys.exit(2)
        
        if len(sys.argv) != 2:
            print(f"Please format the command like so: \n python3 ls8.py <filename>", file=sys.stderr)
            sys.exit(1)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]

        elif op == "MUL":
            self.reg[reg_a] = (self.reg[reg_a]) * (self.reg[reg_b])
            return 2

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            #self.fl,
            #self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            IR = self.ram[self.PC]

            operand_a = self.ram_read(self.PC + 1)
            operand_b = self.ram_read(self.PC + 2)

            try:
                operation_output = self.commands[IR](operand_a, operand_b)

                running = operation_output[1]
                self.PC += operation_output[0]

            except:
                print(f"Unknown command: {IR}")
                sys.exit(1)

