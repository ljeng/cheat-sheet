#include <string>
#include <vector>

using namespace std;

vector<int> KnuthMorrisPratt(string pattern, string text) {
  int j, m = pattern.length(), t = 0, k = 0, n = text.length();
  vector<int> lps(m + 1);
  for (j = 1; j < m; lps[++j] = t) {
    while (t && pattern[j] != pattern[t]) t = lps[t];
    t += pattern[j] == pattern[t];
  }
  j = 0;
  vector<int> matches;
  while (k < n) {
    while (j && text[k] != pattern[j]) j = lps[j];
    j += text[k++] == pattern[j];
    if (j == m) {
      matches.push_back(k - j);
      j = lps[j];
    }
  }
  return matches;
}