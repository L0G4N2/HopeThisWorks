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
                staticFriction += (mass1 / mass2);
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
                    staticFriction += ((mass1 / 1000) / (mass2));
                }
            }
            else if (whichColumn.equals("2")) {
                for (int i = 1; i <= numOfTrials; i++) {
                    System.out.println("Enter the masses from Trial " + i + ".");
                    System.out.println("Enter the first mass: ");
                    double mass1 = scan.nextDouble();
                    System.out.println("Enter the second mass: ");
                    double mass2 = scan.nextDouble();
                    staticFriction += ((mass1) / (mass2 / 1000));
                }
            }
            else if (whichColumn.toUpperCase().equals("BOTH") || whichColumn.equals("3")) {
                for (int i = 1; i <= numOfTrials; i++) {
                    System.out.println("Enter the masses from Trial " + i + ".");
                    System.out.println("Enter the first mass: ");
                    double mass1 = scan.nextDouble();
                    System.out.println("Enter the second mass: ");
                    double mass2 = scan.nextDouble();
                    staticFriction += ((mass1 / 1000) / (mass2 / 1000));
                }
            }
        }
        staticFriction /= numOfTrials;
        return staticFriction;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println(AverageStaticFriction(6, true));
    }
}
