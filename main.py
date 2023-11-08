import argparse
import sys
from typing import Optional
from typing import Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
  # Take CLI arguments and use arg parser
  parser = argparse.ArgumentParser()
  parser.add_argument('person')
  args = parser.parse_args(argv)

  # Purposely bad error for testing
  if args.person == '':
    print("Person's name must not be empty!", file=sys.stderr)
    return 1
  
  print(f'Hello, {args.person}')
  return 0

if __name__ == '__main__':
  exit(main())