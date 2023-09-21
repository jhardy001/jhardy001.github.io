package hardylab02;
import java.util.Scanner;

public class Exercise02_14 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Enter weight in pounds: ");
			double userWeight = input.nextDouble();
			System.out.print("Enter height in inches: ");
			double userHeight = input.nextDouble();
			
			double weightInKg = userWeight * 0.45359237;
			double heightInM = userHeight * 0.0254;
			
			System.out.print("BMI is " + weightInKg/(heightInM*heightInM));
		}
		
	}
}
