//{ Driver Code Starts
// C++ program to find minimum swaps required
// to club all elements less than or equals
// to k together
#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends

class Solution
{
public:
    int minSwap(int arr[], int n, int k) {
        // Complet the function
    int count = 0;
    for (int i = 0; i < n; ++i)
        if (arr[i] <= k)
            ++count;
     
    // Find unwanted elements in current
    // window of size 'count'
    int bad = 0;
    for (int i = 0; i < count; ++i)
        if (arr[i] > k)
            ++bad;
     
    // Initialize answer with 'bad' value of
    // current window
    int ans = bad;
    for (int i = 0, j = count; j < n; ++i, ++j) {
         
        // Decrement count of previous window
        if (arr[i] > k)
            --bad;
         
        // Increment count of current window
        if (arr[j] > k)
            ++bad;
         
        // Update ans if count of 'bad'
        // is less in current window
        ans = min(ans, bad);
    }
    return ans;
    }
};



//{ Driver Code Starts.

// Driver code
int main() {

	int t,n,k;
	cin>>t;
	while(t--)
    {
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        cin>>k;
        Solution ob;
        cout << ob.minSwap(arr, n, k) << "\n";
    }
	return 0;
}

// } Driver Code Ends