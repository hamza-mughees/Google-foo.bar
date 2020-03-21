public static int solution(String n, int b) {
	int minionId = Integer.parseInt(n);
	
	List<Integer> list = new ArrayList<>();
	
	while(Integer.toString(minionId).length() > 1) {
		int digits[] = new int[n.length()];
		String xString = "";
		String yString = "";
		
		for (int i=digits.length-1; i>=0; i--) {
			digits[i] = minionId % 10;
			minionId /= 10;
		}
		
		// insertion sort to sort digits array
		for(int i=1; i<digits.length; i++)
		{
		  int j = i-1;
		  int tmp = digits[i];
		  while(j >= 0 && digits[j] > tmp)
		  {
			digits[j+1] = digits[j];
			j--;
		  }
		  digits[j+1] = tmp;
		}
		
		for (int i=0; i<digits.length; i++) {
			xString += digits[digits.length-i-1];
			yString += digits[i];
		}
		
		int x = Integer.parseInt(xString, b);
		int y = Integer.parseInt(yString, b);
		int z = Integer.parseInt(Integer.toString(x-y, b));
		
		for (int i=0; i<list.size(); i++)
			if (list.get(i) == z)
				return list.size()-i;
		minionId = z;
		list.add(minionId);
	}
	return 1;
}