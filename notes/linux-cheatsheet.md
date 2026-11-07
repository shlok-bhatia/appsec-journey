
# Linux Command Cheatsheet

## File and Directory Management

pwd
ls
ls -la
cd
mkdir
cp
mv
rm
cat
nano

## Finding Files

find . -type f
find . -size 1033c
find . -user username
find . -perm 644

## Permissions

ls -l
chmod 755 filename
chmod 600 filename
chown user filename

## Text Processing

grep "word" file.txt
sort file.txt
uniq -u
uniq -c
strings file
tr 'A-Z' 'a-z'

## Pipes and Redirection

command1 | command2
command > output.txt
command >> output.txt
command 2>/dev/null

## Compression and Encoding

file filename
xxd filename
xxd -r input > output
gzip -d file.gz
bzip2 -d file.bz2
tar -xf file.tar
base64 -d file.txt

## Networking

ip addr
ping
ss -tuln
nc localhost 30000

## SSH

ssh username@hostname -p 2220
ssh -i private_key username@hostname -p 2220

## Git

git status
git add .
git commit -m "message"
git log --oneline
git push
