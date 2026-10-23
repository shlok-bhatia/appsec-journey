# Day 2 — Linux Fundamentals & Bandit

## 1. Objective
- Practise Linux terminal commands.
- Learn SSH authentication.
- Understand how to read files with unusual filenames.
- Practise basic Linux navigation.

## 2. Commands Learned

### `ssh` — Secure Shell
Connects to a remote machine securely.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

- `bandit0`: username
- `-p 2220`: specifies the SSH port.

### `ls` — List Files
Displays files and directories in the current directory.

```bash
ls
```

### `cat` — Read File Contents
Displays the file content.

```bash
cat readme
```

### `pwd` — Present Working Directory
Shows the current directory path.

```bash
pwd
```

### `cd` — Change Directory
Moves to another directory.

```bash
cd /tmp
```

### `exit` — Exit a Session
Closes the current shell or SSH session.

```bash
exit
```

## 3. What I Learned from Bandit

### Level 0 → Level 1
- Connected to the Bandit server using SSH.
- Used `ls` to locate the `readme` file.
- Used `cat readme` to read the password for the next level.

### Level 1 → Level 2
- Practised reading a file named `-`.
- Learned that a filename beginning with a hyphen can be mistaken for a command option.
- Used `cat ./-` to specify a file in the current directory.

### Level 2 → Level 3
- Encountered a filename containing spaces and leading/trailing hyphens.
- Learned that spaces must be handled correctly by the shell.
- Used `--` to mark the end of command options.

Example:

```bash
cat -- "--spaces in this filename--"
```

## 4. Important Concepts

- **SSH:** Secure remote login.
- **Relative path:** A path interpreted from the current directory.
- **Quoting:** Keeps spaces within a filename together.
- **Option terminator (`--`):** Tells many commands that subsequent arguments are not options.
- **Authentication:** The process of verifying a user's identity.

## 5. Problems Faced and Solutions

### Problem 1: Reading a filename starting with `-`
**Reason:** The command interpreted the filename as an option.

**Solution:**
```bash
cat ./-
```

### Problem 2: Reading a filename with spaces and hyphens
**Reason:** The filename was not passed correctly to the command.

**Solution:**
```bash
cat -- "--spaces in this filename--"
```

## 6. Security Notes
- Never publish discovered passwords or access tokens in a public repository.
- Practise only on authorised training environments.
- Use separate private notes for credentials and public notes for explanations.

## 7. Next Session
- Continue Bandit levels 3–5.
- Practise `find`, `file`, and `grep`.
- Document the commands, mistakes, and solutions.

