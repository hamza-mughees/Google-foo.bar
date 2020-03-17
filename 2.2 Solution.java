public static int[] solution(int[] pegs) {
	// Your code here
	int distances[] = new int[pegs.length - 1];
	// Will contain distances in reverse order

	int solution[] = new int[2];
	// Will contain solution

	for (int i = 1; i < pegs.length; i++)
		distances[distances.length - i] = pegs[i] - pegs[i - 1];
		
	/*
	 * E.g. pegs = [4, 30, 50, 60] then reversed distances = [10, 20, 26] => 10-20+26-r =
	 * (1/2)r. (I mathematically derived this pattern, noticing that the signs always
	 * alternate, which I could use)
	 */

	int patternSum = 0;
	int index = 0;

	while (index < distances.length) {
		if (index % 2 == 0)
			patternSum += distances[index++];
		else
			patternSum -= distances[index++];
	}

	if (index % 2 == 0) {
		// patternSum + r = (1/2)r
		// patternSum = -(1/2)r
		// r = -2(patternSum)
		solution[0] = -2 * patternSum;
		solution[1] = 1;
	} else {
		// patternSum - r = (1/2)r
		// patternSum = (3/2)r
		// r = 2(patternSum)/3
		solution[0] = 2 * patternSum;
		if (solution[0] % 3 == 0) {
			solution[0] /= 3;
			solution[1] = 1;
		} else solution[1] = 3;
	}
	
	if (solution[0] / solution[1] < 1 ||
			solution[0] / solution[1] >= distances[distances.length-1] ||
			solution[0] / solution[1] > 2*distances[0]) { // invalid answer (no answer)
		solution[0] = -1;
		solution[1] = -1;
	}
	
	int prevRadius = solution[0] / solution[1];
			
	for (int i=distances.length-2; i>=0 && solution[0] != -1; i--) {
		if (distances[i+1] - prevRadius >= distances[i]) {
			solution[0] = -1;
			solution[1] = -1;
		}
		prevRadius = distances[i+1] - prevRadius;
	}
	
	return solution;
}