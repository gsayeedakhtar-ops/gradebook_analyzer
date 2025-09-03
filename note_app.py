def add_note():
    note = input("Write your note:")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
        print("Note saved!")

def view_notes():
    try:
       with open("notes.txt", "r") as f:
           notes = f.readlines()
           if not notes:
               print("No notes found.")
           else:
               print("\n--- Your Notes ---")
               for i, note in enumerate(notes, start=1):
                   print(f"{i}: {note.strip()}")
    except FileNotFoundError:
        print("No notes file found, Add a note first!")

def main():
    while True:
        print("\n Mini Note App")
        print("1. Add Note")
        print("2. View Note")
        print("3. Exit")

        choice = input("choose an option: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting App. Goodbye!")
            break
        else:
            print("Invalid choice. Try Again.")
if __name__ == "__main__":
    main()
