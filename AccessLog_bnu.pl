use v6;

my $IP_hash = {};
my $i=0;
my $j=0;

if (my $Log = open "C:/myperl/access.log", :r) 
{
	say "Readind the log-file...";
	for $Log.lines -> $l  
		{
			#$j+= 1;
			my ($r) = $l.split(' - - ');
			if ($r ~~ /(^\d ** 0^..^4\.\d  ** 0^..^4\.\d  ** 0^..^4\.\d  ** 0^..^4)/)
				{$IP_hash{$r}++;}
				#last if ($j == 50);
		}
	close $Log;
}
else {die "File can't be opened";}

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
