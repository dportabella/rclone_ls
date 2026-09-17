# rclone_ls_full

List every file and directory under an rclone path (or a local folder), recursively, with
sizes, MIME types and modification times. Directory sizes are the sum of their contents.

One tab-separated line per entry, so it works with `grep`, `awk` and `sort`:

```
directory <TAB> path <TAB> name <TAB> size <TAB> MIME type <TAB> modification time
```

Directories get a line of their own, after their contents, with an empty path and name, the
total size and `dir` as the type. The last line is the root.

## Example usage

```
$ rclone_ls_full googledrive:/backup
/books	book1.pdf	book1.pdf	2590000	application/pdf	2026-09-17T09:30:00.000000000+02:00
/books			2590000	dir	2026-09-17T09:30:00.000000000+02:00
	notes.md	notes.md	453000	text/markdown; charset=utf-8	2026-09-17T09:30:00.000000000+02:00
			3043000	dir	2026-09-17T09:30:00.000000000+02:00

$ rclone_ls_full -H googledrive:/backup
/books	book1.pdf	book1.pdf	2.6 MB	application/pdf	2026-09-17T09:30:00.000000000+02:00
/books			2.6 MB	dir	2026-09-17T09:30:00.000000000+02:00
	notes.md	notes.md	453.0 kB	text/markdown; charset=utf-8	2026-09-17T09:30:00.000000000+02:00
			3.0 MB	dir	2026-09-17T09:30:00.000000000+02:00

$ rclone_ls_full -h
usage: rclone_ls_full [-h] [-H] [--debug] rclone_path

positional arguments:
  rclone_path  rclone path

options:
  -h, --help   show this help message and exit
  -H           Use unit suffixes: Byte, Kilobyte, Megabyte...
  --debug      Enable debug mode
```

`rclone_path` can also be a local folder, like `/home/david/books`.

## Installation

- Install rclone: https://rclone.org/downloads/
- Configure your rclone remotes: https://rclone.org/commands/rclone_config/
- From this folder: `pip install -e .` (it installs the `rclone_ls_full` command and its
  dependencies, `rclone` 2.x and `humanize`). On David's Mac it is installed in `~/.venv`, and
  `prod/bin/comandes.py` checks that it still is.

The package on PyPI, `rclone_ls` 0.0.2, is the older `rclone_ls` script: this version (0.0.3)
has not been published.


## ChatGPT Python Developer Assistance
I sought assistance from ChatGPT during the the development and publication of this simple Python script, and I must say it was absolutely incredible. I'm sharing a [transcript of our conversation](chatgpt_developer_assistance.md).
