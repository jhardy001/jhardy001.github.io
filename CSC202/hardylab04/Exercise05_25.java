package hardylab04;
import java.util.Scanner;

public class Exercise05_25 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			double sum = 0;
			double value = input.nextDouble();
			for (double i = 1; i <= (2 * value - 1); i += 2) {
				sum += 1 / i;
				i += 2;
				sum -= 1 / i;
			}
			double pi = 4 * sum;
			System.out.print(pi);
		}
	}
}
