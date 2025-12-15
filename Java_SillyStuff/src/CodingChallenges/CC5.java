import java.io.*;
import java.nio.file.*;
import java.util.*;

public class CC5 {
	public static void main(String[] args) throws Exception {
		String path = args.length > 0 ? args[0] : "Java_SillyStuff/src/CodingChallenges/input5.txt";
		List<String> lines = Files.readAllLines(Paths.get(path));

		// Map each step to its set of prerequisites
		Map<Character, Set<Character>> prereq = new HashMap<>();
		// All steps present
		Set<Character> steps = new HashSet<>();

		for (String line : lines) {
			if (line.trim().isEmpty()) continue;
			// Expected format: "Step C must be finished before step A can begin."
			String[] parts = line.split(" ");
			if (parts.length < 8) continue;
			char before = parts[1].charAt(0);
			char after = parts[7].charAt(0);
			steps.add(before);
			steps.add(after);
			prereq.computeIfAbsent(after, k -> new HashSet<>()).add(before);
			prereq.computeIfAbsent(before, k -> new HashSet<>());
		}

		// Use a TreeSet to always pick smallest alphabetical available step
		StringBuilder order = new StringBuilder();

		// Compute in-degree-like availability: steps whose prereq set is empty
		TreeSet<Character> available = new TreeSet<>();
		for (char s : steps) {
			Set<Character> p = prereq.getOrDefault(s, Collections.emptySet());
			if (p.isEmpty()) available.add(s);
		}

		while (!available.isEmpty()) {
			char cur = available.first();
			available.remove(cur);
			order.append(cur);

			// Remove cur as a prerequisite from others
			for (char s : new HashSet<>(prereq.keySet())) {
				Set<Character> p = prereq.get(s);
				if (p != null && p.remove(cur)) {
					if (p.isEmpty()) available.add(s);
				}
			}
		}

		System.out.println(order.toString());
	}
}