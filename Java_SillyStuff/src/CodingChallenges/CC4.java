import java.util.*;
import java.io.*;

public class CC4 {
    public CC4(){
        try {
            File file = new File("c:\\Users\\LJGDA\\Documents\\GitHub\\HopeThisWorks\\Java_SillyStuff\\src\\CodingChallenges\\input4.txt");
            Scanner scan = new Scanner(file);

            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < line.length(); i++) {
                    char c = line.charAt(i);
                    if (sb.length() > 0) {
                        char last = sb.charAt(sb.length() - 1);
                        // Check if characters are the same letter but different case
                        if (Character.toLowerCase(last) == Character.toLowerCase(c) && last != c) {
                            sb.deleteCharAt(sb.length() - 1);
                            continue;
                        }
                    }
                    sb.append(c);
                }
                
                String reduced = sb.toString();
                System.out.println(reduced);
                System.out.println("Length: " + reduced.length());
            }

            scan.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new CC4();
    }
}