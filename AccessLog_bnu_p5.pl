use strict;
use warnings;
use English qw(-no_match_vars);

my %IP_hash;

open(Log,"C:/Strawberry/qq/access.log") or die "File can't be opened";

while( <Log> ) 
	{
        if (/((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))/) 
			{ 
				$IP_hash{$1}++ 
			}  
	}
close Log;

my @sorted_keys = sort {$IP_hash{$b} <=> $IP_hash{$a}} keys %IP_hash;

for(my $i = 0; $i < 10; $i++) {

  print "$sorted_keys[$i]: $IP_hash{$sorted_keys[$i]}\n";
}