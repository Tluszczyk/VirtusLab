# VirtusLab

The *join* program, will join two csv(rfc4180) files into one joined file. The trick is, both of these files can be way bigger, than the available memory. The solution is simple. Slice both files into smaller bulks, which can be stored in the memory, sort them, and merge into two sorted files. Now we can simply join them.

You can run the *join* script by typing 
    join file_path file_path column_name [join_type]
    
When ou can run it, it will create and remove temporary sorted chunks, as well as whole sorted files. As output, the script generates joined csv file, and also prints the result to the stdout.
