#include <algorithm>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& a) {
  for (int i = 1; i < a.size(); i++) {
    int j = i;
    while (j && a[j - 1] > a[j]) swap(a[j], a[--j]);
  }
}
