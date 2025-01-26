import kotlin.text.*
import kotlin.text.Regex.*

fun main() {
  // --- Day 3: Squares With Three Sides ---
  // How many valid triangles there are?
  // The sides of a valid triangle are as follows:
  // sum of two sides > remaining side
    
 	val triangles = """    1   2  3
  20  30  40
  90  100  110""".split("\n")

	var validOnes = 0
    for (i in 0..triangles.size - 1) {
        val nums = Regex("\\d+").findAll(triangles[i]).map{it.value.toInt()}.toList()
		    if (((nums[0] + nums[1]) > nums[2]) && ((nums[1] + nums[2]) > nums[0]) && ((nums[0] + nums[2]) > nums[1])) {
            validOnes++
        }
    }
    println("P1: $validOnes")
}
