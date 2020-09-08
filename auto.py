#! /usr/local/bin/python3

import os
import sys
import yaml

from utils import read


def create_folder(path, name, format, indent):
  name = format.get('name', name)

  os.mkdir(f'{path}/{name}')

  print(f'{indent} * {name} (✅)')
  
  return name

def create_file(path, name, format, indent):
  name = format.get('name', name)
  prefix = format.get('prefix', '.')
  ext = format.get('ext', '')

  os.system(f'touch {path}/{name}{prefix}{ext}')

  print(f'{indent} {name}{prefix}{ext} (✅)')



def main(name, path, structure, indent=""):
  print()
  for format in structure:
    if 'dir' in format:
      dir_created = create_folder(path, name, format, indent)

      if 'contents' in format:
        main(name,  f'{path}/{dir_created}', format['contents'], f'| {"-" * 2}')
    
    if 'file' in format:
      create_file(path, name, format, indent)


if __name__ == '__main__':
  _, name, path, scheme = sys.argv

  main(
    name,
    os.path.abspath(path),
    read(os.path.abspath(scheme))
  )