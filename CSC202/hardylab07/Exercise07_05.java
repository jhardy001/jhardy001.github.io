package hardylab07;
import java.util.Scanner;

public class Exercise07_05 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			int[] distinctNumbers = new int[10];
			int num; 				
			int count = 0;			

			System.out.print("Enter ten numbers: ");
			for (int i = 0; i < 10; i++) {
				num = input.nextInt();

				if (isDistinct(distinctNumbers, num)) {
					distinctNumbers[count] = num;
					count++;	
				}
			}

			System.out.println("The number of distinct numbers is " + count);
			System.out.print("The distinct numbers are");
			for (int i = 0; i < distinctNumbers.length; i++) {
				if (distinctNumbers[i] > 0)
					System.out.print(" " + distinctNumbers[i]);
			}
		}

		System.out.println();
	}

	public static boolean isDistinct(int[] array, int num) {
		for (int i = 0; i < array.length; i++) {
			if (num == array[i]) 
				return false;
		}
		return true;
	}
}