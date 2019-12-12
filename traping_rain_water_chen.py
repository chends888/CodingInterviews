class Solution:
    def trap(self, height: List[int]) -> int:
        # Total water trapped
        water = 0
        # Two lists for the max walls for each side of a column
        maxl = [0]
        maxr = [0]
        # Two variables for temporary max walls
        mleft = 0
        mright = 0
        # Iterate through the height list
        for index in range(len(height)):
            # Skip the first element
            if (index > 0):
                # Append the max left till the moment
                if (height[index-1] > mleft):
                    mleft = height[index-1]
                maxl.append(mleft)
            # Iterating backwards on the height list
            index = -index-1
            # Skip the las element
            if (index < -1):
                # Append the max right till the moment
                if (height[index+1] > mright):
                    mright = height[index+1]
                maxr.insert(0, mright)
        # Loop to iterate through height
        for index, column in enumerate(height):
            # Skip the first and last elements
            if ((index > 0) and (index < len(height)-1)):
                # Calculate the water trapped by subtracting the the current wall from the shortest side wall
                trap = min(maxl[index], maxr[index]) - column
                if (trap > 0):
                    water += trap
        return water
