"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

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

        # Instruction Register: self.reg[1]
        # Memory Address Register: self.reg[2]
        # Memory Data Register: self.reg[3]
        # Flags: self.reg[4]
        # self.reg[5] Reserved: Interrupt Mask
        # self.reg[6] Reserved: Interrupt Status
        # self.reg[7] Reserved: Stack Pointer
        # self.reg[8] Unassigned

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

    def load(self, program):
        """Load a program into memory."""

        print(f"Found {program} -- will run.")

        try:
            address = 0

        except FileNotFoundError:
            print(f"{program} not found")
            sys.exit(2)
        
        if len(sys.argv) != 2:
            print(f"Please format the command like so: \n python3 ls8.py <filename>", file=sys.stderr)
            sys.exit(1)

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
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

        operand_a = self.ram[self.PC + 1]
        operand_b = self.ram[self.PC + 2]

        print(f"Operand A: {operand_a} Operand B: {operand_b}")

        running = True

        while running:
            IR = self.ram[self.PC]
            # print(f"Current IR: {IR}, current PC: {self.PC}")

            if IR == HLT:
                # halt the program
                running = False

            elif IR == LDI:
                # sets register to a value
                self.reg[operand_a] = operand_b
                self.PC += 2

            elif IR == PRN:
                # print the value at a register
                print(self.reg[operand_a])
                self.PC += 1

            else:
                print(f"Unknown command: {IR}")
                sys.exit(1)
            
            self.PC += 1
