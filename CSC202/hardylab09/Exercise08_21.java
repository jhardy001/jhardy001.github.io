package hardylab09;
import java.util.Scanner;

public class Exercise08_21 {

    public static void main(String[] args) {

    	try (Scanner input = new Scanner(System.in)) {
			System.out.println("Enter the number of cities: ");
			  int numCities = input.nextInt();
			  double[][] n = new double[numCities][2];
			  System.out.println("Enter the coordinates of the cities:");
			 
			  for (int i = 0; i < n.length; i++) {
			   n[i][0] = input.nextDouble();
			   n[i][1] = input.nextDouble();
			  }
			  double[] sumOfDistance = calSomeOfDistance(calDisstance(n));
			  int cityIndex = findMin(sumOfDistance);
			   
			  System.out.println("The central city is at (" + n[cityIndex][0] + "," +  n[cityIndex][1] + ")");
			  System.out.println("The total distance to all other cities is " + sumOfDistance[cityIndex]);
		}
    	 }
    	 
    	 public static double[][] calDisstance(double[][] n) {
    	 
    	  double[][] distances = new double[n.length][n.length];
    	  for (int i = 0; i < distances.length; i++) {
    	   for (int j = 0; j < distances.length; j++) {
    	    double x1 = n[i][0];
    	    double x2 = n[j][0];
    	    double y1 = n[i][1];
    	    double y2 = n[j][1];
    	    distances[i][j] = Math.sqrt(Math.pow(x1 - x2, 2)
    	      + Math.pow(y1 - y2, 2));
    	   }
    	  }
    	  return distances;
    	 }
    	 
    	 public static double[] calSomeOfDistance(double[][] n) {
    	 
    	  double[] sum = new double[n.length];
    	 
    	  for (int i = 0; i < sum.length; i++) {
    	   for (int j = 0; j < sum.length; j++) {
    	    sum[i] += n[i][j];
    	   }
    	 
    	  }
    	 
    	  return sum;
    	 
    	 }
    	 
    	 public static int findMin(double[] n) {
    	 
    	  double min = n[0];
    	  int minIndex = 0;
    	  for (int i = 0; i < n.length; i++) {
    	   if (min > n[i]) {
    	    min = n[i];
    	    minIndex = i;
    	   }
    	  }
    	  return minIndex;
    	 
    	 }
}