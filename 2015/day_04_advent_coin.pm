use 5.38.2;
use Digest::MD5 qw(md5 md5_hex md5_base64);

# Day 4: The Ideal Stocking Stuffer
# Part 1 and part 2
# Mine AdventCoin for santa using a secret key + number MD5 hash
# which needs to start with 5/6 zeroes for a succesful mine

my $secret_key = "ckczppom";
# comes after secret key to complement it
my $ending_num = 1;

for (; ; $ending_num++)
{
  my $str = md5_hex("$secret_key$ending_num");
  
  last if substr($str, 0, 6) eq "000000";
}

print "ending num ($ending_num)";
