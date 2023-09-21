package hardylab06;

public class Exercise06_09 {
	public static void main(String[] args) {
		
		double feet = 1.0;
		double meters = 20.0;
		
		System.out.println("Feet     Meters         Meters         Feet");
		System.out.println("---------------------------------------------");
		while(feet <= 10.0 && meters <= 65.0) {
			System.out.printf("%4.1f     %6.3f", feet, footToMeter(feet));
			System.out.print("          ");
			System.out.printf("%-11.1f%7.3f\n", meters, meterToFoot(meters));
			feet++;
			meters+=5;
		}
	}
	
	public static double footToMeter(double foot) {
		return 0.305*foot;
	}
	
	public static double meterToFoot(double meter){
		return 3.279*meter;
	}
}
