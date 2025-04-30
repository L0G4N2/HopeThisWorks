package APClassroomFarm;

public class ExperimentalFarm {
    private Plot[][] farmPlots;
    public ExperimentalFarm(Plot[][] p) {
        farmPlots = p;
    }

    /** Returns the plot with the highest yield for a given crop type, as described in part (a). */
    public Plot getHighestYield(String c) {
        /* to be implemented in part (a) */
        Plot highest = null;
        for (Plot[] r: farmPlots) {
            for (Plot plot: r) {
                if (plot.getCropType().equals(c) && (highest == null || plot.getCropYield() > highest.getCropYield())) {
                    highest = plot;
                }
            }
        }
        return highest;
    }

    /** Returns true if all plots in a given column in the two-dimensional array farmPlots
     * contain the same type of crop, or false otherwise, as described in part (b).
     */
    public boolean sameCrop(int col) {
        /* to be implemented in part (b) */
        String crop = farmPlots[0][col].getCropType();
        for (int i = 1; i < farmPlots.length; i++) {
            if (!farmPlots[i][col].getCropType().equals(crop)) {
                return false;
            }
        }
        return true;
    }
}