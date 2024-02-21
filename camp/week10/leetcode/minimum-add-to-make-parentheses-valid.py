class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st =[]
        for ch in s:
            if ch==')':
                if st and st[-1]=='(':
                    st.pop()
                else:
                    st.append(ch)
            else:
                st.append(ch)
            # print(st)
        return len(st)