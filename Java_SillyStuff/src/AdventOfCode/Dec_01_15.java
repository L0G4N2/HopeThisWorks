package AdventOfCode;

import java.util.*;

public class Dec_01_15 {

    public Dec_01_15(String input, boolean part1) {
        if (part1) {
            int floor = 0;
            for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                if (c == '(') {
                    floor++;
                } else if (c == ')') {
                    floor--;
                }
            }
            System.out.println("Final floor: " + floor);
        }
        else {
            int floor = 0;
            for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                if (c == '(') {
                    floor++;
                } else if (c == ')') {
                    floor--;
                }
                if (floor == -1) {
                    System.out.println("Position: " + (i + 1));
                    break;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        new Dec_01_15(input, true); // Part 1
        new Dec_01_15(input, false); // Part 2
    }
}
