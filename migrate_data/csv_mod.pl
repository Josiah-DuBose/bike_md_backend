use strict;
use warnings;
use Data::Dumper;


sub map_model_names {
    my %model_map = (
        "1" => "Honda",
        "2" => "Suzuki",
        "3" => "Yamaha",
        "4" => "Triumph",
        "5" => "Harley Davidson",
        "6" => "Ducati",
        "7" => "Victory",
        "8" => "Kawasaki"
    );

    my $input = "model.csv";
    open(INPUT, $input);

    my $output = 'model_brand_names.csv';
    open(OUTPUT, '>'.$output);

    while (my $line = <INPUT>) {
        my @values = split(',', $line);
        my $key = $values[0];
        if (exists $model_map{$key}) {
            $values[0] = ($model_map{$key});
        }
        print(Dumper(\@values));
         print OUTPUT join(",", "@values");
    }
}

sub map_years {
    my %year_map = (
        "2005" => "1",
        "2006" => "2",
        "2007" => "3",
        "2008" => "4",
        "2009" => "5",
        "2010" => "6",
        "2011" => "7",
        "2012" => "8",
        "2013" => "8",
        "2014" => "9",
        "2015" => "10",
        "2016" => "11"
    );

    my $input = "model.csv";
    open(INPUT, $input) or die "Could not open $input: $!";

    my $output = 'model_year_id.csv';
    open(OUTPUT, '>'.$output) or die "Could not open $output: $!";

    while (my $line = <INPUT>) {
        my @values = split(',', $line);
        my $key = $values[2];
        print("key ".$key."\n");
        if (exists $year_map{$key}) {
            print(Dumper($year_map{$key}));
            $values[2] = ($year_map{$key});
        }
        print(Dumper(\@values));
        print OUTPUT join(",", @values), "\n";
    }

    1;

}

eval {
    map_model_names();
    map_years();

}
