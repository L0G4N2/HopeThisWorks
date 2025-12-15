package AdventOfCode;

import java.util.*;

public class Dec_02_15 {
    public Dec_02_15(int length, int width, int height, boolean part1) {
        if (part1) {
            int lw = length * width;
            int wh = width * height;
            int hl = height * length;
            int surfaceArea = 2 * (lw + wh + hl);
            int extra = Math.min(lw, Math.min(wh, hl));
            int totalPaper = surfaceArea + extra;
            System.out.println("Total wrapping paper needed: " + totalPaper);
        } else {
            int side1 = Math.min(length, Math.min(width, height));
            int side2;
            if (side1 == length) {
                side2 = Math.min(width, height);
            } else if (side1 == width) {
                side2 = Math.min(length, height);
            } else {
                side2 = Math.min(length, width);
            }
            int perimeter = 2 * (side1 + side2);
            int volume = length * width * height;
            int totalRibbon = perimeter + volume;
            System.out.println("Total ribbon needed: " + totalRibbon);
        }

    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int length = scan.nextInt();
        int width = scan.nextInt();
        int height = scan.nextInt();
        new Dec_02_15(length, width, height, true);  // Part 1
        // new Dec_02_15(length, width, height, false); // Part 2
    }
}
