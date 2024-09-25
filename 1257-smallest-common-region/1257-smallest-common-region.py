class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        # Create a dictionary to map each region to its parent region.
        parent_map = {}
        for region in regions:
            # region[0] is the parent region, and the rest are the child regions.
            for child_region in region[1:]:
                parent_map[child_region] = region[0]
      
        # A set to store all the ancestors of region1.
        ancestors = set()
        # Loop to find all ancestors of region1 and add them to the set.
        while region1 in parent_map:
            ancestors.add(region1)
            # Move to the parent region.
            region1 = parent_map[region1]
      
        # Loop to traverse the ancestors of region2.
        while region2 in parent_map:
            # Check if the current region2 is also an ancestor of region1.
            if region2 in ancestors:
                # If it is, we have found the smallest common region.
                return region2
            # Move to the parent region of region2.
            region2 = parent_map[region2]
      
        # If there is no common ancestor in the set, the smallest common
        # region is the topmost ancestor of region1.
        return region1
