import java.util.*;
import java.io.*;

public class CC3 {
    public CC3() {
        int sum = 0;

        try {
            File file = new File("c:\\Users\\LJGDA\\Documents\\GitHub\\HopeThisWorks\\Java_SillyStuff\\src\\CodingChallenges\\input3.txt");
            Scanner scan = new Scanner(file);

            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                
                // Check each digit against the next digit
                for (int i = 0; i < line.length(); i++) {
                    int currentNum = Integer.parseInt(line.substring(i, i + 1));
                    int nextNum;
                    
                    // If we're at the last digit, compare with the first digit
                    if (i == line.length() - 1) {
                        nextNum = Integer.parseInt(line.substring(0, 1));
                    } else {
                        nextNum = Integer.parseInt(line.substring(i + 1, i + 2));
                    }
                    
                    if (currentNum == nextNum) {
                        sum += currentNum;
                    }
                }
            }

            scan.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println("Sum: " + sum);
    }

    public static void main(String[] args) {
        new CC3();
    }
}