package hardylab05;
import java.util.Scanner;

public class Exercise05_41 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			int largest = 0;
			int occurence = 0;
			int num;
			
			System.out.print("Enter a number: ");
			do {
				num = input.nextInt();
				if (num>largest) {
					occurence = 0;
					largest = num;
				}
				if (num == largest) {
					occurence ++;
				}
			} while (num!=0);
			
			System.out.println("The largest number is " + largest);
			System.out.println("The number of occurences is " + occurence);
		}
	}
}
