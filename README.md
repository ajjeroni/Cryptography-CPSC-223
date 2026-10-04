# Caesar Cipher

A simple Python command-line program for encrypting and decrypting messages with a Caesar cipher, created for cryptography coursework.

## Usage

Requires Python 3. No additional packages are needed.

```bash
python3 caesarcipher.py
```

Choose `1` to encrypt or `2` to decrypt, then enter your message and a nonnegative integer shift. To decrypt, use the same shift that encrypted the message.

- Messages accept English letters and spaces only, with at least one letter.
- Output is lowercase and preserves spaces.
- Shifts wrap around the alphabet (for example, `hello world` with shift `3` becomes `khoor zruog`).

## Files

- `caesarcipher.py` — interactive encryption and decryption program.
- `*.docx` — assignment documents and reflection.
