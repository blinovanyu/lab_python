use v6;

my $IP_hash = {};
my $i=0;

if (my $Log = open "C:/myperl/access.log", :r) 
{
	say "Readind the log-file...";
	for $Log.lines -> $l  
		{
			if !(my $r = ($l ~~ /(^\d ** 0^..^4\.\d  ** 0^..^4\.\d  ** 0^..^4\.\d  ** 0^..^4) \s\- \s\-/)[0])
				{next;}
			if $IP_hash{$r} 
				{$IP_hash{$r} += 1;}
				else 
				{$IP_hash{$r} = 1}		
		}
	close $Log;
}
else {die "File can't be opened";}
say "Sorting...";
if keys($IP_hash).elems != 0 
{
	say "TOP-10 Results:";
	my @sorted_keys = $IP_hash.keys.sort: {$IP_hash{$^b} <=> $IP_hash{$^a}}; 
	for ^10
	{
		say "@sorted_keys[$i]: $IP_hash{@sorted_keys[$i]}";
		$i+= 1;
	}
} 
else {die "NULL";}