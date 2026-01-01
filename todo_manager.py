import argparse
import sys
import os
import json

todo_file = "todo.json"

todo = []
add_id = 1

def load_file():
    global todo, add_id

    if os.path.exists(todo_file):
        try:
            with open(todo_file, 'r') as f:
                data = json.load(f)
                todo = data.get("todo", [])
                add_id = data.get("add_id", 1)
        except Exception as e:  
            print(f"Error loading data: {e}")
            todo = []
            add_id = 1
    else:
        print(f"file {todo_file} tidak ditemukan, mulai dengan data kosong")
        todo = []
        add_id = 1

def save_data():
    data = {
        "todo": todo,
        "add_id": add_id
    }
    try:
        with open(todo_file, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"error saving data: {e}")


def find_id(task_id):
    for task in todo:
        if task["id"] == task_id:
            return task
    return None

def tambah_task(deskripsi):
    global todo, add_id
    task = {"id": add_id, "task": deskripsi, "done": False}
    todo.append(task)
    add_id += 1
    print(f"task: {deskripsi} ditambahkan dengan ID {task['id']})")
    save_data() 

def lihat_task():
    if not todo:
        print("tidak ada task")
        return
    else:
        for data in todo:
            if data['done']:
                status = "[✓]"
            else:
                status = "[ ]"
            print(f"{data['id']} {status} {data['task']}")

def tandai_selesai(task_id):
    global todo
    task = find_id(task_id)
    
    if not task:
        print(f"task dengan id {task_id} tidak ditemukan")
        sys.exit(0)
    
    if task['done']:
        print(f"task dengan id {task_id} sudah ditandai selesai sebelumnya")
        sys.exit(1)
    
    task['done'] = True
    print(f"task dengan id {task_id} sudah ditandai selesai")
    save_data()

def hapus_task(task_id):
    global todo
    task = find_id(task_id)
    
    if not task:
        print(f"task dengan id {task_id} tidak ditemukan")
        sys.exit(1)
    
    todo = [i for i in todo if i['id'] != task_id]
    print(f"{task_id} sudah dihapus")
    save_data()

load_file()
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

parser_add = subparser.add_parser("add", help="Menambahkan tugas")
parser_add.add_argument("task", help="Tulis kan task yang ingin dibuat")

parser_delete = subparser.add_parser("delete", help="Menghapus tugas")
parser_delete.add_argument("id", type=int, help="Id yang ingin dihapus")

parser_done = subparser.add_parser("done", help="Mengubah status menjadi done")
parser_done.add_argument("id", type=int, help="Id yang ditandai selesai")

parser_list = subparser.add_parser("list", help="Lihat semua task")

args = parser.parse_args()

if args.command == "add":
    tambah_task(args.task)

elif args.command == "list":
    lihat_task()

elif args.command == "done":
    tandai_selesai(args.id)

elif args.command == "delete":
    hapus_task(args.id)
else:
    parser.print_help()