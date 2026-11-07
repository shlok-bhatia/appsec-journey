
# Linux Day 5 - Encoding, Compression and Networking

## 1. ROT13 Encoding

tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt

- ROT13 replaces each letter with another letter 13 positions ahead.
- tr is used to translate characters.
- Applying ROT13 again decodes the text.

## 2. Hexdump

xxd data.txt

- Displays file contents in hexadecimal format.
- Useful for examining binary data.

xxd -r data.txt > data

- Reverses a hexdump into its original binary file.
- -r means reverse.

## 3. Identifying File Types

file data

- Identifies the actual file format.
- Helps determine which decompression tool to use.

## 4. gzip Compression

gzip -d data.gz

- Decompresses gzip files.
- -d means decompress.

## 5. bzip2 Compression

bzip2 -d data.bz2

- Decompresses bzip2 files.
- -d means decompress.

## 6. tar Archives

tar -xf data.tar

- Extracts files from a tar archive.
- -x means extract.
- -f specifies the archive file.

## 7. SSH Private Key Authentication

ssh -i sshkey.private bandit14@localhost -p 2220

- SSH connects to another machine.
- -i specifies the private key.
- Private keys can authenticate users without passwords.

## 8. Netcat

nc localhost 30000

- nc stands for Netcat.
- Used for network communication.
- Connects to a service using its hostname and port.

## 9. What I learned

- Decoding ROT13 text.
- Reversing hexadecimal dumps.
- Identifying compressed file formats.
- Decompressing gzip and bzip2 files.
- Extracting tar archives.
- Using SSH private keys.
- Connecting to network services using Netcat.
