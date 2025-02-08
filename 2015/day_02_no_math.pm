use 5.38.2;
use List::Util qw(min max);

# Day 2: I Was Told There Would Be No Math
# Part 1
# Counts how much wrapping paper is needed for gifts when
# the dimensions are known and the shape is a right rectangular prism

my $gifts = '2x3x4
1x1x10';

my $paper_needed = 0;

for my $line (split('\n', $gifts)) {
    (my $l, my $w, my $h) = $line =~ /\d+/g;  
    my $smallest_side = min($l * $w, $w * $h, $h * $l);
    # say "l$l w$w h$h and smallest is $smallest_side";
    # 2*l*w + 2*w*h + 2*h*l + smallest side
    $paper_needed += 2 * $l * $w + 2 * $w * $h + 2 * $h * $l + $smallest_side;
}

say "Part 1 wrapping paper needed: $paper_needed square feet.";


# Day 2: I Was Told There Would Be No Math
# Part 2
# Counts how much ribbon is needed:
# smallest perimeter + volume (cubic feet)

my $ribbon_needed = 0;

for my $line (split('\n', $gifts)) {
    (my $l, my $w, my $h) = $line =~ /\d+/g;  
    my $smallest_perimeter = min(2* $l + 2* $w, 2 * $w + 2* $h, 2* $h + 2* $l);
    # say "smallest is $smallest_perimeter";
    $ribbon_needed += $l * $w * $h + $smallest_perimeter;
}

say "Part 2 ribbon needed: $ribbon_needed.";
