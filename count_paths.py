def count_paths(x, y):
    # Base case: if we are at the origin (0, 0), there's exactly one path (we are already there)
    if x == 0 or y == 0:
        return 1
    # Recursive case: the number of paths is the sum of paths from (x-1, y) and (x, y-1)
    return count_paths(x - 1, y) + count_paths(x, y - 1)

# Example usage:
if __name__ == "__main__":
    n, m = 3, 3
    print(f"Number of different paths from ({n},{m}) to (0,0): {count_paths(n, m)}")
