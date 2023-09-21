package hardylab04;
import java.util.Scanner;

public class Exercise05_01 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			int posNum = 0;
			int negNum = 0;
			int total = 0;
			System.out.println("Enter a num (0 to quit): ");
			int num = input.nextInt();
			while (num!=0) {
				if(num>0) {
					posNum++;
				}
				if(num<0) {
					negNum++;
				}
				total += num;
				num = input.nextInt();
			}
			double average = total/(double)(posNum + negNum);
			System.out.println("The number of positives is " + posNum);
			System.out.println("The number of negatives is " + negNum);
			System.out.println("The total is " + total);
			System.out.println("The average is " + average);
		}
	}
}
