class Solution(object):
    
    def slope(self, c1, c2):
        dominator = float(c2[1] - c1[1])
        divider = float(c2[0] - c1[0])

        # On X Axis
        if (divider == 0):
            return 0.0, True, False

        # On Y Axis
        if (dominator == 0):
            return 0.0, False, True

        return dominator / divider, False, False
        
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        c1 = coordinates[0]
        i_slope, i_x_axis, i_y_axis = self.slope(c1, coordinates[1])
        for i in range(1, len(coordinates)):
            c2 = coordinates[i]
            c_slope, c_x_axis, c_y_axis = self.slope(c1, c2)
            
            if i_x_axis and not c_x_axis:
                return False
            
            if i_y_axis and not c_y_axis:
                return False
            
            if c_slope != i_slope:
                return False
        
        return True