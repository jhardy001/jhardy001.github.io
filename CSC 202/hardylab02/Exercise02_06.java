package hardylab02;
import java.util.Scanner;

public class Exercise02_06 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Enter an integer between 0 and 1000: ");
			int number = input.nextInt();
			
			System.out.print(number/100 + (number%100)/10 + number%10);
		}
	}
}
