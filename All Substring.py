def powerset(string_list, size):
    powersetsize = 2**size

    for outer in range(0, powersetsize):
        subset = []
        for inner in range(0, size):
            if ((outer & (1 << inner)) > 0):
                subset.append(string_list[inner])
        
        print(f"{{{', '.join(subset)}}}")

size = int(input("Enter number of elements: "))
elements = []

for i in range(0, size):
    item = input(f"Enter element {i+1}: ")
    elements.append(item)

print("\nAll possible subsets (Powerset):")
powerset(elements, len(elements))
