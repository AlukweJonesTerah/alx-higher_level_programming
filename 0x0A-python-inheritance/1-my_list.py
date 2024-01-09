#!urs/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Returns:a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
