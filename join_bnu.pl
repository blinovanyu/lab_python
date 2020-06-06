use v6;

my $arr={};
my $i;

if (my $F1 = open "C:/myperl/file1.txt", :r) 
{ 
	for $F1.lines -> $l  
		{ 
			my $r = ($l ~~ /(\S+)\s(\d+)/);
			if !$r[0] or !$r[1] {next;}		
			$arr{$r[0]}{'age'} = $r[1];
	}
	close($F1);
}
else {die "File 1 can't be opened";}

if (my $F2 = open "C:/myperl/file2.txt", :r) 
{ 
	for $F2.lines -> $l  
		{ 
			my $r = ($l ~~ /(\S+)\s(\d+)/);
			if !$r[0] or !$r[1] {next;}		
			$arr{$r[0]}{'tp'} = $r[1];
	}
	close($F2);
}
else {die "File 1 can't be opened";}

say "Name\tAge\tTelephone\n";
if keys($arr).elems != 0 
{
	for $arr.keys.sort -> $i 
	{
		my $age = (!$arr{$i}{'age'}) ?? '-' !! $arr{$i}{'age'};
		my $tp = (!$arr{$i}{'tp'}) ?? '-' !! $arr{$i}{'tp'}; 
		say "$i\t$age\t$tp";
	}
} 
else {die "NULL";}


