#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> manacher(string d) {
  int n = d.length() * 2;
  vector<int> m(++n);
  int tc = 0;
  int bp_prime, enp_prime;
  for (int enp = 0; enp < n; ++enp) {
    int bp = tc + m[tc];
    if (enp > bp) bp_prime = enp - 1, enp_prime = enp + 1;
    else {
      int enp_symmetric = 2 * tc - enp;
      if (enp + m[enp_symmetric] >= bp) {
        enp_prime = bp + 1;
        bp_prime = 2 * enp - enp_prime;
        m[enp] = bp - enp;
      }
      else {
        m[enp] = m[enp_symmetric];
        bp_prime = enp_prime = -1;
      }
    }
    while (0 <= bp_prime
      && enp_prime < n
      && (bp_prime % 2 == 0
        || max(bp_prime, enp_prime) < n << 1
        && d[bp_prime >> 1] == d[enp_prime >> 1]))
        m[enp]++, bp_prime--, enp_prime++;
    if (enp + m[enp] > bp) tc = enp;
  }
  return m;
}
