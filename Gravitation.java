import java.util.ArrayList;
import java.util.Scanner;

public class Gravitation {
    public double force(double m1, double m2, double r) {
        double G = (6.674) * (Math.pow(10, -11));
        return(G * ((m1 * m2)/(r * r)));
    }
    public ArrayList<Double> calculate(int numOfSystems, boolean isVariables, boolean sameMass) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Double> forces = new ArrayList<>();
        if (isVariables == false && sameMass == false) {
            for (int i = 1; i <= numOfSystems; i++) {
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
        else if (isVariables == false && sameMass == true) {
            System.out.print("Enter the mass that is the same throughout all the systems: ");
            double m1 = scan.nextDouble();
            System.out.println();
            for (int i = 1; i <= numOfSystems; i++) {
                System.out.println("System " + i + ":");
                System.out.print("Enter the mass of the second object: ");
                double m2 = scan.nextDouble();
                System.out.println();
                System.out.print("Enter the distance between the masses: ");
                double r = scan.nextDouble();
                forces.add(force(m1, m2, r));
            }
            return(forces);
        }
        else if (isVariables == true && sameMass == true) {
            System.out.print("Enter the factor of the mass that is the same throughout all the systems: ");
            double f1 = scan.nextDouble();
            System.out.println();
            for (int i = 1; i <= numOfSystems; i++) {
                System.out.println("System " + i + ":");
                System.out.print("Enter the factor of the mass of the second object: ");
                double f2 = scan.nextDouble();
                System.out.println();
                System.out.print("Enter the factor of the distance between the masses: ");
                double fr = scan.nextDouble();
                forces.add(force((3 * f1), (4 * f2), (5 * fr)));
            }
            return(forces);
        }
        else if (isVariables == true && sameMass == false) {
            for (int i = 1; i <= numOfSystems; i++) {
                System.out.println("System " + i + ":");
                System.out.print("Enter the factor of the first mass: ");
                double f1 = scan.nextDouble();
                System.out.println();
                System.out.print("Enter the factor of the second mass: ");
                double f2 = scan.nextDouble();
                System.out.println();
                System.out.print("Enter the factor of the distance between the masses: ");
                double fr = scan.nextDouble();
                forces.add(force((3 * f1), (4 * f2), (5 * fr)));
            }
            return(forces);
        }
        else {
            return(null);
        }
    }
    public ArrayList<Double> sortNumList(ArrayList<Double> list) {
        ArrayList<Double> temp = new ArrayList<>(list);
        int size = temp.size();
        ArrayList<Double> sortedList = new ArrayList<>();
        while (sortedList.size() != size) {
            double greatestNum = 0;
            if (temp.size() == 1) {
                greatestNum = temp.get(0);
                sortedList.add(greatestNum);
                temp.remove(greatestNum);
            }
            else {
                for (int i = 0; i < temp.size(); i++) {
                    if (temp.get(i) > greatestNum) {
                        greatestNum = temp.get(i);
                    }
                }
                sortedList.add(greatestNum);
                temp.remove(greatestNum);
            }
        }
        return(sortedList);
    }
}
