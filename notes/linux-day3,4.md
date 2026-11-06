
# Linux Day 3 - File Discovery

## 1. Hidden Files

ls -a

- Displays hidden and normal files.
- Linux hidden files start with a dot (.).
- . represents the current directory.
- .. represents the parent directory.

To read a hidden file:

cat ...Hiding-From-You

## 2. Identifying File Types

file ./*

- Identifies the type of files.
- ASCII text means human-readable text.
- Binary data is not normally human-readable.

## 3. Finding Files by Size and Permissions

find . -type f -size 1033c ! -executable

- find . searches the current directory.
- -type f searches regular files only.
- -size 1033c finds files of exactly 1033 bytes.
- ! -executable excludes executable files.

## 4. What I learned

- Finding hidden files using ls -a.
- Reading files using cat.
- Identifying file types using file.
- Finding files using size and permissions.
- Understanding Linux file paths.

---

# Linux Day 4 - Pipes and Text Processing

## 1. find with ownership and size

find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

- Searches the filesystem.
- Filters by owner, group and file size.
- 2>/dev/null hides error messages.

## 2. grep

grep millionth data.txt

- Searches for specific text in a file.
- Displays matching lines.
- Useful for searching keywords in log files.

## 3. sort and uniq

sort data.txt | uniq -u

- sort arranges lines.
- uniq -u displays lines occurring only once.
- uniq works on adjacent lines, so sorting first is important.

## 4. strings

strings data.txt

- Extracts readable text from binary files.
- Useful for finding readable information inside binary data.

## 5. Pipes

command1 | command2

- Passes the output of one command as input to another.
- Helps combine multiple Linux commands.
- Makes command-line work more efficient.

## 6. Base64

base64 -d data.txt

- Decodes Base64-encoded data.
- Base64 is encoding, not encryption.

## 7. Redirection

find / -name "example.txt" 2>/dev/null

- Linux uses 0 for standard input.
- 1 represents standard output.
- 2 represents standard error.
- /dev/null discards unwanted output.

## 8. What I learned

- Searching files across the filesystem.
- Filtering using ownership and size.
- Searching text using grep.
- Removing duplicate lines using sort and uniq.
- Extracting readable strings.
- Using pipes and redirection.
- Decoding Base64.
- Understanding Linux input and output streams.

---

# Bandit Progress

- Level 3 → 4: Hidden files
- Level 4 → 5: Identifying file types
- Level 5 → 6: Finding files by size
- Level 6 → 7: Finding files by ownership
- Level 7 → 8: Searching with grep
- Level 8 → 9: Sorting and unique lines
- Level 9 → 10: Extracting readable strings
- Level 10 → 11: Base64 decoding
