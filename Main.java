import java.util.Scanner;
public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Scrap scrap = new Scrap();
        Gravitation grav = new Gravitation();
        AverageStaticFriction avgStatFriction = new AverageStaticFriction();

        System.out.println("Do you need help calculating static friction? (y/n)");
        String needCalculator = scan.nextLine();
        if (needCalculator.equals("y") || needCalculator.equals("Y")) {
            System.out.println("How many trials did you complete?");
            int numOfTrials = scan.nextInt();
            System.out.println("Does your data need conversion? (true/false)");
            boolean needsConversion = scan.nextBoolean();
            System.out.println(avgStatFriction.calculate(numOfTrials, needsConversion));
        }

        System.out.println("Do you need help comparing the gravitation between objects? (y/n)");
        String needGravitation = scan.nextLine();
        if (needGravitation.equals("y") || needGravitation.equals("Y")) {
            System.out.println("How many systems are there?");
            int numOfMasses = scan.nextInt();
            System.out.println(grav.calculate(numOfMasses));
        }

        System.out.println("Is there anything else you need? (y/n)");
        String needHelp = scan.nextLine();
        while (!(needHelp.equals("y") || needHelp.equals("n"))) {
            if (needHelp.equals("y")) {
                System.out.println("What can I help with?");
                break;
            }
            else if (needHelp.equals("n")) {
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
