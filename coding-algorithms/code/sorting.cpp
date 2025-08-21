#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

void InsertionSort(vector<int>& a) {
  for (int i = 1; i < a.size(); i++)
    for (int j = i; j && a[j - 1] > a[j]; swap(a[j], a[--j]));
}

void Quicksort(vector<int>& a) {
  stack<pair<int, int>> ranges;
  ranges.emplace(0, a.size() - 1);
  int i, j;
  while (!ranges.empty()) {
    auto [lo, hi] = ranges.top();
    ranges.pop();
    if (lo < hi) {
      for (i = lo - 1, j = lo; j < hi; j++)
        if (a[j] < a[hi])
          swap(a[++i], a[j]);
      swap(a[++i], a[hi]);
      ranges.emplace(lo, i - 1);
      ranges.emplace(i + 1, hi);
    }
  }
}

void MergeSort(vector<int>& a) {
  int n = a.size();
  vector<int> b(n);
  int k;
  for (int width = 1; width < n; width *= 2) {
    for (int start = 0; start < n; start += 2 * width) {
      int mid = min(start + width, n), end = min(start + 2 * width, n);
      int left = start, right = mid;
      for (k = start;
         left < mid && right < end;
         b[k++] = a[left] > a[right] ? a[right++] : a[left++]);
      while (left < mid) b[k++] = a[left++];
      while (right < end) b[k++] = a[right++];
    }
    copy(b.begin(), b.end(), a.begin());
  }
}

void HeapSort(vector<int>& a) {
  int count = a.size();
  int start = count >> 1, end = count;
  while (end > 1) {
    if (start) start--;
    else swap(a[0], a[--end]);
    int root = start;
    while (true) {
      int child = 2 * root;
      if (++child >= end) break;
      child += child + 1 < end && a[child] < a[child + 1];
      if (a[root] < a[child]) {
        swap(a[root], a[child]);
        root = child;
      }
      else break;
    }
  }
}
