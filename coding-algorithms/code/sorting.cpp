#include <algorithm>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& a) {
  for (int i = 1; i < a.size(); i++) {
    int j = i;
    while (j && a[j - 1] > a[j]) swap(a[j], a[--j]);
  }
}

void MergeSort(vector<int>& a) {
  int n = a.size();
  vector<int> b(n);
  for (int width = 1; width < n; width *= 2) {
    for (int start = 0; start < n; start += 2 * width) {
      int left = start, right = mid;
      int mid = min(start + width, n), end = min(start + 2 * width, n);
      int k = start;
      while (left < mid && right < end)
        b[k++] = a[left] > a[right] ? a[right++] : a[left++];
      while (left < mid) b[k++] = a[left++];
      while (right < end) b[k++] = a[right++];
    }
    copy(b.begin(), b.end(), a.begin());
  }
}
