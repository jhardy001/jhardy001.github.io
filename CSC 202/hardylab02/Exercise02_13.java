package hardylab02;
import java.util.Scanner;

public class Exercise02_13 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Enter monthly saving amount: ");
			double currentSavings = input.nextDouble();
			double monthlyInterest = 0.05/12;
			
			currentSavings = 100*(1+0.00417);
			System.out.println("After the first month, the account value is " + currentSavings);
			
			currentSavings = (100+currentSavings)*(1+monthlyInterest);
			System.out.println("After the second month, the account value is " + currentSavings);
			
			currentSavings = (100+currentSavings)*(1+monthlyInterest);
			System.out.println("After the third month, the account value is " + currentSavings);
			
			currentSavings = (100+currentSavings)*(1+monthlyInterest);
			currentSavings = (100+currentSavings)*(1+monthlyInterest);
			currentSavings = (100+currentSavings)*(1+monthlyInterest);
			System.out.println("After the sixth month, the account value is " + currentSavings);
		}
		
	}
}
