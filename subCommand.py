import argparse

parser = argparse.ArgumentParser(description="Manajer File")
subparsers = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

parser_create = subparsers.add_parser("create", help="Buat file baru")
parser_create.add_argument("filename", help="Nama file")
parser_create.add_argument("-c", "--content", help="Isi file")

parser_delete = subparsers.add_parser("delete", help="Hapus file")
parser_delete.add_argument("filename", help="Nama file")
parser_delete.add_argument("-f", "--force", action="store_true", help="Hapus paksa")

parser_list = subparsers.add_parser("list", help="List file")
parser_list.add_argument("-d", "--directory", default=".", help="Direktori")

args = parser.parse_args()

print(f"Command: {args.command}")
print(f"Args: {args}")

if args.command == "create":
    print(f"Membuat file: {args.filename}")
    if args.content:
        print(f"Dengan isi: {args.content}")
        
elif args.command == "delete":
    print(f"Menghapus file: {args.filename}")
    if args.force:
        print("Mode force aktif!")
        
elif args.command == "list":
    print(f"List file di: {args.directory}")
    
else:
    parser.print_help()