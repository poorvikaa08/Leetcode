int averageValue(int* nums, int numsSize) {
    
    int i, sum=0, count=0;


    sum = 0, count = 0;
    for (i = 0; i < numsSize; i++) {
        if ((nums[i] % 2) == 0) {
            if ((nums[i] % 3) == 0) {
                sum += nums[i];
                count++;
            }
        }
    }

    if(count==0)
      return 0;

    return sum/count;  
    
}