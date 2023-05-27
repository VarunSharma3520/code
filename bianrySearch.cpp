#include<iostream>
using namespace std;

    // Binary search implementation
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;  // Element found, return its index...
        }

        if (arr[mid] < target) {
            left = mid + 1;  // Target is in the right half...
        } else {
            right = mid - 1;  // Target is in the left half...
        }
    }

    return -1;  // Element not found
}  

int main(){
    int arr[100]={1,2,3,4,5,6,7,8,9,10};
    int usedSize = 10;
    int elem = 1;
    cout<<binarySearch(arr,usedSize,elem);
    return 0;
}