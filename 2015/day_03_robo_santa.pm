use 5.38.2;
use feature "switch";

# Day 3: Perfectly Spherical Houses in a Vacuum
# Part 1
# Counts how many houses receive a gift which happens
# if santa visits the house in an infinite 2D grid
# hash keeps track of visited locations

my %houses;
my $directions = " ^><^>>";
my $x_pos = 0;
my $y_pos = 0;

# then process other directions
for my $dir (split('', $directions)) {
    given ($dir)
    {
      when ('^') { $y_pos++; }
      when ('v') { $y_pos--; }
      when ('<') { $x_pos--; }
      when ('>') { $x_pos++; }
      default {}
    }
    $houses{"$x_pos $y_pos"} += 1;
}

my $lucky_houses = 0;
for (keys %houses)
{
  if ($houses{$_} > 0)
  {
    $lucky_houses++;
  }
}

say "Part 1 \t Amount of houses at least 1 gift: $lucky_houses.";


# Day 3: Perfectly Spherical Houses in a Vacuum
# Part 2
# Next year robo santa delivers presents with santa each taking turns on the instructions
# Calculate how many houses get presents this year

%houses = ();
say scalar(%houses);
$x_pos = 0;
$y_pos = 0;
my $robo_y_pos = 0;
my $robo_x_pos = 0;

my $turn_num = 0;
for my $dir (split('', $directions)) {
    if ($turn_num == 0)
    {
        # first both santas deliver present to (0, 0)
        $houses{"$x_pos $y_pos"} += 1;
        $houses{"$robo_x_pos $robo_y_pos"} += 1;
    }
    elsif ($turn_num % 2 == 1)
    {
        # santa goes first
        given ($dir)
        {
          when ('^') { $y_pos++; }
          when ('v') { $y_pos--; }
          when ('<') { $x_pos--; }
          when ('>') { $x_pos++; }
          default {}
        }
        $houses{"$x_pos $y_pos"} += 1;
    }
    elsif ($turn_num % 2 == 0)
    {
        given ($dir)
        {
          when ('^') { $robo_y_pos++; }
          when ('v') { $robo_y_pos--; }
          when ('<') { $robo_x_pos--; }
          when ('>') { $robo_x_pos++; }
          default {}
        }
        $houses{"$robo_x_pos $robo_y_pos"} += 1;
    }
    
    $turn_num++;
}

$lucky_houses = 0;
for (keys %houses)
{
  if ($houses{$_} > 0)
  {
    $lucky_houses++;
  }
}

say "Part 2 \t Amount of houses with over 1 gift: $lucky_houses.";
