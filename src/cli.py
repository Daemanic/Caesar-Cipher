from __future__ import annotations
import argparse
import sys
from pathlib import Path
from compile import decrypt, encrypt
from scoring import frequency_score

def read_text(input_file: str | None, text: str | None) -> str:
    if text is not None:
        return text
    if input_file:
        return Path(input_file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise ValueError("provide --text, --input, or pipe text through stdin")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="caesar-cipher",
        description="encrypt, decrypt, or rank candidates"
    )
    parser.add_argument("mode", choices=("encrypt", "decrypt", "crack"))
    parser.add_argument("--text", help="text to process")
    parser.add_argument("--input", help="read UTF-8 text from a file")
    parser.add_argument("--output", help="write result to a UTF-8 file")
    parser.add_argument("--shift", type=int, help="shift for encrypt/decrypt")
    parser.add_argument("--top", type=int, default=5, help="crack candidates to show")
    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.text is not None and args.input:
        parser.error("use either --text or --input, not both")
    if args.mode in ("encrypt", "decrypt") and args.shift is None:
        parser.error("--shift is required for encrypt and decrypt")
    if args.top < 1:
        parser.error("--top must be at least 1")
    try:
        text = read_text(args.input, args.text)
    except (OSError, UnicodeError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if args.mode == "encrypt":
        result = encrypt(text, args.shift)
    elif args.mode == "decrypt":
        result = decrypt(text, args.shift)
    else:
        candidates = []
        for shift in range(26):
            candidate = decrypt(text, shift)
            candidates.append((frequency_score(candidate), shift, candidate))
        candidates.sort(key=lambda item: item[0])
        result = "\n".join(
            f"shift:{shift:2d} \tscore:{score:.2f} \t{candidate}"
            for score, shift, candidate in candidates[:args.top]
        )
    try:
        if args.output:
            Path(args.output).write_text(result + "\n", encoding="utf-8")
        else:
            print(result)
    except (OSError, UnicodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

