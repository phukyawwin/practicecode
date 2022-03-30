def areAlmostEqual(s1, s2):
    max_diffs=2
    diffs=0
    st = set()
    st2 = set()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs+=1
        if s1[i] not in st:
            st.add(s1[i])
        if s2[i] not in st2:
            st2.add(s2[i])
        if diffs > max_diffs:
            return False
    return (diffs == 0 or diffs == 2) and len(st) == len(st2) and st == st2
s1 = "bakk"
s2 = "kabk"
#s1="caa"
#s2="aaz"
#s1 = "attack"
#s2 = "defend"
print(areAlmostEqual(s1, s2))
