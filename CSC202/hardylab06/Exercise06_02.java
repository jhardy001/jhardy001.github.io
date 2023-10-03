package hardylab06;
import java.util.Scanner;

public class Exercise06_02 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Enter an integer to sum the digits of: ");
			long num = input.nextLong();
			System.out.println("The sum of all digits is: " + sumDigits(num));
		}
	}
		
		
		public static int sumDigits(long n){
			int temp = (int)Math.abs(n);
			int sum = 0;
			
			while(temp != 0) {
				sum += temp%10;
				temp = temp/10;
			}
			
			return sum;
	}
}
