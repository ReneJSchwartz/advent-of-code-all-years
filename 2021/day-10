console.log(`2011/10/Part 1
`)


str = `[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]`.split("\n")

starting = ["[", "{", "(", "<"]
stopping = ["]", "}", ")", ">"]

totalIllegalPts = 0

for (x in str)
{
	line = str[x]
	braceStack = []
	for (y in line)
	{
		c = line[y]
		if (starting.includes(c))
		{
			braceStack.push(c)
		}
		else if (stopping.includes(c))
		{
			startingBrace = braceStack.slice(-1)[0]
			if (startingBrace == "[" && c == "]")
			{
				console.log("[] match")
				braceStack.pop()
			}
			else if (startingBrace == "{" && c == "}")
			{
				console.log("{} match")
				braceStack.pop()
			}
			else if (startingBrace == "(" && c == ")")
			{
				console.log("() match")
				braceStack.pop()
			}
			else if (startingBrace == "<" && c == ">")
			{
				console.log("<> match")
				braceStack.pop()
			}
			else
			{
				// add first illegal brace to illegal pts and move on to next line
				if (c == ")")
				{
					totalIllegalPts += 3
				}
				if (c == "]")
				{
					totalIllegalPts += 57
				}
				if (c == "}")
				{
					totalIllegalPts += 1197
				}
				if (c == ">")
				{
					totalIllegalPts += 25137
				}
				break
			}
		}
	}
	console.log(braceStack.join(""))
}
console.log("totalIllegalPts: " + totalIllegalPts)
