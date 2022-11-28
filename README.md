# Mautic multisend

This is simple python script with no external dependencies that handles multiThreaded mautic email sending


## Install

Copy `multisend` and `multisend.conf` to your server

## Configuration

Configuration is stored in `multisend.conf`: 

```ini
[LOGGING]
# Log level it can be info|debug|warning|error
LEVEL = info
#FILE = debug.log  # Enable to log in file

[EMAIL]
# Number of trheads you wish to run
THREADS = 5
# Where multitrheaded spools will be stored
SPOOLS_PATH = ./multi-spools
# Where is source spool (usually var/spool in mautic dir)
SOURCE_SPOOL = ./spool
# Naming format of multitrheaded spool folders
SPOOL_FOLDER_FORMAT = spool_{}
# Path to mautic console (usually bin/console in mautic dir)
MAUTIC_CONSOLE_PATH = ./mautic/bin/console
#MAUTIC_CONSOLE_PATH = ./fake_console
```

## Test Running

For test you should run multisend script manually:

```bash
chmod +x multisend
./multisend
```

# Production Running

For production running you should use systemd service `mautic-multisend.service`