use 5.38.2;
use Data::Dumper;

# Day 7: Some Assembly Required
# Part 1
# Bobby needs some help assembling his electronics kit.
# We got wires, logic gates, and more abbreviations 
# that a dictionary can hold.

my $input = "123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i";


my %wires = ();

for (split(/\n/, $input))
{
    unless ($_ =~ /[A-Z]/g)
    {
        my @words = $_ =~ /\w+/g;
        $wires{$words[1]} += $words[0];
    }
}

for (split(/\n/, $input))
{
    if ($_ =~ /AND/g)
    {
        my @words = split(' ', $_); 
        my $l = $words[0];
        my $r = $words[2];
        my $dest = $words[4];
        #say "$l & $r & $dest";
        $wires{"$dest"} += $wires{"$l"} & $wires{"$r"};
    }
    elsif ($_ =~ /OR/g)
    {
        my @words = split(' ', $_); 
        my $l = $words[0];
        my $r = $words[2];
        my $dest = $words[4];
        $wires{"$dest"} += $wires{"$l"} | $wires{"$r"};
    }
    elsif ($_ =~ /LSHIFT/g)
    {
        my @words = split(' ', $_); 
        my $l = $words[0];
        my $r = $words[2];
        my $dest = $words[4];
        $wires{"$dest"} += $wires{"$l"} << $r;
    }
    elsif ($_ =~ /RSHIFT/g)
    {
        my @words = split(' ', $_); 
        my $l = $words[0];
        my $r = $words[2];
        my $dest = $words[4];
        $wires{"$dest"} += $wires{"$l"} >> $r;
    }
    elsif ($_ =~ /NOT/g)
    {
        # some problems on this, still figuring it out
        my @words = split(' ', $_); 
        my $l = $words[1];
        my $l_val = pack 'n', $wires{"$l"};
        say $l_val;
        my $dest = $words[3];
        $wires{"$dest"} += unpack 'B16', ~$l_val;
    }
}

say "wires:";
for (keys %wires)
{
    say "$_: ", $wires{$_};
}
