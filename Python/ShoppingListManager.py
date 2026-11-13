def add_item(items,name):
    if not name or not name.strip():
        print("Enter Valid Item name!")
        return
    cleaned_name = name.strip()
    if any(item.lower()== cleaned_name.lower() for item in items):
        print(f"Rejected: '{cleaned_name}' already exist in the list.")
        return

    items.append(cleaned_name)
    print(f"success! '{cleaned_name}' has been added.")
def remove_item(items,name):
    if not name or not name.strip():
        print("Error: Item name cannot be empty or whitespcae-only. ")
        return
    cleaned_name = name.strip()
    for item in items:
        if item.lower() == cleaned_name.lower():
            items.remove(item)
            print(f"Success: '{cleaned_name} has been removed.")
            return
        print(f"Notice: '{cleaned_name}' was not not found in list")
def show_items(items):
    if not items:
        print("No Items found in list ")
        return
    print('current items')
    for index,item in enumerate(items,start=1):
        print(f"{index}.{item}")
    print("-----------------")

def main():
    items = []
    while True:
        print("\n--- Item Manager Menu ---\n1.Add Item\n2.Remove Item\n3.Show Items\n4.Quit")
        choice = input("Enter The Choice: ")
        if choice == "1":
            name = input("Enter the name of the item to add.")
            if not  name.strip():
                print("Error: Item name cannot be empty or whitespace-only")
                continue
            add_item(items,name)
        elif choice == "2":
            name = input("Enter name of item to remove.")
            if not name.strip():
                print("Error: Item name cannot be empty of whitespaces-only")
                continue
            remove_item(items,name)
        elif choice == "3":
            show_items(items)
        else:
            print("Cart Existed! ")
            break
if __name__ == "__main__":
    main()

