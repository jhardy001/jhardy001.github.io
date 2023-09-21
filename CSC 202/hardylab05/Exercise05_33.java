package hardylab05;

public class Exercise05_33 {
	public static void main(String[] args) {
		int numPerfect = 0;
		int sumOfDivisor = 0;
		
		for(int i=1; i <= 10000; i++) {
			for (int j = 1; j < i; j++) {
				if (i%j == 0) {
				sumOfDivisor += j;
				}
			}
		if (sumOfDivisor == i) {
				System.out.println(i+ " is a perfect number");
				numPerfect ++;
			}
		sumOfDivisor = 0;
		}
		System.out.println("Total number of perfect numbers is " + numPerfect);
	}
}
