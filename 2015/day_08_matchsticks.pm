use 5.38.2;

# Day 8: Matchsticks
# Part 1
# Count outputted string contents (with regex).

my $santas_text_file = q!""
"abc"
"aaa\"aaa"
"\x27"!;

my $total_str_len = 0;
my $total_str_contents_len = 0;

for (split(/\n/, $santas_text_file))
{
  $total_str_len += length(); 
  $total_str_contents_len += length();
  $total_str_contents_len -= 2;
  # remove quotes
  $total_str_contents_len -=  $_ =~ /\\"/g;
  # remove backslashes
  $total_str_contents_len -=  $_ =~ /\\\\/g;
  # remove hexadecimal characters like \x27
  $total_str_contents_len -=  3 * $_ =~ /[^\\]\\x[\w]{2}/g;
}


say "Str length is: $total_str_len
and content len is: $total_str_contents_len
difference of these is: @{[$total_str_len - $total_str_contents_len]}";
