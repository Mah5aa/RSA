# RSA
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. 
The RSA algorithm involves four steps: key generation, key distribution, encryption, and decryption. A basic principle behind RSA is the observation that it is practical to find three very large positive integers e, d, and n, such that with modular exponentiation for all integers m (with 0 ≤ m < n):

(m^e)^d≡m(mod n)
and that knowing e and n, or even m, it can be extremely difficult to find d.The triple bar (≡) here denotes modular congruence (which is to say that when you divide (me)d by n and m by n, they both have the same remainder).
- for more informations visit wikipedia and relative articles about RSA https://en.wikipedia.org/wiki/RSA_(cryptosystem)
--------------------------

In the context of RSA, when we say an "N bit prime", we mean that it's a prime in the range [2n−1,2n)

In addition, when we say an RSA key is an "N bit key", we mean that it's in the range [2n−1,2n). What this means that if you pick two random N/2 bit primes, and multiply them together, you'll get an N−1 bit modulus about half the time. To avoid this, one common practice is to select the primes from the range (2–√⋅2n/2−1,2n/2)

that way, when we multiply the two primes together, we'll always get an N-bit key.

-----------------------
This project includes two files . In the file pq.txt I saved all 28bits primes that RSA code in line 34 found. So if a user wanted to test the code manually, she(he) can choose unique p,q and enjoy coding!
