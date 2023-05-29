# rclone_ls

List files/dirs and their sizes in a given rclone path.

## Example usage
```
$ ./rclone_ls remote:/path
8196	.DS_Store
1747191312	books/
1503049236	downloads/
930638960	temp/
total:	8225934615

$ ./rclone_ls -H remote:/path
8.2 kB	.DS_Store
1.7 GB	books/
1.5 GB	downloads/
930.6 MB	temp/
total:	2.7 GB

$ ./rclone_ls -h
usage: rclone_ls [-h] [-H] [--debug] rclone_path

List files/dirs and their sizes in a given rclone path. For instance: rclone_ls remote:/path

positional arguments:
  rclone_path  rclone path

options:
  -h, --help   show this help message and exit
  -H           Use unit suffixes: Byte, Kilobyte, Megabyte...
  --debug      Enable debug mode
```

## Note
- The `total` is printed in stderr. 
  You can avoid printing by adding this to the command line: `2>/dev/null`.
- `rclone_path` can be a local folder, such as `/home/david/books`.


## Installation
- Manually install rclone: https://rclone.org/downloads/
- Configure your rclone remotes: https://rclone.org/commands/rclone_config/
- `$ pip install rclone_ls`
