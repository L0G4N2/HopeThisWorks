import java.util.*;
import java.io.*;

public class CC2 {
    public CC2() {
        int doubles = 0;
        int triples = 0;

        try {
            File file = new File("c:\\Users\\LJGDA\\Documents\\GitHub\\HopeThisWorks\\Java_SillyStuff\\src\\CodingChallenges\\input2.txt");
            Scanner scan = new Scanner(file);

            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                Map<Character, Integer> charCount = new HashMap<>();
                
                for (int i = 0; i < line.length(); i++) {
                    char c = line.charAt(i);
                    charCount.put(c, charCount.getOrDefault(c, 0) + 1);
                }
                
                boolean hasDouble = false;
                boolean hasTriple = false;
                
                for (int count: charCount.values()) {
                    if (count == 2) hasDouble = true;
                    if (count == 3) hasTriple = true;
                }
                
                if (hasDouble) {
                    doubles++;
                }
                if (hasTriple) {
                    triples++;
                }
            }
            
            scan.close();
            
            int checksum = doubles * triples;
            System.out.println("Doubles: " + doubles);
            System.out.println("Triples: " + triples);
            System.out.println("Checksum: " + checksum);
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new CC2();
    }
}