package hardylab04;

public class Exercise05_03 {
	public static void main(String[] args) {
		System.out.println("Kilograms	 Pounds");
		int kg = 1;
		double lbs = 2.2;
		while(kg<=199) {
			double lbsToKg = kg*lbs;
			System.out.print(kg + "	        ");
			System.out.printf("%7.1f \n", lbsToKg);
			kg+=2;
		}
	}
}
