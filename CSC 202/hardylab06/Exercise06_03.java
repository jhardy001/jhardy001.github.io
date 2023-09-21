package hardylab06;
import java.util.Scanner;

public class Exercise06_03 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Please enter an integer to reverse: ");
			int value = input.nextInt();
			
			if((isPalindrome(value))){
			    System.out.println(value + " is a palindrome");
			}else{
			    System.out.println(value + " is not a palindrome");
			}
		}      
       
    }
	
	public static int reverse(int number) {
		int temp = number;
		int reverse = 0;
		
		while (temp != 0) {
			int remainder = temp % 10;
			reverse = reverse * 10 + remainder;
			temp = temp / 10;
		}
		
		return reverse;
	}
	
	public static boolean isPalindrome(int number) {
		if (number == reverse(number)) {
			return true;
		}
		return false;
	}
}
