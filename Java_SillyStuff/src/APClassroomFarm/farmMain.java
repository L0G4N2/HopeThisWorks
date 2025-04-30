package APClassroomFarm;

public class farmMain {
    public static void main(String[] args) {
        Plot[][] plots = {{new Plot("corn", 32), new Plot("peas", 30), new Plot("corn", 50)},
                                {new Plot("rice", 40), new Plot("peas", 10), new Plot("peas", 10)},
                                {new Plot("corn", 60), new Plot("peas", 50), new Plot("wheat", 70)}};
        ExperimentalFarm f = new ExperimentalFarm(plots);
        System.out.println(f.getHighestYield("corn").getCropYield());
        System.out.println(f.sameCrop(1));
    }
}