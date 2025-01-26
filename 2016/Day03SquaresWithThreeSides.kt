import kotlin.text.*
import kotlin.text.Regex.*

fun main() {
  // --- Day 3: Squares With Three Sides ---
  // How many valid triangles there are?
  // The sides of a valid triangle are as follows:
  // sum of two sides > remaining side
    
  // Part 1: count valid horizontal triangles.
  val triangles = """    1   2  3
  20  30  40
  90  100  110""".split("\n")

    var validOnes = 0
    for (i in 0..triangles.size - 1) {
        val nums = Regex("\\d+").findAll(triangles[i]).map{it.value.toInt()}.toList()
	if (nums[0] + nums[1] > nums[2] && nums[1] + nums[2] > nums[0] && nums[0] + nums[2] > nums[1]) {
            validOnes++
        }
    }
    println("P1: $validOnes")

    // Part 2: triangles are placed vertically, not horizontally.
    validOnes = 0
    // Add triangles to three separate triangle holders and 
    // then see if they are valid when they have 3 nums in them.
    var triangleLeft = IntArray(3) {0}
    var triangleMiddle = IntArray(3) {0}
    var triangleRight = IntArray(3) {0}
    // Is used to place triangle values in the triangle arrays and 
    // is used the check when the arrays are full.
    var triangleIndex = 0
    // Counts how many triangles there are in total.
    var triangleCounter = 0
    for (i in 0..triangles.size - 1) {
        val nums = Regex("\\d+").findAll(triangles[i]).map{it.value.toInt()}.toList()
	triangleLeft[triangleIndex] = nums[0]
	triangleMiddle[triangleIndex] = nums[1]
        triangleRight[triangleIndex] = nums[2]
	triangleIndex++

	// triangles full, check them for valid ones
	if (triangleIndex === 3) {
            triangleIndex = 0
	    triangleCounter += 3
            
            if (isValidTriangle(triangleLeft.toList())) {
		validOnes++
            }
	    if (isValidTriangle(triangleMiddle.toList())) {
		validOnes++
            }
	    if (isValidTriangle(triangleRight.toList())) {
		validOnes++
            }
        }
    }
    println("P2 total triangles: $triangleCounter")
    println("P2 valid triangles: $validOnes")
}

// Returns if a triangle is valid or not based on
// if sum of two sides > remaining side.
fun isValidTriangle(nums: List<Int>): Boolean {
    return (nums[0] + nums[1] > nums[2] && nums[1] + nums[2] > nums[0] && nums[0] + nums[2] > nums[1])
}
