class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    """
    New methods start here
    """

    def compare_next_item(self):
        """
        Performs "bubble sort" functionality with an item already held; moves right, compares items, swaps if needed, moves left and places the held item, moves right and picks up the item there.
        """
        self.move_right()
        if self.compare_item() <= 0:
            self.move_left()
            self.swap_item()
            self.move_right()
            self.swap_item()
        else:
            self.swap_item()
            self.set_light_off()
            self.move_left()
            self.swap_item()
            self.move_right()
            self.swap_item()

    def sort(self):
        """
        Sort the robot's list.
        """
        """
        How is this robot going to sort this list?
        My robot (beta version) is a bubble sort robot. It picks up the first item, moves right, and compares the items; if the held item is lesser than or equal, the robot moves left, drops the item, moves right, picks up the item, and continues; if the held item is greater, it swaps them, moves left, sets the lesser item down, moves right, picks up the item, and continues. The robot's light is used to determine whether the list is sorted; the light is turned on at the start of each sort attempt and is turned off whenever a swap is made, so if it reaches the end of the list with the light still on, the sort is complete.

        For future versions:
        I considered trying to implement a merge sort, since you can definitely look at this data as a bunch of individual lists to be merged. I could get it to a list of sorted pairs easily enough I think; but I couldn't nail down a way for my robot to have enough info to successfully merge the lists from there.

        Similarly for quicksort, it was an appealing option at the start but the limited capabilities of the robot to hold onto any specific value rather than just comparing what it's holding to what's in front of it meant I never really got started down that road.
        """
        while self.can_move_left():
            self.move_left()
        if not self.can_move_right():
            return "List sorted successfully!"
        self.swap_item()
        self.set_light_on()
        while self.can_move_right():
            self.compare_next_item()
        if self.light_is_on():
            self.swap_item()
            return "List sorted successfully!"
        else:
            self.swap_item()
            while self.can_move_left():
                self.move_left()
            self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
