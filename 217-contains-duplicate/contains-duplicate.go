func containsDuplicate(nums []int) bool {
    var map_name = map[int]int{}
    fmt.Println(map_name)
    for i:=0; i< len(nums); i++{
        _, ok :=map_name[nums[i]]
        if ok == false{
            map_name[nums[i]] =  1
        } else {
            return true
        }
    }
    return false
}