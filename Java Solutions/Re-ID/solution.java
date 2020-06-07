public class Solution {
	public static String solution(int i) {
		String primeString = "";
			
		for (int j=2; j<21000; j++) {
			boolean isPrime = true;
			for (int k=j/2; k>1; k--) {
				if (j%k == 0) isPrime = false;
			}
			if (isPrime) primeString += Integer.toString(j);
		}
		
		return primeString.substring(i, i+5);
	}
}