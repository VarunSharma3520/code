#include <iostream>
using namespace std;

/*
operation on array (Basically CRUD):
traversal
insertion
deletion
searching
*/
struct myArray
{
    int total_size;
    int used_size;
};

int traversal(int arr[5]){
    for (int i = 0; i < 5; ++i) {
        cout << i + 1 << ": " << arr[i] << endl;
    }
    return 0;
}

void insertElementArray (int keyPosition, int value, int arr[100], int maxSize, int elementSize)
{
    for(int i = elementSize; i >= keyPosition; i--){
        arr[i+1]=arr[i];
    }
    arr[keyPosition]=value;
    elementSize=elementSize+1;
    for (int i = 0; i < elementSize; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int deleteArray(int arr[100], int key, int elementSize){
    for(int i = key; i < elementSize; i++){
        arr[i] = arr[i+1];
    }
    elementSize--;
    for (int i = 0; i < elementSize; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}

int main() {
    // myArray marks;
    // marks.total_size=5;
    // marks.used_size=6;
    int marks[5] = {88, 76, 90, 61, 69};
    traversal(marks);

    int array[100]={10, 20, 40, 50, 60};
    insertElementArray(2, 30, array, 100, 5);
    deleteArray(array,1,6);
    return 0;
}