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
            y += num
        }
        else if (cardinalDirs[dirIndex % 4] === "S") {
            y -= num
        }
        else if (cardinalDirs[dirIndex % 4] === "E") {
            x += num
        }
        else if (cardinalDirs[dirIndex % 4] === "W") {
            x -= num
        }    
    }
    println("P1: y$y/x$x")
}
