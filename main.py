#!/usr/bin/env python
import argparse

VERSION="v0.0.1"

def main():
  parser = argparse.ArgumentParser(description='A simple "Hello, world!" application')
  parser.add_argument("-v", "--version", action="version", version=VERSION)
  args = parser.parse_args()

  print("Hello, world!")

if __name__ == "__main__":
  main()
