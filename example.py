import numpy as np
from she import RLWE, Rq

if __name__ == '__main__':
    n = 8  # power of 2
    q = 67108289  # prime number, q = 1 (mod 2n)
    t = 37  # prime number, t < q
    std = 3  # standard deviation of Gaussian distribution

    rlwe = RLWE(n, q, t, std)
    (sec, pub) = rlwe.generate_keys()

    m0 = Rq(np.random.randint(t, size=n), t)  # plaintext
    m1 = Rq(np.random.randint(t, size=n), t)  # plaintext

    c0 = rlwe.encrypt(m0, pub)
    c1 = rlwe.encrypt(m1, pub)

    m_0 = rlwe.decrypt(c0, sec)
    m_1 = rlwe.decrypt(c1, sec)

    print(m0)
    print(m_0)
    print()

    print(m1)
    print(m_1)
    print()

    print('# Add')
    print(m0 + m1)

    c_add = rlwe.add(c0, c1)
    m_add = rlwe.decrypt(c_add, sec)
    print(m_add)
    print()

    print('# Mul')
    print(m0 * m1)

    c_mul = rlwe.mul(c0, c1)
    m_mul = rlwe.decrypt(c_mul, sec)
    print(m_mul)
    print()
