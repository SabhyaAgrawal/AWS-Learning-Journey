# Linux Basics Commands

This repository contains the Linux commands I have learned while preparing for AWS Cloud Engineer roles. I am using these commands regularly to improve my Linux skills.

---

## Check Current Directory

```bash
pwd
```

Displays the current working directory.

---

## List Files and Folders

```bash
ls
```

Shows files and folders in the current directory.

```bash
ls -l
```

Shows detailed information.

```bash
ls -la
```

Shows all files, including hidden files.

---

## Change Directory

```bash
cd folder_name
```

Move into a folder.

```bash
cd ..
```

Move back one directory.

```bash
cd ~
```

Go to the home directory.

---

## Create a Directory

```bash
mkdir project
```

Creates a new folder.

```bash
mkdir -p project/src
```

Creates nested folders.

---

## Create a File

```bash
touch notes.txt
```

Creates an empty file.

---

## Copy Files

```bash
cp file.txt backup.txt
```

Copies a file.

```bash
cp -r project backup
```

Copies an entire folder.

---

## Move or Rename Files

```bash
mv old.txt new.txt
```

Renames a file.

```bash
mv file.txt Documents/
```

Moves a file to another folder.

---

## Delete Files and Folders

```bash
rm file.txt
```

Deletes a file.

```bash
rm -r folder_name
```

Deletes a folder and everything inside it.

---

## View File Contents

```bash
cat file.txt
```

Displays the complete file.

```bash
head file.txt
```

Shows the first few lines.

```bash
tail file.txt
```

Shows the last few lines.

---

## Search for Files

```bash
find . -name "*.txt"
```

Finds all text files in the current directory.

---

## Search Inside a File

```bash
grep "Linux" notes.txt
```

Searches for the word "Linux" inside a file.

---

## Check Running Processes

```bash
ps
```

Lists currently running processes.

```bash
top
```

Displays system processes in real time.

---

## Stop a Process

```bash
kill PID
```

Stops a running process.

---

## Check Disk Usage

```bash
df -h
```

Shows available disk space.

```bash
du -sh folder_name
```

Shows the size of a folder.

---

## Check Memory Usage

```bash
free -h
```

Displays RAM usage.

---

## Change File Permissions

```bash
chmod 755 script.sh
```

Changes file permissions.

---

## Change File Ownership

```bash
chown user:user file.txt
```

Changes the owner of a file.

---

## Check Your Username

```bash
whoami
```

Displays the currently logged-in user.

---

## Check IP Address

```bash
ip addr
```

Shows network information and IP address.

---

## Test Internet Connection

```bash
ping google.com
```

Checks whether the system can reach another server.

---

## Update Packages (Ubuntu)

```bash
sudo apt update
```

Updates the package list.

```bash
sudo apt upgrade
```

Installs the latest package updates.

---

## Install Software

```bash
sudo apt install git
```

Installs Git.

---

## Command History

```bash
history
```

Shows previously executed commands.

---

## Clear the Terminal

```bash
clear
```

Clears the terminal screen.

---

# Keyboard Shortcuts

| Shortcut | Purpose |
|----------|---------|
| Ctrl + C | Stop the current command |
| Ctrl + L | Clear the terminal |
| Ctrl + D | Exit the terminal |
| Ctrl + R | Search command history |
| Tab | Auto-complete commands |
| Up Arrow | Previous command |

---

# Sample Workflow

```bash
pwd
ls -la
mkdir linux-practice
cd linux-practice
touch README.md
nano README.md
```

---

## What I Learned

- Navigating the Linux file system
- Managing files and directories
- Viewing and editing files
- Searching files and text
- Managing processes
- Working with permissions
- Monitoring system resources
- Basic networking commands
- Installing software using APT
- Everyday Linux commands used in cloud environments

---

**Learning Goal:** Build a strong foundation in Linux for AWS Cloud Engineering, DevOps, and System Administration.
