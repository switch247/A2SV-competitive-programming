class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        A = [0] * (n+1)
        for l, r , x in bookings:
            A[ l-1 ] += x
            A[r] -= x
        # print(A)
        for i in range(1,len(A)):A[i] += A[i-1]
        return A[:n]
