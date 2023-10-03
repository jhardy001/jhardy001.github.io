package hardylab03;
import java.util.Scanner;

public class Exercise03_07 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner (System.in)) {
			// Receive the amount
			System.out.print("Enter an amount in double, for example, 11.56: ");
			double amount = input.nextDouble();
			int remainingAmount = (int)(amount * 100);
			
			// Find the number of one dollars
			int numberOfOneDollars = remainingAmount / 100;
			remainingAmount = remainingAmount % 100;
			
			// Find the number of quarters in the remaining amount
			int numberOfQuarters = remainingAmount / 25;
			remainingAmount = remainingAmount % 25;
			
			// Find the number of dimes in the remaining amount
			int numberOfDimes = remainingAmount / 10;
			remainingAmount = remainingAmount % 10;
			
			// Find the number of nickels in the remaining amount
			int numberOfNickels = remainingAmount / 5;
			remainingAmount = remainingAmount % 5;
			
			// Find the number of pennies in the remaining amount
			int numberOfPennies = remainingAmount;
			
			// Display results
			System.out.println("Your amount " + amount + " consists of");
			
			//if one dollar
			if (numberOfOneDollars == 1) {
				System.out.println("    " + numberOfOneDollars + " dollar");
			}
			else {
				System.out.println("    " + numberOfOneDollars + " dollars");
			}
			
			//if one quarter
			if (numberOfQuarters == 1) {
				System.out.println("    " + numberOfQuarters + " quarters");
			}
			else {
				System.out.println("    " + numberOfQuarters + " quarters");
			}
			
			//if one dime
			if (numberOfDimes == 1) {
				System.out.println("    " + numberOfDimes + " dime"); 
			}
			else {
				System.out.println("    " + numberOfDimes + " dimes"); 
			}
			
			//if one nickel
			if (numberOfNickels == 1) {
				System.out.println("    " + numberOfNickels + " nickel");
			}
			else {
				System.out.println("    " + numberOfNickels + " nickels");
			}
			
			//if one penny
			if (numberOfPennies == 1) {
				System.out.println("    " + numberOfPennies + " penny");
			}
			else {
				System.out.println("    " + numberOfPennies + " pennies");
			}
		}
		}
	}
