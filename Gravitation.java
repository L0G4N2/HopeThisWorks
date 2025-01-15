import java.util.ArrayList;
import java.util.Scanner;

public class Gravitation {
    public double force(double m1, double m2, double r) {
        double G = (6.674) * (10 ^ -11);
        return(G * ((m1 * m2)/(r * r)));
    }
    public ArrayList<Double> calculate(int numOfMasses) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Double> forces = new ArrayList<>();
        for (int i = 1; i <= numOfMasses; i++) {
            System.out.println("System " + i + ":");
            System.out.print("Enter the first mass: ");
            double m1 = scan.nextDouble();
            System.out.println();
            System.out.print("Enter the second mass: ");
            double m2 = scan.nextDouble();
            System.out.println();
            System.out.print("Enter the distance between the masses: ");
            double r = scan.nextDouble();
            forces.add(force(m1, m2, r));
        }
        return(forces);
    }
}
