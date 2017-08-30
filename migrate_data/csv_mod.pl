use strict;
use warnings;
use Data::Dumper;

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

my $output = 'models.csv';
open(OUTPUT, '>'.$output);

while (my $line = <INPUT>) {
    my @values = split(',', $line);
    my $key = $values[0];
    if (exists $model_map{$key}) {
        $values[0] = ($model_map{$key});
    }
    print(Dumper(\@values));
    print OUTPUT "@values";
}
