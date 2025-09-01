def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min_left, max_left = maxmin_select(arr, left, mid)
    min_right, max_right = maxmin_select(arr, mid + 1, right)

    overall_min = min(min_left, min_right)
    overall_max = max(max_left, max_right)

    return overall_min, overall_max


if __name__ == "__main__":
    arr = [7, 2, 9, 4, 1, 5, 8, 3, 6]
    minimo, maximo = maxmin_select(arr, 0, len(arr) - 1)
    print("Lista:", arr)
    print("Menor elemento:", minimo)
    print("Maior elemento:", maximo)
