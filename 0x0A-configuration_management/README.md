# Puppet Configuration Management Tasks

This repository contains Puppet manifests that demonstrate basic configuration management tasks. The project uses Puppet 5.5 on Ubuntu 20.04 LTS.

## Requirements

- Ubuntu 20.04 LTS
- Puppet 5.5
- Puppet-lint 2.1.1

### Task 0: Create a File

Creates a file at `/tmp/school` with the following properties:
- Owner: `www-data`
- Group: `www-data`
- Permissions: `0744`
- Content: `I love Puppet`

**Manifest File**: `0-create_a_file.pp`

### Task 1: Install a Package

Installs `Flask` version 2.1.0 using `pip3`.

**Manifest File**: `1-install_a_package.pp`

### Task 2: Execute a Command

Kills a process named `killmenow` using the `pkill` command.

**Manifest File**: `2-execute_a_command.pp`

## How to Run

1. Ensure Puppet is installed on your system:
   ```bash
   sudo apt-get install -y puppet

