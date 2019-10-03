#include <stdio.h>

void insertion_sort(int arr[], int len) {
    for (int j = 1; j < len; j++) {
        int key = arr[j];
        int i = j - 1 ;
        while ((i >= 0) && (arr[i] > key)) {
            arr[i+1] = arr[i];
            i--;
        }
        arr[i+1] = key;
    }
}

int main() {
    int arr[] = {3, 5, 2, 1, 4, -1};
    int len = 6;
    insertion_sort(arr, 6);
    for (int i = 0; i < len; i++) {
        char end = (i < len - 1) ? ' ': '\n';
        printf("%d%c", arr[i], end);
    }
    return 0;
}
