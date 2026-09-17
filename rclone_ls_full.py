#!/usr/bin/env python3

import sys

args=[]

def print_debug(message):
   import sys
   if args.debug_mode:
      print(message, file=sys.stderr)

def size_string(size):
   import humanize
   return humanize.naturalsize(size) if args.human_readable_size else size

def print_file(path, file):
   size_str = size_string(file['Size']) if not file['IsDir'] else ''
   print(f"{path}\t{file['Path']}\t{file['Name']}\t{size_str}\t{file['MimeType']}\t{file['ModTime']}")
   sys.stdout.flush()

def print_dir(path, dir_size, ModTime):
   print(f"{path}\t\t\t{size_string(dir_size)}\tdir\t{ModTime}")
   sys.stdout.flush()
   
def rclone_ls(path, relpath, ModTime=None):
   from rclone.rclone import Rclone
   import locale

   rc = Rclone()

   # rclone 2.x runs the rclone binary without a shell: each flag and its value are separate
   # arguments, and the path must not be quoted.
   print_debug(f"trying '{path}")
   files=rc.lsjson(path, '--log-level', 'ERROR')
   files=sorted(files, key=lambda x: locale.strxfrm(x['Name'].lower()))

   print_debug(files)

   total_size = 0
   for file in files:
      if file['IsDir']:
         total_size += rclone_ls(f"{path}/{file['Name']}", f"{relpath}/{file['Name']}", file['ModTime'])
      else:
         print_file(relpath, file)
         total_size += file['Size']

   if ModTime is None:
      # With --stat, rclone lsjson returns a single object, not a list.
      ModTime=rc.lsjson(path, '--log-level', 'ERROR', '--stat')['ModTime']

   print_dir(relpath, total_size, ModTime)

   return total_size

def main():
   import argparse

   parser = argparse.ArgumentParser(prog='rclone_ls_full')
   parser.description = 'List files/dirs and their sizes in a given rclone path. For instance: rclone_ls_full remote:/path'
   parser.add_argument("rclone_path", help="rclone path")
   parser.add_argument("-H", action="store_true", dest="human_readable_size", help="Use unit suffixes: Byte, Kilobyte, Megabyte...")
   parser.add_argument("--debug", action="store_true", dest="debug_mode", help="Enable debug mode")

   global args
   args = parser.parse_args()

   rclone_ls(args.rclone_path, '')


if __name__ == '__main__':
   main()




# rclone lsjson googledrive:biz
# [
# 2023/06/19 11:30:56 NOTICE: Dangling shortcut "DB4ALL-ROI-Calculations-May5-2009" detected
# 2023/06/19 11:30:56 NOTICE: Dangling shortcut "DB4ALL-SWOT_may27" detected

