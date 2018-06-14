#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void quick_sort(int* array, int start, int end) {

	if (start >= end) return;

	int mid = (start + end) / 2;
	int pivot = array[mid];

	swap(&array[start], &array[mid]);

	int p = start + 1, q = end;

	while (1) {
		while (array[p] <= pivot) { p++; }
		while (array[q]>pivot) { q--; }

		if (p>q) break;

		swap(&array[p], &array[q]);
	}

	swap(&array[start], &array[q]);

	quick_sort(array, start, q - 1);
	quick_sort(array, q + 1, end);

}

int main(void) {

	int array[] = { 6,3,11,9,12,2,8,15,18,7,14 };
	int i;

	quick_sort(array, 0, sizeof(array) / sizeof(int) - 1);

	for (i = 0; i< sizeof(array)/ sizeof(int); i++) {
		printf("%4d\n", array[i]);
	}

	return 0;
}


