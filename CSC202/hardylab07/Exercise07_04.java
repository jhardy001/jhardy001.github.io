package hardylab07;
import java.util.Scanner;

public class Exercise07_04 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Enter scores: (negative number signifies end): ");
			
			int[] scores = new int[100];  	
			int num; 	
			int numScores; 	
			int average; 				
			numScores = average = 0;		
			for (int i = 0; i < 100; i++) {
				num = input.nextInt();			
				if (num < 0)				
					break;
				
				scores[i] = num;			
				average += num;		
				numScores++;		
			}

			average /= numScores;	

			int equalOrMore;				
			int below;					
			equalOrMore = below = 0;
			for (int i = 0; i < numScores; i++) {
				if (scores[i] >= average)
					equalOrMore++;		
				else
					below++;			
			}

			System.out.println("\nAverage of scores: " + average);
			System.out.println(
				"Number of scores above or equal to average: " + equalOrMore);
			System.out.println(
				"Number of scores below average: " + below);
		}
	}
}