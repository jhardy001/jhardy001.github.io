package hardylab04;

public class Exercise05_05 {
	public static void main(String[] args) {
		int kg = 1;
		int lbs = 20;
		final double KG_TO_LBS = 2.2;
		System.out.println("Kilograms    Pounds     |     Pounds      Kilograms");
		while(kg <= 199 && lbs <= 515) {
			System.out.printf("%-12d%7.1f", kg, (kg * KG_TO_LBS));
			System.out.print("     |     ");
			System.out.printf(
				"%-9d%12.2f\n",
				lbs, (lbs / KG_TO_LBS));
			kg+=2;
			lbs+=5;
		}
	}
}
