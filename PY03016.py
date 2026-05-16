n = int(input())
st = []
ans = 0

for _ in range(n):
    x = int(input())
    cnt = 1

    while st and st[-1][0] < x:
        ans += st[-1][1]
        st.pop()

    if st and st[-1][0] == x:
        c = st[-1][1]
        ans += c
        st.pop()

        if st:
            ans += 1

        st.append((x, c + 1))
    else:
        if st:
            ans += 1
        st.append((x, 1))

print(ans)