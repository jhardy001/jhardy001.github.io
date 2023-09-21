package hardylab04;
import java.util.Scanner;

public class Exercise05_26 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
		}
		double item = 1;
		double e = 1;
		for(int i = 1; i<= 20; i++) {
			item=item/i;
			e += item;
			System.out.print(e + " " + i);
		}
	}
}
