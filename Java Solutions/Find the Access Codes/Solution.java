public class Solution {
	public static int solution(int[] l) {
		int n = l.length;
		int f[] = new int[n];
		int triples = 0;
		
		for (int i=0; i<n; i++)
			for (int j=0; j<i; j++)
				if (l[i]%l[j]==0) {
					f[i]++;	
					triples += f[j];
				}
		
		return triples;
	}
}
