package hardylab03;
import java.util.Scanner;
public class Exercise03_14 {
	public static void main(String[] args) {
		try (Scanner input = new Scanner (System.in)) {
      int coin = (int)(Math.random()*2);
      
      System.out.println("Guess head or tail? Enter 0 for head and 1 for tail: ");
      int userGuess = input.nextInt();
      
      if(userGuess == coin){
              System.out.println("Correct guess");
          }
          else{
            if(coin==0){
              System.out.println("Sorry, it is a head");
            }
            else{
              System.out.println("Sorry, it is a tail");
            }
          }
    }
		}
	}
