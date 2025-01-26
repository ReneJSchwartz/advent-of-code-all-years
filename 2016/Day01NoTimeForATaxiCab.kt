fun main() {
    // --- Day 1: No Time for a Taxicab ---
    // How many blocks away is Easter Bunny HQ?
    // You first face north and then get directions
    // that turn you to some dir and then you walk
    // for example 5 blocks to that dir
    // when all instructions are given how far away
    // Easter Bunny HQ is from the starting point?

    val cardinalDirs = arrayOf("N", "E", "S", "W")
    var dirIndex = 100;
    println("curDir: " + cardinalDirs[dirIndex % 4])
    println(cardinalDirs.joinToString())
    
    val instructions = "R5, L5, R5, R3".split(", ")
    println(instructions)
    var x = 0
    var y = 0
    // Part 2 ans is the first location visited twice
    var visitedLocations = HashMap<String, Int> ()

    for (i in 0..instructions.size - 1) {
        val dir = instructions[i][0];
	var num = instructions[i].substring(1).toInt()	

	if (dir === 'R') {
            dirIndex++
        }
        else if (dir === 'L') {
            dirIndex--
        }
        
        if (cardinalDirs[dirIndex % 4] === "N") {
	    // Save every visited location and not just the destination
            for (i in 1..num) {
                y++;
				visitedLocations["$y $x"] = visitedLocations.getOrDefault("$y $x", 0) + 1
        
                if (visitedLocations.get("$y $x") == 2) {
                    println("P2: y$y/x$x")
                    return
                }
            }
	    // approach for p2 won't cut it anymore
	    // y += num
        }
        else if (cardinalDirs[dirIndex % 4] === "S") {
            for (i in 1..num) {
                y--;
				visitedLocations["$y $x"] = visitedLocations.getOrDefault("$y $x", 0) + 1
        
                if (visitedLocations.get("$y $x") == 2) {
                    println("P2: y$y/x$x")
                    return
                }
            }
        }
        else if (cardinalDirs[dirIndex % 4] === "E") {
            for (i in 1..num) {
                x++;
				visitedLocations["$y $x"] = visitedLocations.getOrDefault("$y $x", 0) + 1
        
                if (visitedLocations.get("$y $x") == 2) {
                    println("P2: y$y/x$x")
                    return
                }
            }
        }
        else if (cardinalDirs[dirIndex % 4] === "W") {
            for (i in 1..num) {
                x--;
				visitedLocations["$y $x"] = visitedLocations.getOrDefault("$y $x", 0) + 1
        
                if (visitedLocations.get("$y $x") == 2) {
                    println("P2: y$y/x$x")
                    return
                }
            }
        }    
    }
    println("P1: y$y/x$x")
}
