$language = "python"
$day_number = (Get-Date -Format "d ").TrimEnd()
$day_folder = "day$day_number"
$main_file = "a.py"
$input_file = "input.txt"

python gen.py $language $day_number

code $language
code -g "$language/$day_folder/$main_file"
code -g "$language/$day_folder/$input_file"