use 5.38.2;

# Day 1: Not Quite Lisp
# Part 1
# Counts which floor santa ends up if ')' is down 1 floor and '(' is up;

# replace test cases with personalized input
my $floors = ')())())';  
# =~ binds regex to a string, the regex stores all matches of char )
my @down_matches = $floors =~ /\)/g;
my @up_matches = $floors =~ /\(/g;
# using array in scalar context gets its length
say "Part 1 floor: ", scalar(@up_matches) - scalar(@down_matches);

# Day 1: Not Quite Lisp
# Part 2
# Counts when santa steps to basement (-1 floor)

my $cur_floor = 0;
my $counter = 0;
for my $c (split('', $floors)) {
    # eq as in equals, interesting as it's also comparison method in OData that is used with PlayFab (and elsewhere of course)
    $cur_floor += $c eq '(' ? 1 : -1; 
    $counter++;
    last if $cur_floor eq -1;
}
# easiest interpolation ever :)
say "$counter floors travelled when arriving at basement (-1 floor).";
