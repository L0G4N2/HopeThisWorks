package OraclePractice.JavaAssessment;

public class Q12 {
    private String color;
    public Q12() {
        this("white");
    }
    public Q12(String color) {
        color = color;
    }
    public static void main(String[] args) {
        Q12 e = new Q12();
        System.out.println("Color:" + e.color);
    }
}
