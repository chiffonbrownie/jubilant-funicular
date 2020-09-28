import java.util.Scanner;

public class AgeGuess {
	public static void main(String[] args) {
		
		// Declare variables + scanner object scan
		String name;
		int ageGuess;
		Scanner scan = new Scanner(System.in);

		// Ask user for name and age
		System.out.print("Enter name: ");
		name=scan.nextLine();		//Accepts Name
		System.out.print("Enter age: ");
		ageGuess=scan.nextInt();	//Accepts Age
		
		// Print out name and ageGuess
		System.out.println("Name is "+name);
		System.out.println("Age is "+ageGuess);
	}
}
