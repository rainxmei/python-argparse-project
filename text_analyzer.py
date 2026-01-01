import argparse

parser = argparse.ArgumentParser(
    description="Program untuk membaca dan menganalisis file teks"
)

parser.add_argument("file", help="Nama file input")

parser.add_argument("-l", "--lines", action="store_true", 
                    help="Hitung jumlah baris")
parser.add_argument("-w", "--words", action="store_true",
                    help="Hitung jumlah kata")
parser.add_argument("-c", "--chars", action="store_true",
                    help="Hitung jumlah karakter")
parser.add_argument("-s", "--search", 
                    help="Cari teks tertentu dalam file")

args = parser.parse_args()

try:
    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File '{args.file}' tidak ditemukan!")
    exit(1)

print(f"\nFile: {args.file}")
print("-" * 30)

if args.lines:
    lines = content.count('\n') + 1
    print(f"Jumlah baris: {lines}")

if args.words:
    words = len(content.split())
    print(f"Jumlah kata: {words}")

if args.chars:
    chars = len(content)
    print(f"Jumlah karakter: {chars}")

if args.search:
    count = content.lower().count(args.search.lower())
    print(f"Kata '{args.search}' ditemukan {count} kali")

if not (args.lines or args.words or args.chars or args.search):
    print("Isi file:")
    print("-" * 30)
    print(content[:500] + "..." if len(content) > 500 else content)