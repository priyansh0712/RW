class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry: ")

        try:
            file = open(self.filename, "a")   # append mode
            file.write(entry + "\n")
            file.close()
            print("Entry added successfully.")
        except:
            print("Error while writing to file.")

    def view_entries(self):
        try:
            file = open(self.filename, "r")   # read mode
            content = file.read()
            file.close()

            if content == "":
                print("Journal is empty.")
            else:
                print("\nAll Entries:")
                print(content)

        except FileNotFoundError:
            print("No journal file found.")

    def search_entry(self):
        keyword = input("Enter word to search: ")

        try:
            file = open(self.filename, "r")
            lines = file.readlines()
            file.close()

            found = False
            for line in lines:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print("No matching entry found.")

        except FileNotFoundError:
            print("Journal file does not exist.")

    def delete_entries(self):
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            file = open(self.filename, "w")   # clears file
            file.close()
            print("All entries deleted.")
        else:
            print("Cancelled.")


def main():
    manager = JournalManager()

    while True:
        print("\n1. Add Entry")
        print("2. View Entries")
        print("3. Search Entry")
        print("4. Delete All")
        print("5. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                manager.add_entry()
            case "2":
                manager.view_entries()
            case "3":
                manager.search_entry()
            case "4":
                manager.delete_entries()
            case "5":
                print("Bye.")
                break
            case _:
                print("Invalid choice.")
main()              
