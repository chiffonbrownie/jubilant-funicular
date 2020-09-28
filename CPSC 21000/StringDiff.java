import java.util.Scanner;
import java.util.Random;

public class StringDiff {
	public static void main (String[] args) {
		
		//declare variables + add scanner and random
		String userString, generatedString = "";
		char userChar, generatedChar;
		int generatedInt, distance = 0;
		Scanner scan = new Scanner(System.in);
		Random rand = new Random();
		
		//ask for input
		System.out.print("Please enter a string of 5 uppercase characters: ");
		userString = scan.nextLine();
		
		//generate random string using length of inout string
		for (int i= 0; i < userString.length(); i++) {
			generatedInt = rand.nextInt(26) + 65; //[0...25] + 65 = [65...90]
			generatedString = generatedString + (char)generatedInt;
		}
		
		//iterate through both strings
		for (int i = 0; i < userString.length(); i++) {
			
			//get character at current index 
			userChar = userString.charAt(i);
			generatedChar = generatedString.charAt(i);
			
			//turn current index character to integer
			int userAscii = userChar;
			int generatedAscii = generatedChar;
			
			//fancy maths
			//take absolute value of current char and add to distance
			distance += Math.abs(userAscii - generatedAscii);
		}
		
		//print out strings
		System.out.println("\nThe user string is: " + userString+"\n");
		System.out.println("A random string is: " + generatedString+"\n");
		System.out.printf("The distance between %s and %s is %d", userString, generatedString, distance);
		
		//close scanner
		scan.close();		
	}

}
