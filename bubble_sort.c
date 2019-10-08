#include <stdio.h>

void print_arr(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        char end = (i < len - 1) ? ' ': '\n';
        printf("%d%c", arr[i], end);
    }
}

void bubble_sort(int arr[], int len) {
    bool swap = false;
    for (int k = 0; k < len; k++) {
        for (int i = 0; i < len-k-1; i++) {
            if (arr[i] > arr[i+1]) {
                int c = arr[i+1];
                arr[i+1] = arr[i];
                arr[i] = c;
                swap = true;
            }
        }
        if (!swap) {
            break;
        }
    }
}

int main() {
    int arr[] = {3, 5, 2, 1, 4, -1};
    int len = sizeof(arr)/sizeof(*arr);   
    bubble_sort(arr, len);
    print_arr(arr, len);
    return 0;
}