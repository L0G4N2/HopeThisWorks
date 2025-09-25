package OraclePractice.JavaAssessment;

public class Q8 {
    public Q8() { System.out.print("Deer"); }
    public Q8 (int age) { System.out.print("DeerAge"); }
    private boolean hasHorns() { return false; }
    public static void main(String[] args) {
        Q8 q8 = new Reindeer(5);
        System.out.println(","+q8.hasHorns());
    }
}

class Reindeer extends Q8 {
    public Reindeer(int age) { System.out.print("Reindeer"); }
    public boolean hasHorns() { return false; }
}
