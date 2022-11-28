# Mautic multisend

This is simple python script with no external dependencies that handles multiThreaded mautic email sending


## Install

Copy `multisend` and `multisend.conf` to your server

## Configuration

Configuration is stored in `multisend.conf`: 

```ini
[LOGGING]
LEVEL = info   # Log level it can be info|debug|warning|error
#FILE = debug.log  # Enable to log in file

[EMAIL]
THREADS = 5   # Number of trheads you wish to run
SPOOLS_PATH = ./multi-spools  # Where multitrheaded spools will be stored
SOURCE_SPOOL = ./spool  # Where is source spool (usually var/spool in mautic dir)
SPOOL_FOLDER_FORMAT = spool_{}  # Naming format of multitrheaded spool folders
MAUTIC_CONSOLE_PATH = ./mautic/bin/console  # Path to mautic console (usually bin/console in mautic dir)
```

## Test Running

For test you should run multisend script manually:

```bash
chmod +x multisend
./multisend
```

# Production Running

For production running you should use systemd service `mautic-multisend.service`