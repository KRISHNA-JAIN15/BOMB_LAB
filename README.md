# Bomb Defusal Game

This Python-based Bomb Defusal Game challenges players to defuse a simulated bomb by completing various phases. Each phase presents a unique task, including retrieving passwords, solving riddles, decoding Morse code, and performing programming challenges in C and Assembly. Successfully completing all phases defuses the bomb, while mistakes or incomplete tasks lead to a simulated explosion.

## Game Phases

### Phase 1: Password Retrieval

- Locate the password in `key.txt`.
- Use Ubuntu commands to find the key.
- Run the bomb lab and enter the correct password.

### Phase 2: Implement `isEven(int x)`

- Complete the `isEven` function in `solution.c`.
- The function should return `1` if `x` is even and `0` if odd.
- Compile with:
  ```
  gcc -o solution solution.c
  ```

### Phase 3: Message Decryption

- Decrypt the Encrypted Message.
- Enter the Decrypted Message

### Phase 4: Morse Code Decoding

- Decode the Morse Code.
- Enter the Decoded Word

### Phase 5: Riddle Solving

- Solve the Assigned Riddles.

### Phase 6: Encrypted Image Mystery

- Find Hidden Messages.
- Reveal the Secret Key

### Phase 7: Find %rax value

- Compile and Run the Assembly Code.
- Find the rax Value
- Check till it becomes a 3 digit number.

# Run the round using ./bomb_lab

## After completion , BOMB will get defused and you will be given a secret key ....

## Make Sure

- To execute commands in the current round, use Ctrl + Z to exit temporarily, find your answers, and then re-run the lab using ./bomb_lab.
- Always keep the terminal in full-screen mode, as some functions require clearing lines, which might affect other lines.

## Instructions to Install all dependencies

```

- sudo apt update
- sudo apt install -y build-essential gdb manpages-dev
- sudo apt install python3 gcc nasm gdb
- sudo apt install figlet toilet
- sudo apt install ruby
- sudo gem install lolcat
- sudo apt install alsa-utils
- python3 -m pip install pillow

Note : Note: if you use Ubuntu, Ubuntu provides a package for Pillow, so you can install it directly using apt: sudo apt install python3-pil

- gcc --version
- gdb --version
- nasm --version

```

## Custom Morse Code

| Character | Morse Code |
| --------- | ---------- |
| A         | #@!        |
| B         | @#!        |
| C         | #@#@       |
| D         | @#@        |
| E         | #@         |
| F         | #@!#       |
| G         | @@#!       |
| H         | ####@      |
| I         | @##        |
| J         | #@!!       |
| K         | @#@!       |
| L         | #@#!#      |
| M         | @@@        |
| N         | #@#        |
| O         | @@#!       |
| P         | #@!#@      |
| Q         | @@#@#      |
| R         | #@#!       |
| S         | ###@!      |
| T         | @@         |
| U         | ##@!       |
| V         | ###@#      |
| W         | #@!@       |
| X         | @#!@#      |
| Y         | @#@!!      |
| Z         | @@@#!      |
| 0         | @#@@#      |
| 1         | #@!@#      |
| 2         | ##@#!      |
| 3         | ###@#      |
| 4         | @@#@!      |
| 5         | #####      |
| 6         | @#@#!      |
| 7         | @@@#!      |
| 8         | #@##!      |
| 9         | #@#!@      |

This guide provides instructions for using various Linux commands, including file navigation, text editing, C program compilation, and decoding hidden messages in images.

## Table of Contents

1. Displaying File Contents and Navigating Directories
2. Compiling C Code
3. Decoding Hidden Messages in Images
4. Assembly Phase

### Find Secret Key

```
- Display the contents of a file
    cat filename.txt

- Change to a specific directory
    cd /path/to/directory

- Move up one directory
    cd ..
```

### Compile C Code

```
- Open a File
   nano filename.c
- Common Commands:

   Save changes: Ctrl + O (then press Enter to confirm)
   Exit nano: Ctrl + X
   Cut text: Ctrl + K
   Paste text: Ctrl + U
   Search for text: Ctrl + W

gcc -o solution solution.c
chmod +x solution  # Make it executable
```

### Decode Image

```
exiftool image.png

nano encoded_message.txt
//Write Hidden message in file
base64 -d encoded_message.txt > hidden_message.txt
cat hidden_message.txt

```

### Assembly Code

```

nasm -f elf64 -o asm_phase.o asm_phase.asm
ld -o asm_phase asm_phase.o  # Link the object file
chmod +x asm_phase            # Make it executable

gdb ./asm_phase
(gdb) break _start
(gdb) run
(gdb) disassemble _start
(gdb) info registers
(gdb) stepi // use stepi 2 times

```
