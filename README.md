# camera-problem
Camera Problem

Here is some progress for the camera duplicates test. My initial thoughts leaned me towards a near duplicate detection algorithm. Something along the lines of breaking each string into shingles and calculating Jaccard similarity. Although it would be an interesting approach, the similarity of something like Canon Mark II and Canon Mark III would be extremely high, but would be considered two very different models. So I moved on to a more brute force approach.

My approach was to iterate over each entry in the file, clean the entry up with some basic regex replacements for things like abbreviations mk -> Mark, and numbers to roman numerals 2 -> II. I split the various types of formatting up into separate functions and ensured the ability to add formatting rules as I found them from the data. 

Once the entry was formatted, I remove white space and lower cased the string to create a dictionary key. If the dictionary had an existing entry, I did a name check to determine if the entry name was better than the existing. If better, the entry name takes the place in the lookup dictionary. Names that were more verbose seemed to look better, with more appropriate spacing and such, so I did a length check on each name to determine which was better.

The next step would probably be to create a list of negative matches that, if the entry matches, excludes the entry from being included in the updated list.