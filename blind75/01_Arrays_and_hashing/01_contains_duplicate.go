# check if there any duplicates in a given int array

####################################################################
# GO
# Solution 1 = SORTING ; TC: O(n log n), SC: O(1)

func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i, _ := range(nums) {
        if i < len(nums)-1 && nums[i] == nums[i+1] {
            return true
        }
    }
    return false
}

# Solution 2 = USE SETS ; TC: O(n), SC : O(n)

func containsDuplicate(nums []int) bool {
    set := make(map[int]struct{})

    for _, num := range(nums) {
        if _, ok := set[num]; ok {
            return true
        }
        set[num] = struct{}{}
    }
    return false
}
