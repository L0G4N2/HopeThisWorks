import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Scrap scrap = new Scrap();
        Gravitation grav = new Gravitation();
        AverageStaticFriction avgStatFriction = new AverageStaticFriction();

        System.out.println("Do you need help calculating static friction? (Yes/No)");
        String needCalculator = scan.nextLine().toUpperCase();
        if (needCalculator.equals("Y") || needCalculator.equals("YES")) {
            System.out.println("How many trials did you complete?");
            int numOfTrials = scan.nextInt();
            System.out.println("Does your data need conversion? (true/false)");
            boolean needsConversion = scan.nextBoolean();
            System.out.println(avgStatFriction.calculate(numOfTrials, needsConversion));
        }

        System.out.println("Do you need help comparing the gravitation between objects? (Yes/No)");
        String needGravitation = scan.nextLine().toUpperCase();
        if (needGravitation.equals("Y") || needGravitation.equals("YES")) {
            System.out.println("How many systems are there?");
            int numOfSystems = scan.nextInt();
            System.out.println("Are the masses numerical or variable? (1 or 2)");
            boolean isVariables = true;
            int temp = scan.nextInt();
            if (temp == 1) {
                isVariables = false;
            }
            else if (temp == 2) {
                isVariables = true;
            }
            System.out.println("Is there one mass that is the same throughout all the systems? (Yes/No)");
            String sameMassAnswer = scan.nextLine().toUpperCase();
            boolean sameMass = false;
            while (!(sameMassAnswer.equals("Y") || sameMassAnswer.equals("YES"))) {
                sameMassAnswer = scan.nextLine().toUpperCase();
            }
            if (sameMassAnswer.equals("Y") || sameMassAnswer.equals("YES")) {
                sameMass = true;
            }
            ArrayList <Double> list = new ArrayList<>(grav.calculate(numOfSystems, isVariables, sameMass));
            System.out.println(list);
            System.out.println("Sort this data? (Yes/No)");
            String sort = scan.nextLine().toUpperCase();
            while (!(sort.equals("Y") || sort.equals("YES"))) {
                sort = scan.nextLine().toUpperCase();
            }
            if (sort.equals("Y")) {
                System.out.println(grav.sortNumList(list));
            }
        }

        System.out.println("Is there anything else you need? (y/n)");
        String needHelp = scan.nextLine().toUpperCase();
        while (!(needHelp.equals("Y") || needHelp.equals("N"))) {
            if (needHelp.equals("Y")) {
                System.out.println("What can I help with?");
                break;
            }
            else if (needHelp.equals("N")) {
                System.out.println("Well, bye bye then!");
                break;
            }
            else {
                System.out.println("Waiting on a valid response...");
                needHelp = scan.nextLine();
            }
        }

        System.out.println("If you would like to run anything else: Run \"scrap.trash.\"");
        System.out.println("Freely edit \"Scrap.java\" before running it.");
        System.out.println("Next, you\'d want to call the function from the \"Scrap\" class in the code.");
        // Uncomment the next line either by deleting the "//" or by selecting the line and pressing "CTRL + /"
        // scrap.trash();
    }
}
