use 5.38.2;

# Day 5: Doesn't He Have Intern-Elves For This?
# Part 1
# Look for nice strings in santas text-file (using what else than regex!).
# Nice strings have 3+vowels, double letter, and it does not contain 
# certain substrings like ab or pq

my $santas_text_file = "ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb";

my $nice_strings = 0;

for (split(/\n/, $santas_text_file))
{
  my @vowels = $_ =~ /[aeiou]/g;
  next if scalar(@vowels) < 3;
  
  my @double_letter = $_ =~ /(\w)\1/g;
  next unless scalar(@double_letter);
  
  # forbidden combinations
  next if $_ =~ /ab|cd|xy|pq/g;
  
  $nice_strings++;
}

say "Nice strings found p1: $nice_strings";

# Part 2
# Out with the old rules, obviously nice strings are those that:
# have a pair of non-overlapping double letters like xyfillerxy, and
# have a double letter with 1 letter in between it like efe, xyx, aaa.

#$santas_text_file = "qjhvhtzxzqqjkmpb
#xxyxx
#uurcxstgmygtbstg
#ieodomkazucvgmuy";

$nice_strings = 0;

for (split(/\n/, $santas_text_file))
{
  my @triplet = $_ =~ /(\w).\1/g;
  next unless scalar(@triplet);
  
  my @pair = $_ =~ /(\w{2})(?=.*\1)/g;
  next unless scalar(@pair);
  
  $nice_strings++;
}

say "Nice strings found p2: $nice_strings";
