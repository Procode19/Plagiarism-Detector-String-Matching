# src/rabin_karp.py

def rabin_karp_search(text, pattern):
    """
    Rabin-Karp String Matching
    """

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    if m > n:
        return False

    p_hash = 0
    t_hash = 0
    h = 1

    # Calculate h
    for _ in range(m - 1):
        h = (h * d) % q

    # Initial hash
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Sliding Window
    for i in range(n - m + 1):

        # Hash matched
        if p_hash == t_hash:

            # Character verification
            if text[i:i+m] == pattern:
                return True

        # Recalculate hash
        if i < n - m:

            t_hash = (
                d * (t_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return False