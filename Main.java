import java.util.Scanner;
public class Main {

    public static double AverageStaticFriction(int numOfTrials, boolean needsConversion) {
        Scanner scan = new Scanner(System.in);
        double staticFriction = 0;
        if (needsConversion == false) {
            for (int i = 1; i <= numOfTrials; i++) {
                System.out.println("Enter the masses from Trial " + i + ".");
                System.out.println("Enter the first mass: ");
                double mass1 = scan.nextDouble();
                System.out.println("Enter the second mass: ");
                double mass2 = scan.nextDouble();
                staticFriction += (mass2 / mass1);
            }
        }
        else if (needsConversion == true) {
            System.out.println("Which column needs to be converted? 1, 2, or Both(3)?");
            String whichColumn = scan.nextLine();
            if (whichColumn.equals("1")) {
                for (int i = 1; i <= numOfTrials; i++) {
                    System.out.println("Enter the masses from Trial " + i + ".");
                    System.out.println("Enter the first mass: ");
                    double mass1 = scan.nextDouble();
                    System.out.println("Enter the second mass: ");
                    double mass2 = scan.nextDouble();
                    staticFriction += ((mass2) / (mass1 / 1000));
                }
            }
            else if (whichColumn.equals("2")) {
                for (int i = 1; i <= numOfTrials; i++) {
                    System.out.println("Enter the masses from Trial " + i + ".");
                    System.out.println("Enter the first mass: ");
                    double mass1 = scan.nextDouble();
                    System.out.println("Enter the second mass: ");
                    double mass2 = scan.nextDouble();
                    staticFriction += ((mass2 / 1000) / (mass1));
                }
            }
            else if (whichColumn.toUpperCase().equals("BOTH") || whichColumn.equals("3")) {
                for (int i = 1; i <= numOfTrials; i++) {
                    System.out.println("Enter the masses from Trial " + i + ".");
                    System.out.println("Enter the first mass: ");
                    double mass1 = scan.nextDouble();
                    System.out.println("Enter the second mass: ");
                    double mass2 = scan.nextDouble();
                    staticFriction += ((mass2 / 1000) / (mass1 / 1000));
                }
            }
        }
        return (staticFriction / numOfTrials);
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Do you need help calculating static friction? (y/n)");
        String needCalculator = scan.nextLine();
        if (needCalculator.equals("y")) {
            System.out.println("How many trials did you complete?");
            int numOfTrials = scan.nextInt();
            System.err.println("Does your data need conversion? (true/false)");
            boolean needsConversion = scan.nextBoolean();
            System.out.println(AverageStaticFriction(numOfTrials, needsConversion));
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
                System.out.println("I do not understand your response...");
                needHelp = scan.nextLine();
            }
        }
    }
}
