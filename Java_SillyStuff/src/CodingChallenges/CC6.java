import java.nio.file.*;
import java.util.*;

public class CC6 {
	public static void main(String[] args) throws Exception {
		String path = args.length > 0 ? args[0] : "Java_SillyStuff/src/CodingChallenges/input6.txt";
		List<String> lines = Files.readAllLines(Paths.get(path));

		int validCount = 0;
		for (String line : lines) {
			if (line == null) continue;
			line = line.trim();
			if (line.isEmpty()) continue;

			String[] words = line.split("\\s+");
			Set<String> seen = new HashSet<>();
			boolean valid = true;
			for (String w : words) {
				if (!seen.add(w)) { // duplicate
					valid = false;
					break;
				}
			}
			if (valid) validCount++;
		}

		System.out.println("Valid passphrases: " + validCount);
	}
}