#!/usr/bin/env python3
import subprocess
import sys


def main(args):
    new_args = ["python3", "-m", "isort"]
    new_args.extend(args)

    results = subprocess.run(
        new_args,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    if results.stderr:
        sys.stderr.write(results.stderr.decode())
        sys.stderr.flush()

    elif results.stdout:
        sys.stdout.write(results.stdout.decode())
        sys.stdout.flush()

    sys.exit(results.returncode)


if __name__ == "__main__":
    main(sys.argv[1:])
