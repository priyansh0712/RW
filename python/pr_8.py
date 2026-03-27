import numpy as np


class DataAnalytics:
    instance_count = 0

    def __init__(self, array=None):
        self.array = None
        if array is not None:
            self.array = np.array(array)
        DataAnalytics.instance_count += 1

    def set_array(self, array):
        self.array = np.array(array)
        print("\nArray created successfully:")
        print(self.array)

    def display_array(self):
        if self.array is None:
            print("No array available.")
            return
        print("\nCurrent Array:")
        print(self.array)

    def _check_array_exists(self):
        return self.array is not None

    def __flatten_array(self):
        return self.array.flatten()

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                n = int(input("Enter number of elements: "))
                elements = list(map(float, input(f"Enter {n} elements separated by space: ").split()))
                if len(elements) != n:
                    print("Invalid number of elements.")
                    return
                self.set_array(elements)

            elif choice == "2":
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = rows * cols
                elements = list(map(float, input(f"Enter {total} elements for the array separated by space: ").split()))
                if len(elements) != total:
                    print("Invalid number of elements.")
                    return
                arr = np.array(elements).reshape(rows, cols)
                self.set_array(arr)

            elif choice == "3":
                x = int(input("Enter size of first dimension: "))
                y = int(input("Enter size of second dimension: "))
                z = int(input("Enter size of third dimension: "))
                total = x * y * z
                elements = list(map(float, input(f"Enter {total} elements for the array separated by space: ").split()))
                if len(elements) != total:
                    print("Invalid number of elements.")
                    return
                arr = np.array(elements).reshape(x, y, z)
                self.set_array(arr)

            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

    def indexing_and_slicing(self):
        if not self._check_array_exists():
            print("No array available. Create an array first.")
            return

        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    if self.array.ndim == 1:
                        i = int(input("Enter index: "))
                        print("Element:", self.array[i])

                    elif self.array.ndim == 2:
                        r = int(input("Enter row index: "))
                        c = int(input("Enter column index: "))
                        print("Element:", self.array[r, c])

                    elif self.array.ndim == 3:
                        i = int(input("Enter first dimension index: "))
                        j = int(input("Enter second dimension index: "))
                        k = int(input("Enter third dimension index: "))
                        print("Element:", self.array[i, j, k])

                elif choice == "2":
                    if self.array.ndim == 1:
                        start, end = map(int, input("Enter range (start:end): ").split(":"))
                        print("\nSliced Array:")
                        print(self.array[start:end])

                    elif self.array.ndim == 2:
                        row_range = input("Enter the row range (start:end): ").strip()
                        col_range = input("Enter the column range (start:end): ").strip()

                        r1, r2 = map(int, row_range.split(":"))
                        c1, c2 = map(int, col_range.split(":"))

                        print("\nSliced Array:")
                        print(self.array[r1:r2, c1:c2])

                    elif self.array.ndim == 3:
                        print("For 3D slicing, enter ranges for all three dimensions.")
                        d1 = input("Enter first dimension range (start:end): ").strip()
                        d2 = input("Enter second dimension range (start:end): ").strip()
                        d3 = input("Enter third dimension range (start:end): ").strip()

                        a1, a2 = map(int, d1.split(":"))
                        b1, b2 = map(int, d2.split(":"))
                        c1, c2 = map(int, d3.split(":"))

                        print("\nSliced Array:")
                        print(self.array[a1:a2, b1:b2, c1:c2])

                elif choice == "3":
                    break
                else:
                    print("Invalid choice.")
            except Exception as e:
                print("Error:", e)

    def mathematical_operations(self):
        if not self._check_array_exists():
            print("No array available. Create an array first.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product / Matrix Multiplication")

        choice = input("Enter your choice: ").strip()

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                total = self.array.size
                elements = list(map(float, input(f"Enter the same-size array elements ({total} elements separated by space): ").split()))
                if len(elements) != total:
                    print("Invalid number of elements.")
                    return

                second_array = np.array(elements).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(second_array)

                if choice == "1":
                    print("\nResult:")
                    print(self.array + second_array)

                elif choice == "2":
                    print("\nResult:")
                    print(self.array - second_array)

                elif choice == "3":
                    print("\nResult:")
                    print(self.array * second_array)

                elif choice == "4":
                    print("\nResult:")
                    print(self.array / second_array)

                elif choice == "5":
                    if self.array.ndim == 2 and second_array.ndim == 2:
                        if self.array.shape[1] == second_array.shape[0]:
                            print("\nDot Product / Matrix Multiplication Result:")
                            print(np.dot(self.array, second_array))
                        else:
                            print("Matrix multiplication not possible due to shape mismatch.")
                    else:
                        print("Dot product / matrix multiplication is supported here for 2D arrays only.")
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

    def combine_or_split_arrays(self):
        if not self._check_array_exists():
            print("No array available. Create an array first.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                total = self.array.size
                elements = list(map(float, input(f"Enter the elements of another array to combine ({total} elements separated by space): ").split()))
                if len(elements) != total:
                    print("Invalid number of elements.")
                    return

                second_array = np.array(elements).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(second_array)

                if self.array.ndim == 1:
                    combined = np.concatenate((self.array, second_array))
                    print("\nCombined Array:")
                    print(combined)
                else:
                    combined = np.vstack((self.array, second_array))
                    print("\nCombined Array (Vertical Stack):")
                    print(combined)

            elif choice == "2":
                if self.array.ndim == 1:
                    parts = int(input("Enter number of parts to split into: "))
                    result = np.array_split(self.array, parts)
                    print("\nSplit Arrays:")
                    for i, part in enumerate(result, start=1):
                        print(f"Part {i}: {part}")

                elif self.array.ndim == 2:
                    axis_choice = input("Split by rows or columns? (r/c): ").strip().lower()
                    parts = int(input("Enter number of parts to split into: "))

                    if axis_choice == "r":
                        result = np.array_split(self.array, parts, axis=0)
                    elif axis_choice == "c":
                        result = np.array_split(self.array, parts, axis=1)
                    else:
                        print("Invalid axis choice.")
                        return

                    print("\nSplit Arrays:")
                    for i, part in enumerate(result, start=1):
                        print(f"Part {i}:")
                        print(part)

                else:
                    parts = int(input("Enter number of parts to split along first axis: "))
                    result = np.array_split(self.array, parts, axis=0)
                    print("\nSplit Arrays:")
                    for i, part in enumerate(result, start=1):
                        print(f"Part {i}:")
                        print(part)
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

    def search_sort_filter(self):
        if not self._check_array_exists():
            print("No array available. Create an array first.")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.array == value)

                if len(positions) == 0:
                    print("Value not found.")
                else:
                    print("\nValue found at positions:")
                    for pos in positions:
                        print(tuple(pos))

            elif choice == "2":
                order = input("Sort in ascending or descending? (a/d): ").strip().lower()

                if self.array.ndim == 1:
                    sorted_array = np.sort(self.array)
                    if order == "d":
                        sorted_array = sorted_array[::-1]
                else:
                    sorted_array = np.sort(self.array, axis=-1)
                    if order == "d":
                        sorted_array = np.flip(sorted_array, axis=-1)

                print("\nOriginal Array:")
                print(self.array)
                print("\nSorted Array:")
                print(sorted_array)
                print("(Sorting applied on last axis.)")

            elif choice == "3":
                print("\nFilter conditions:")
                print("1. Greater than")
                print("2. Less than")
                print("3. Equal to")

                cond = input("Enter your choice: ").strip()
                value = float(input("Enter comparison value: "))

                if cond == "1":
                    filtered = self.array[self.array > value]
                elif cond == "2":
                    filtered = self.array[self.array < value]
                elif cond == "3":
                    filtered = self.array[self.array == value]
                else:
                    print("Invalid condition.")
                    return

                print("\nFiltered Values:")
                print(filtered)

            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

    def aggregate_and_statistics(self):
        if not self._check_array_exists():
            print("No array available. Create an array first.")
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Percentiles")
        print("7. Correlation Coefficient")

        choice = input("Enter your choice: ").strip()

        try:
            flat = self.__flatten_array()

            if choice == "1":
                print("\nOriginal Array:")
                print(self.array)
                print("\nSum of Array:", np.sum(self.array))

            elif choice == "2":
                print("\nOriginal Array:")
                print(self.array)
                print("\nMean of Array:", np.mean(self.array))

            elif choice == "3":
                print("\nOriginal Array:")
                print(self.array)
                print("\nMedian of Array:", np.median(self.array))

            elif choice == "4":
                print("\nOriginal Array:")
                print(self.array)
                print("\nStandard Deviation of Array:", np.std(self.array))

            elif choice == "5":
                print("\nOriginal Array:")
                print(self.array)
                print("\nVariance of Array:", np.var(self.array))

            elif choice == "6":
                p = float(input("Enter percentile value (0-100): "))
                print("\nOriginal Array:")
                print(self.array)
                print(f"\n{p}th Percentile:", np.percentile(flat, p))

            elif choice == "7":
                total = self.array.size
                elements = list(map(float, input(f"Enter another array for correlation ({total} elements separated by space): ").split()))
                if len(elements) != total:
                    print("Invalid number of elements.")
                    return
                second_array = np.array(elements).flatten()

                if len(flat) != len(second_array):
                    print("Arrays must have same number of elements.")
                    return

                corr = np.corrcoef(flat, second_array)[0, 1]
                print("\nFirst Array (flattened):")
                print(flat)
                print("\nSecond Array:")
                print(second_array)
                print("\nCorrelation Coefficient:", corr)

            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

    @classmethod
    def show_instance_count(cls):
        print(f"\nTotal DataAnalytics objects created: {cls.instance_count}")

    @staticmethod
    def show_numpy_version():
        print("\nNumPy Version:", np.__version__)


def main():
    analyzer = DataAnalytics()

    while True:
        print("\n" + "=" * 40)
        print("Welcome to the NumPy Analyzer!")
        print("=" * 40)
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Indexing and Slicing")
        print("3. Perform Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort, or Filter Arrays")
        print("6. Compute Aggregates and Statistics")
        print("7. Display Current Array")
        print("8. Show NumPy Version")
        print("9. Show Object Count")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analyzer.create_array()
        elif choice == "2":
            analyzer.indexing_and_slicing()
        elif choice == "3":
            analyzer.mathematical_operations()
        elif choice == "4":
            analyzer.combine_or_split_arrays()
        elif choice == "5":
            analyzer.search_sort_filter()
        elif choice == "6":
            analyzer.aggregate_and_statistics()
        elif choice == "7":
            analyzer.display_array()
        elif choice == "8":
            DataAnalytics.show_numpy_version()
        elif choice == "9":
            DataAnalytics.show_instance_count()
        elif choice == "10":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
